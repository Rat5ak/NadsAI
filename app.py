import sys
import os
import re
import json
from datetime import datetime
from flask import Flask, request, render_template, send_file, url_for
from flask_socketio import SocketIO, emit
from maestro_gpt4o import process_objective, create_zip, gpt_orchestrator, gpt_sub_agent, anthropic_refine, create_folder_structure

# Initialize Flask and Flask-SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    objective = request.form['objective']
    use_search = 'use_search' in request.form
    
    # Call your existing logic to handle the objective
    project_name = process_objective_with_updates(objective, use_search)
    
    # Create a zip of the project directory
    zip_path = create_zip(project_name)
    
    # Emit an event to notify the client that the zip file is ready
    zip_url = url_for('download_file', filename=os.path.basename(zip_path))
    socketio.emit('zip_ready', {'zip_url': zip_url})
    
    return '', 200

@app.route('/downloads/<filename>')
def download_file(filename):
    file_path = os.path.join(app.root_path, 'downloads', filename)
    if not os.path.exists(file_path):
        return "File not found", 404
    return send_file(file_path, as_attachment=True)

def process_objective_with_updates(objective, use_search):
    file_content = None
    task_exchanges = []
    gpt_tasks = []

    while True:
        previous_results = [result for _, result in task_exchanges]
        if not task_exchanges:
            gpt_result, file_content_for_gpt, search_query = gpt_orchestrator(objective, file_content, previous_results, use_search)
        else:
            gpt_result, _, search_query = gpt_orchestrator(objective, previous_results=previous_results, use_search=use_search)

        if "The task is complete:" in gpt_result:
            final_output = gpt_result.replace("The task is complete:", "").strip()
            break
        else:
            sub_task_prompt = gpt_result
            if file_content_for_gpt and not gpt_tasks:
                sub_task_prompt = f"{sub_task_prompt}\n\nFile content:\n{file_content_for_gpt}"
            sub_task_result = gpt_sub_agent(sub_task_prompt, search_query, gpt_tasks, use_search)
            gpt_tasks.append({"task": sub_task_prompt, "result": sub_task_result})
            task_exchanges.append((sub_task_prompt, sub_task_result))
            file_content_for_gpt = None
        
        # Emit an event to update the client with the current progress
        socketio.emit('progress_update', {'message': format_progress(sub_task_prompt)})
        socketio.sleep(1)  # Sleep to ensure the client has time to receive updates

    sanitized_objective = re.sub(r'\W+', '_', objective)
    timestamp = datetime.now().strftime("%H-%M-%S")
    refined_output = anthropic_refine(objective, [result for _, result in task_exchanges], timestamp, sanitized_objective)

    project_name_match = re.search(r'Project Name: (.*)', refined_output)
    project_name = project_name_match.group(1).strip() if project_name_match else sanitized_objective

    folder_structure_match = re.search(r'<folder_structure>(.*?)</folder_structure>', refined_output, re.DOTALL)
    folder_structure = {}
    if folder_structure_match:
        json_string = folder_structure_match.group(1).strip()
        try:
            folder_structure = json.loads(json_string)
        except json.JSONDecodeError as e:
            socketio.emit('progress_update', {'message': f'Error parsing JSON: {e}'})
            socketio.emit('progress_update', {'message': f'Invalid JSON string: {json_string}'})

    code_blocks = re.findall(r'Filename: (\S+)\s*```[\w]*\n(.*?)\n```', refined_output, re.DOTALL)
    create_folder_structure(project_name, folder_structure, code_blocks)

    return project_name

def format_progress(text):
    text = re.sub(r'###\s?', '', text)  # Remove markdown headers
    text = text.replace('\n', '<br>')  # Replace new lines with HTML line breaks
    return text

if __name__ == '__main__':
    socketio.run(app, debug=True)
