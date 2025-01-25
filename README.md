<<<<<<< HEAD
# Langraph_chatbot
=======
# Langraph_chatbot : 
https://tijo-langchat.streamlit.app/
>>>>>>> 7896852c9bdaaae41fd48190acb2f399ee642ce8

This project is a chatbot application built using FastAPI, Streamlit, and LangGraph. The chatbot interacts with users through a web interface and processes their messages using a LangGraph-based agent.

## Project Structure
<<<<<<< HEAD
=======
```sh
>>>>>>> 7896852c9bdaaae41fd48190acb2f399ee642ce8
Agentic_Langraph_chatbot/
├── app.py                                    # Main file with fast api backend
├── Dockerfile                                # DockerFile
├── README.md                                 # Unit and integration tests
├── requirements.txt                          # Dependencies
└── ui.py                                     # Streamlit file for Frond end 
.env(Please add your api keys here, I didn't) # Environment variable template
<<<<<<< HEAD

=======
```
>>>>>>> 7896852c9bdaaae41fd48190acb2f399ee642ce8

## Tools and Libraries

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Streamlit**: An open-source app framework for Machine Learning and Data Science teams.
- **LangGraph**: A library for building and running language models.
- **Uvicorn**: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.

## Setup Instructions

Follow these steps to set up and run the project:

1. **Create a Conda Environment**:
    ```sh
    conda create -n langchat python=3.11 -y
    ```

2. **Activate the Conda Environment**:
    ```sh
    conda activate langchat
    ```

3. **Install the Required Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the FastAPI and Streamlit Servers**:
    ```sh
    uvicorn app:app --reload
    streamlit run ui.py
    ```

Alternatively, you can use Docker to run the project:

1. **Build the Docker Image**:
    ```sh
    docker build -t langraph_chatbot .
    ```

2. **Run the Docker Container**:
    ```sh
    docker run -p 8000:8000 -p 8501:8501 langraph_chatbot
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Define your AI agent by entering a system prompt.
3. Select a model from the dropdown menu.
4. Enter your message(s) and click the "Submit" button.
5. View the agent's response on the web interface.

## Notes

- Ensure that the FastAPI server is running on `http://127.0.0.1:8000` as the Streamlit app communicates with this endpoint.
- The Dockerfile is configured to expose ports 8000 and 8501 for FastAPI and Streamlit, respectively.

## License

This project is licensed under the MIT License.
