# Nads AI Project Generator

Welcome to the Nads AI Project Generator! This project is designed to streamline the creation of various coding projects by leveraging AI-powered tools to automate and simplify the development process. Save up to 90% of development costs and time on your projects with Nads AI!

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [API Keys Configuration](#api-keys-configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

Nads AI Project Generator is an AI-powered web application that helps developers create project templates quickly and efficiently. By providing an objective, the AI generates a customized project structure and initial codebase, reducing development time and effort.

## Features

- **Automated Project Creation**: Generate project templates based on objectives.
- **Customizable**: Easily modify generated templates to fit specific needs.
- **Real-time Collaboration**: Work with team members in real-time.
- **Cost-effective**: Save up to 90% on development costs.

## Installation

1.  Clone the repository:
    
    ```sh
    git clone https://github.com/Rat5ak/NadsAI.git
    ```
    
2.  Navigate to the project directory:
    
    ```sh
    cd NadsAI
    ```
    
3.  Install the dependencies:
    
    ```sh
    pip install -r requirements.txt
    ```
    

## Usage

Run the application:

```sh
python app.py
```

Open your web browser and go to `http://localhost:5000` to access the Nads AI Project Generator interface.

## Project Structure

- `app.py`: Contains the Flask and Flask-SocketIO code to handle project generation and downloading.
- `index.html`: Contains the front-end code for the project generator interface.
- `styles.css`: Contains the CSS styles for the project.
- `download.png`: An image file used in the front-end.
- `maestro_gpt4o.py`: Contains the core functions for processing objectives and creating projects.
- `requirements.txt`: Lists the dependencies for the project.

## Technologies Used

- **Flask**: Web framework for Python.
- **Flask-SocketIO**: Provides real-time communication between the client and server.
- **OpenAI**: For generating content and code using GPT-4o.
- **Anthropic**: For refining and improving generated content.
- **Tavily**: For search functionality.
- **HTML/CSS**: For front-end structure and design.
- **JavaScript**: For handling client-side interactions.

## API Keys Configuration

Ensure you have valid API keys for OpenAI, Anthropic, and Tavily. Set these keys in the `maestro_gpt4o.py` file:

```python
openai_client = OpenAI(api_key="your_openai_api_key")
anthropic_client = Anthropic(api_key="your_anthropic_api_key")
```

## Contributing

We welcome contributions to improve Nads AI Project Generator! Here are a few ways you can help:

- **Report bugs**: If you find any issues, please report them using GitHub Issues.
- **Suggest features**: If you have ideas for new features, we would love to hear about them.
- **Submit pull requests**: If you want to contribute code, please fork the repository and create a pull request.

### Steps to Contribute

1.  **Fork the repository**.
    
2.  **Create a new branch**:
    
    ```sh
    git checkout -b feature/your-feature-name
    ```
    
3.  **Make your changes** and commit them:
    
    ```sh
    git commit -m "Add some feature"
    ```
    
4.  **Push to your branch**:
    
    ```sh
    git push origin feature/your-feature-name
    ```
    
5.  **Create a pull request** on GitHub.
    

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

* * *

Thank you for using Nads AI Project Generator! If you have any questions or need further assistance, please feel free to open an issue on GitHub.
