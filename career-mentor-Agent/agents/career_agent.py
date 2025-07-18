class CareerAgent:
    def __init__(self, model):
        self.model = model
        self.introduced = False

    def run(self, user_input: str) -> str:
        intro = (
            "👋 Hello! I'm your **Career Mentor Agent**.\n"
            "🌟 I'm here to help you find the right career path based on your interests and skills.\n"
            "💬 Just tell me what you enjoy doing or what your goals are, and I’ll suggest a career for you.\n"
            "📌 I can also provide the skills you’ll need and real-world job roles!\n"
        )

        if not self.introduced:
            self.introduced = True
            return intro

        if len(user_input.strip()) < 10:
            return "⚠️ Please tell me a bit more about what you enjoy or what kind of work you’d love to do."

        prompt = (
            "You are an expert career advisor. Based on the user's input, suggest ONE ideal career path from the following options:\n"
            "- Frontend Developer\n"
            "- Data Analyst\n"
            "- AI Researcher\n"
            "- Cybersecurity Specialist\n"
            "- UX Designer\n\n"
            "Explain why this field fits the user's interests, what core skills are required, and how they can get started.\n\n"
            f"User: {user_input}"
        )

        return self.model.generate(prompt)
