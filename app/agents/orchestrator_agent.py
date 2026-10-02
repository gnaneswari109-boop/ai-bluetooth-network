from app.agents.base_agent import BaseAgent


class OrchestratorAgent(BaseAgent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "orchestrator", "orchestrator", ["planning", "coordination"]) 

    async def run(self, task: dict):
        return {
            "agent": self.name,
            "task": task["name"],
            "status": "orchestrating",
            "result": "Task delegated to specialists"
        }
