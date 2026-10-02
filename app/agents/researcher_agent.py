from app.agents.base_agent import BaseAgent


class ResearcherAgent(BaseAgent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "researcher", "researcher", ["research", "analysis"])

    async def run(self, task: dict):
        return {
            "agent": self.name,
            "task": task["name"],
            "status": "completed",
            "summary": "Research completed",
            "facts": ["Fact 1", "Fact 2", "Fact 3"],
        }
