from app.agents.base_agent import BaseAgent


class SummarizerAgent(BaseAgent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "summarizer", "summarizer", ["summary", "reporting"]) 

    async def run(self, task: dict):
        return {
            "agent": self.name,
            "task": task["name"],
            "status": "completed",
            "result": {
                "summary": "Final summary compiled from all specialist outputs"
            }
        }
