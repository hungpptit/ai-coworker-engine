# LangGraph state routing and node definitions
from app.agents.chro_agent import GucciCHROAgent, AgentState

class SimulationOrchestrator:
    def __init__(self):
        self.chro_agent = GucciCHROAgent()

    def process_chat_flow(self, state: AgentState, message: str):
        # Định tuyến qua các node đại diện cho Agent
        return self.chro_agent.execute_turn(state, message)