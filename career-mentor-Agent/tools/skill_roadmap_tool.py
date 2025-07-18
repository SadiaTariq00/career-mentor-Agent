def get_career_roadmap(field: str) -> str:
    roadmaps = {
        "Frontend Developer": "HTML, CSS, JavaScript, Git, React, Responsive Design, Web Performance Optimization",
        "Data Analyst": "Python, SQL, Excel, Pandas, Data Cleaning, Data Visualization (Matplotlib/Seaborn), Tableau/Power BI",
        "AI Researcher": "Python, Deep Learning, TensorFlow, PyTorch, Research Papers, Model Evaluation, Experimentation Frameworks",
        "Cybersecurity Specialist": "Networking Basics, Linux, Cryptography, Firewalls, Penetration Testing, SIEM Tools, Security+ Certification",
        "UX Designer": "Design Thinking, Wireframing, Prototyping, Figma/Sketch, User Research, Usability Testing, Accessibility Guidelines"
    }
    return roadmaps.get(field, "🚫 No roadmap found for this field.")
