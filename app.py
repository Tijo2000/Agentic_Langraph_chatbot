from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

groq_api_key = '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'
os.environ["TAVILY_API_KEY"] = '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'

MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768"
]

tool_tavily = TavilySearchResults(max_results=2)
tools = [tool_tavily]

app = FastAPI(title='LangGraph AI Agent')

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model."}

    llm = ChatGroq(groq_api_key=groq_api_key, model_name=request.model_name)

    # Define a state modifier function
    def state_modifier(state):
        state["system_prompt"] = request.system_prompt
        return state

    agent = create_react_agent(llm, tools=tools, state_modifier=state_modifier)

    state = {"messages": request.messages}
    result = agent.invoke(state)

    # Ensure the result is in the expected format
    return {"messages": [{"type": "ai", "content": result.get("output", "No response generated.")}]}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.1', port=8000)