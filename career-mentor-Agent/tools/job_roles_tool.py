def get_job_roles(field: str) -> str:
    roles = {
        "Frontend Developer": "React Developer, Vue.js Developer, UI Engineer, Web Designer",
        "Data Analyst": "Business Analyst, Reporting Analyst, Marketing Data Analyst, Risk Analyst",
        "AI Researcher": "Machine Learning Scientist, Deep Learning Engineer, AI Research Scientist, Cognitive Computing Expert",
        "Cybersecurity Specialist": "Security Analyst, Ethical Hacker, SOC Analyst, Cybersecurity Consultant",
        "UX Designer": "Interaction Designer, UX Researcher, Product Designer, UI/UX Specialist"
    }
    return roles.get(field, "🚫 No job roles found for this field.")
