from abc import ABC, abstractmethod


class BaseAgent(ABC):
    def __init__(self, agent_id: str, name: str, role: str, capabilities: list[str]):
        self.agent_id = agent_id
        self.name = name
        self.role = role
        self.capabilities = capabilities

    @abstractmethod
    async def run(self, task: dict):
        raise NotImplementedError
