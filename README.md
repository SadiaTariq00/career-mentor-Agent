# 🎓 Career Mentor Agent (Chainlit + Gemini)

An AI-powered career guidance system that helps users explore career paths, learn required skills, and discover job roles — built with a multi-agent architecture using Chainlit and Google Gemini.

---

## 🚀 Overview

Career planning can feel overwhelming. This smart assistant simplifies it by understanding what you're passionate about and recommending:
- A suitable **career path**
- The required **skill roadmap**
- Real-world **job roles**

All in a conversational format — powered by Gemini API.

---

## 🧠 Key Features

- 🤖 Conversational agent built with Chainlit
- 🎯 Suggests careers based on user input
- 📘 Returns a custom skill roadmap for the field
- 💼 Lists job roles related to the selected career
- 🔁 Handoff logic between agents for modular design
- ⚙️ Powered by Google Gemini via `google-generativeai`

---

## 🧱 Architecture

### 🔹 Agents

| Agent            | Responsibility                                |
|------------------|-----------------------------------------------|
| `CareerAgent`    | Suggests a career based on interests          |
| `SkillAgent`     | Returns required skills (roadmap)             |
| `JobAgent`       | Returns real-world job titles                 |

### 🔧 Tools

| Tool Function           | Description                                         |
|-------------------------|-----------------------------------------------------|
| `get_career_roadmap()`  | Returns a list of skills needed for the career      |
| `get_job_roles()`       | Returns job titles based on the career field        |

---

## 🛠️ Setup Instructions

### 1️⃣ Prepare Your Project Folder

Place all project files in a folder named:

Ensure your structure looks like this:

career-mentor-agent/
├── main.py
├── .env
├── requirements.txt
├── agents/
│ ├── career_agent.py
│ ├── skill_agent.py
│ └── job_agent.py
├── tools/
│ ├── skill_roadmap_tool.py
│ └── job_roles_tool.py
├── model/
│ └── gemini_model.py



2. Create and Activate Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

3. Create .env File
Inside the project root, create a .env file and add your Gemini API key:
GEMINI_API_KEY=your_gemini_api_key_here

4. Run the App
Start your Chainlit career bot with:
chainlit run main.py

 Author
Sadia Tariq

🛠️ Clone the Repository (If using GitHub)

```bash
git clone https://github.com/SadiaTariq00/career-mentor-Agent.git
cd career-mentor-agent
