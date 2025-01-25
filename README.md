# Agentic_Langraph_chatbot
Agentic LangGraph Chatbot 🤖
A conversational AI chatbot built with LangGraph and LangChain, designed to handle multi-agent workflows for dynamic, context-aware interactions. Perfect for applications in customer support, personal assistants, and specialized domain expertise.

License: MIT
Python 3.9+
Dependencies

🚀 Features
Multi-Agent Workflows: Coordinate autonomous agents for complex tasks.

Persona-Based Interactions: Specialized agents for travel planning, finance, coding, and general assistance.

PDF Processing: Extract and summarize text from PDF documents.

REST API: Built with FastAPI for seamless integration.

Groq Integration: Optional high-speed LLM inference via Groq's API.

📦 Installation
Clone the repository:

bash
Copy
git clone https://github.com/Tijo2000/Agentic_Langraph_chatbot.git
cd Agentic_Langraph_chatbot
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up API keys (create a .env file):

bash
Copy
OPENAI_API_KEY="your_openai_key"
GROQ_API_KEY="your_groq_key"  # Optional
🛠️ Usage
Run the Chatbot
Start the FastAPI server:

bash
Copy
uvicorn app.main:app --reload
Example API Requests
Chat with the Travel Planner Agent:

bash
Copy
curl -X POST "http://localhost:8000/chat/travel" \
-H "Content-Type: application/json" \
-d '{"message": "Plan a 3-day trip to Paris"}'
Process a PDF:

bash
Copy
curl -X POST "http://localhost:8000/process-pdf" \
-F "file=@/path/to/your/document.pdf"
Run Tests
bash
Copy
pytest tests/
📂 Project Structure
plaintext
Copy
Agentic_Langraph_chatbot/
├── app/
│   ├── models/          # Pydantic schemas and data models
│   ├── services/        # Core logic for agents and workflows
│   ├── utils/           # Helper functions (PDF processing, API calls)
│   └── main.py          # FastAPI entry point
├── assets/              # Diagrams and screenshots
├── tests/               # Unit and integration tests
├── requirements.txt     # Dependencies
└── .env.example         # Environment variable template
⚙️ Configuration
Configure agents and models in app/config.py:

python
Copy
class Settings(BaseSettings):
    openai_api_key: str
    groq_api_key: Optional[str] = None
    model_name: str = "gpt-4"  # Switch to "mixtral-8x7b" for Groq
🤝 Contributing
Fork the repository.

Create a branch: git checkout -b feature/your-idea.

Commit changes: git commit -m "Add your feature".

Push to the branch: git push origin feature/your-idea.

Open a Pull Request.

📄 License
This project is licensed under the MIT License. See LICENSE for details.

🙌 Acknowledgments
Built with LangChain and LangGraph.

API framework by FastAPI.

LLM inference powered by Groq.
