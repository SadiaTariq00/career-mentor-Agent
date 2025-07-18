import chainlit as cl
from model.gemini_model import GeminiModel
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

FIELDS = [
    "Frontend Developer",
    "Data Analyst",
    "AI Researcher",
    "Cybersecurity Specialist",
    "UX Designer"
]

model = GeminiModel()
career_agent = CareerAgent(model)
skill_agent = SkillAgent()
job_agent = JobAgent()

def extract_recommended_field(response: str) -> str:
    for field in FIELDS:
        if f"career as a {field}" in response or f"career as an {field}" in response:
            return field
    return None

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.strip()

    try:
        lowered = user_input.lower()

        if "roadmap" in lowered or "skills" in lowered:
            for field in FIELDS:
                if field.lower() in lowered:
                    await cl.Message(content=f"🧠 Here's what you'll need to become a great **{field}**:\n\n{skill_agent.run(field)}").send()
                    return
            await cl.Message(content="📌 Please mention a valid career field like **Frontend Developer**, **Data Analyst**, or **UX Designer**.").send()
            return

        # Job Roles
        elif "job" in lowered or "roles" in lowered:
            for field in FIELDS:
                if field.lower() in lowered:
                    await cl.Message(content=f"💼 These are typical job roles in **{field}**:\n\n{job_agent.run(field)}").send()
                    return
            await cl.Message(content="📌 Kindly include a known field like **AI Researcher**, **Cybersecurity Specialist**, or **UX Designer**.").send()
            return

        # Main Career Suggestion
        response = career_agent.run(user_input)
        await cl.Message(content=response).send()

        recommended_field = extract_recommended_field(response)
        if recommended_field:
            await cl.Message(content=f"📚 Based on that, here's your skill roadmap for **{recommended_field}**:\n\n{skill_agent.run(recommended_field)}").send()
            await cl.Message(content=f"🔍 And here are the job roles you might target as a **{recommended_field}**:\n\n{job_agent.run(recommended_field)}").send()

    except Exception as e:
        await cl.Message(content=f"❌ Oops! Something went wrong:\n`{str(e)}`").send()
