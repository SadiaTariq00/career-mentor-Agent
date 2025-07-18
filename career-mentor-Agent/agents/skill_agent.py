from tools.skill_roadmap_tool import get_career_roadmap

class SkillAgent:
    def __init__(self):
        self.name = "SkillAgent"

    def run(self, field: str) -> str:
        intro = "📘 I'm the **Skill Agent**. I'll guide you through the essential skills for your chosen career."

        valid_fields = [
            "Frontend Developer",
            "Data Analyst",
            "AI Researcher",
            "Cybersecurity Specialist",
            "UX Designer"
        ]

        if field in valid_fields:
            skills = get_career_roadmap(field)
            return intro + f"\n\n📚 To become a **{field}**, you should focus on learning:\n{skills}"

        return intro + (
            "\n\n⚠️ Hmm, I don't have a roadmap for that field yet.\n"
            "Try one of these: **Frontend Developer**, **Data Analyst**, **AI Researcher**, **Cybersecurity Specialist**, or **UX Designer**."
        )
