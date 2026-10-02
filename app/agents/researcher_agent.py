from app.agents.base_agent import BaseAgent


class ResearcherAgent(BaseAgent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "researcher", "researcher", ["research", "analysis"]) 

    async def run(self, task: dict):
        return {
            "agent": self.name,
            "task": task["name"],
            "status": "completed",
            "result": {
                "summary": "Research data collected for the task",
                "facts": ["fact 1", "fact 2", "fact 3"]
            }
        }
