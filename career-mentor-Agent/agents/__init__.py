from .career_agent import CareerAgent
from .skill_agent import SkillAgent
from .job_agent import JobAgent
from model.gemini_model import GeminiModel

# ---------------------------
# Runner class defined here
# ---------------------------
class Runner:
    def __init__(self, agents):
        """
        Initialize Runner with a list of agents.
        Converts list to dict with class name keys for easy lookup.
        """
        if isinstance(agents, list):
            self.agents = {agent.__class__.__name__: agent for agent in agents}
        else:
            self.agents = agents

    async def run(self, agent_name: str, query: str):
        """
        Call the specified agent by name with the query.
        Handles async if needed.
        """
        agent = self.agents.get(agent_name)
        if not agent:
            return f"⚠️ No agent found with name {agent_name}"

        result = agent.run(query)
        if hasattr(result, "__await__"):  # check for async
            return await result
        return result

# ---------------------------
# Initialize model & agents
# ---------------------------
model = GeminiModel()
career_agent = CareerAgent(model)
skill_agent = SkillAgent()
job_agent = JobAgent()

# Runner instance
runner = Runner([career_agent, skill_agent, job_agent])
