# Background deadlock analysis agent
from typing import Dict, Any, List

class DirectorSupervisor:
    @staticmethod
    def analyze_conversation(message: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        """Phân tích ngầm tin nhắn và lịch sử để phát hiện deadlock hoặc vi phạm"""
        has_centralization_flaw = any(word in message.lower() for word in ["force", "standardize 100%", "centralize all", "mandatory"])
        is_jailbreak = any(word in message.lower() for word in ["ignore previous", "system prompt", "developer mode"])
        
        # Thuật toán phát hiện vòng lặp hội thoại
        is_user_stuck = False
        if len(history) >= 2:
            last_user_msgs = [turn["user"] for turn in history[-2:] if "user" in turn]
            if message.lower() in [m.lower() for m in last_user_msgs]:
                is_user_stuck = True
                
        return {
            "is_violation": has_centralization_flaw,
            "is_jailbreak": is_jailbreak,
            "is_user_stuck": is_user_stuck
        }