from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agents.chro_agent import AgentState
from app.graph import SimulationOrchestrator

app = FastAPI(title="AI Co-worker Engine - Edtronaut Assignment")
orchestrator = SimulationOrchestrator()

class ChatRequest(BaseModel):
    user_message: str
    state: AgentState

class ChatResponse(BaseModel):
    assistant_message: str
    updated_state: AgentState
    safety_flags: dict

@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        msg, updated_state, safety = orchestrator.process_chat_flow(request.state, request.user_message)
        return ChatResponse(
            assistant_message=msg,
            updated_state=updated_state,
            safety_flags=safety
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    # Sử dụng đường dẫn dạng module path "app.main:app" để tránh lỗi đường dẫn tuyệt đối trong Python
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)