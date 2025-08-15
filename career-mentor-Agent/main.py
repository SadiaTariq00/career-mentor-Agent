import chainlit as cl

from agents import runner, career_agent, skill_agent, job_agent

FIELDS = [
    "Frontend Developer",
    "Data Analyst",
    "AI Researcher",
    "Cybersecurity Specialist",
    "UX Designer"
]

def extract_recommended_field(response: str) -> str:
    for field in FIELDS:
        if f"career as a {field}" in response or f"career as an {field}" in response:
            return field
    return None

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.strip()
    lowered = user_input.lower()

    try:
        # Skill roadmap
        if "roadmap" in lowered or "skills" in lowered:
            for field in FIELDS:
                if field.lower() in lowered:
                    skills = await runner.run("SkillAgent", field)
                    await cl.Message(content=f"🧠 Here's what you'll need to become a great **{field}**:\n\n{skills}").send()
                    return
            await cl.Message(content="📌 Please mention a valid career field like **Frontend Developer**, **Data Analyst**, or **UX Designer**.").send()
            return

        # Job roles
        elif "job" in lowered or "roles" in lowered:
            for field in FIELDS:
                if field.lower() in lowered:
                    jobs = await runner.run("JobAgent", field)
                    await cl.Message(content=f"💼 These are typical job roles in **{field}**:\n\n{jobs}").send()
                    return
            await cl.Message(content="📌 Kindly include a known field like **AI Researcher**, **Cybersecurity Specialist**, or **UX Designer**.").send()
            return

        # Main career suggestion
        response = await runner.run("CareerAgent", user_input)
        await cl.Message(content=response).send()

        # Auto skills & jobs if career suggested
        recommended_field = extract_recommended_field(response)
        if recommended_field:
            skills = await runner.run("SkillAgent", recommended_field)
            await cl.Message(content=f"📚 Here's your skill roadmap for **{recommended_field}**:\n\n{skills}").send()

            jobs = await runner.run("JobAgent", recommended_field)
            await cl.Message(content=f"🔍 Job roles for **{recommended_field}**:\n\n{jobs}").send()

    except Exception as e:
        await cl.Message(content=f"❌ Oops! Something went wrong:\n`{str(e)}`").send()
