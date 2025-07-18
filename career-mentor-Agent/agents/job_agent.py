from tools.job_roles_tool import get_job_roles

class JobAgent:
    def __init__(self):
        self.name = "JobAgent"

    def run(self, field: str) -> str:
        intro = "🧾 I'm the **Job Agent**. Let's look at the real-world job roles available in your chosen career field."

        valid_fields = [
            "Frontend Developer",
            "Data Analyst",
            "AI Researcher",
            "Cybersecurity Specialist",
            "UX Designer"
        ]

        if field in valid_fields:
            roles = get_job_roles(field)
            return intro + f"\n\n💼 **Job roles for {field}** may include:\n{roles}"

        return intro + (
            "\n\n⚠️ Sorry, I don't have information for that field yet.\n"
            "Try one of these: **Frontend Developer**, **Data Analyst**, **AI Researcher**, **Cybersecurity Specialist**, or **UX Designer**."
        )
