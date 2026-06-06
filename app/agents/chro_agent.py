# CHRO NPC logic class implementation
from typing import Tuple, Dict
from pydantic import BaseModel
from app.prompts.system_instructions import CHRO_SYSTEM_PROMPT
from app.agents.director_agent import DirectorSupervisor

class AgentState(BaseModel):
    conversation_history: list = []
    temperament_score: float = 1.0
    violation_count: int = 0

class GucciCHROAgent:
    def __init__(self):
        self.base_prompt = CHRO_SYSTEM_PROMPT

    def execute_turn(self, state: AgentState, user_message: str) -> Tuple[str, AgentState, Dict[str, bool]]:
        # Gọi Director Layer kiểm tra ngầm
        analysis = DirectorSupervisor.analyze_conversation(user_message, state.conversation_history)
        safety_flags = {"jailbreak_attempt": analysis["is_jailbreak"]}
        
        if analysis["is_violation"]:
            state.violation_count += 1
            state.temperament_score = max(0.1, state.temperament_score - 0.3)
            
        # Kỹ thuật Context Mutation nếu điểm thiện cảm quá thấp
        active_prompt = self.base_prompt
        if state.temperament_score <= 0.4:
            active_prompt += "\n[MUTATION] Your tone is now strictly formal, cold, and highly demanding."

        # Định tuyến phản hồi dựa trên phân tích hệ thống
        if analysis["is_jailbreak"]:
            response = "I cannot comply with that request. Let's refocus on building the leadership framework for Gucci Group."
        elif analysis["is_user_stuck"]:
            response = (
                "Let's break the cycle for a moment. We seem to be stuck on high-level alignment. "
                "Tactically speaking, how can we leverage our 'Trust' pillar within the 360-degree appraisal blueprint?"
            )
        elif analysis["is_violation"]:
            response = "I have major reservations. Forcing absolute standardization across our Maisons kills brand DNA."
        else:
            response = "This balances our group synergy with individual brand autonomy well. What is your rollout timeline?"
            
        state.conversation_history.append({"user": user_message, "assistant": response})
        return response, state, safety_flags