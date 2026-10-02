from app.agents.base_agent import BaseAgent


class CodeAgent(BaseAgent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "coder", "coder", ["code", "implementation"])

    async def run(self, task: dict):
        return {
            "agent": self.name,
            "task": task["name"],
            "status": "completed",
            "summary": "Implementation prepared",
            "files": ["main.py", "service.py"],
        }
