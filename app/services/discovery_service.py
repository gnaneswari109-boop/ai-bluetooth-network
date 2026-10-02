from typing import Dict, List

AGENTS: Dict[str, dict] = {}


def register_agent(agent: dict):
    AGENTS[agent["agent_id"]] = agent
    return agent


def list_agents() -> List[dict]:
    return list(AGENTS.values())


def find_agents_by_capability(capability: str) -> List[dict]:
    return [
        agent for agent in AGENTS.values()
        if capability in (agent.get("capabilities") or [])
    ]
