# Speech Analysis Application

This repository contains code for a Flask-based web application for speech analysis. The application leverages various natural language processing (NLP) and speech recognition technologies to analyze conversations and identify key traits or habits of speakers.

## Contents

- [Overview](#overview)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Challenges](#challenges)
- [License](#license)

## Overview

LINK TO MY MODEL: https://speechanalysis-5ehzxowrfq-ue.a.run.app/

The application allows users to upload either text files or audio files containing conversations. It then processes the input data using OpenAI's language model and Deepgram's speech recognition API to analyze the conversation content. The analyzed data is then presented back to the user, highlighting key insights about each speaker.

## Features

- Supports analysis of both text and audio conversations.
- Utilizes OpenAI's language model for text analysis.
- Integrates Deepgram's API for speech-to-text transcription.
- Provides insights into the traits or habits of speakers based on the conversation content.
- Offers a simple and intuitive user interface for easy interaction.

## Dependencies

The application relies on the following dependencies:

- OpenAI (version 1.14.2)
- langchain-openai (version 0.1.1)
- Flask (version 3.0.2)
- Gunicorn (version 21.2.0)
- Other dependencies listed in `requirements.txt`

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

### (EXPLORER/HERO MODE)

To use the application locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/your-username/speech-analysis.git
    ```

2. **Install Dependencies**: Navigate to the project directory and install the necessary dependencies using pip:

    ```bash
    cd speech-analysis
    pip install -r requirements.txt
    ```

3. **Run the Application**: Start the Flask development server by running the following command:

    ```bash
    python app.py
    ```

    This command starts the application on port 5000.


To run the application using Docker, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/your-username/speech-analysis.git
    ```

2. **Build the Docker Image**: Navigate to the project directory and build the Docker image using the provided Dockerfile:

    ```bash
    cd speech-analysis
    docker build -t speech-analysis .
    ```

3. **Run the Docker Container**: After building the Docker image, run the container using Gunicorn:

    ```bash
    docker run -d -p 8080:8080 speech-analysis
    ```

    This command starts the containerized application on port 8080.

4. **Access the Application**: Open your web browser and navigate to `http://localhost:8080` to access the running application.


## Deployment

### Local Deployment

For local development and testing, you can use the Flask development server.

### Cloud Deployment
### (MASTER MODE)

To deploy the application to Google Cloud Run, follow these steps:

1. **Project Creation**: Create a new project on Google Cloud Platform (GCP) from the [Google Cloud Console](https://console.cloud.google.com/).

2. **Download the Cloud SDK**: Download and install the [Cloud SDK (gcloud CLI)](https://cloud.google.com/sdk/docs/install) on your local machine.

3. **Authentication**: Authenticate with your Google Cloud account using the following command and follow the prompts:

    ```bash
    gcloud auth login
    ```

4. **Project and Region Selection**: Set the default project and choose the appropriate region using the following commands:

    ```bash
    gcloud config set project [PROJECT_ID]
    gcloud config set run/region [REGION]
    ```

   Replace `[PROJECT_ID]` with your actual Google Cloud project ID (e.g., `speech-analysis-418123`) and `[REGION]` with your preferred region (e.g., `us-central1`).

5. **Artifact Permissions**: Ensure that your account has the necessary permissions for accessing Artifact Registry, Cloud Build, and Cloud Run services. Grant the appropriate roles using the IAM & Admin section of the [Google Cloud Console](https://console.cloud.google.com/iam-admin/iam).

6. **API Enablement**: Enable the required APIs (Artifact Registry API, Cloud Build API, Cloud Run API) using the [API & Services Dashboard](https://console.cloud.google.com/apis/dashboard).

7. **Initialization**: Initialize the gcloud CLI with the following command and follow the prompts:

    ```bash
    gcloud init
    ```

8. **Deployment**: Deploy your application to Google Cloud Run using the following command from the root directory of your project:

    ```bash
    gcloud run deploy --source .
    ```

   This command builds a Docker image from the current directory and deploys it to Cloud Run. Make sure that you have a `Dockerfile` and an `app.yaml` (or other required configuration files) in your project directory.

   Follow the prompts to specify the service name, allow unauthenticated invocations, and choose the appropriate region and platform (fully managed).

   Once the deployment is complete, you will receive a URL where your application is hosted on Google Cloud Run.

Replace `[PROJECT_ID]` and `[REGION]` with your actual project ID and preferred region, respectively.

## Challenges

1. Initially I faced version issues.
- To resolve this, I used version control
2. The model started hallucination and generating random insights and speakers.
- To remedy this, I tuned the temperature, removed buffer memory and tried various prompts.
3. Handling the transcribed text from audio file was tricky.
- I had to check the JSON format and it's contents.
4. I had to generalize the code because Flask typically runs on port 5000 by default, whereas the deployed model operates on port 8080.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

