FOLLLOW THESE STEPS TO RUN THIS PROJECT IN YOUR DEVICE :



    🚀 Auto BugFix — AI Powered Python Code Fixer

An AI-powered system that:

Detects Python issues using Pylint

Retrieves similar past fixes using FAISS (RAG)

Generates fixes using Groq LLM

Validates fixes using Pytest





📌 Project Architecture------


User Code
   ↓
Pylint Detector
   ↓
Retriever (FAISS RAG)
   ↓
Groq LLM Generator
   ↓
Validator (Pytest)



🛠 Tech Stack---

Python 3.10+

Pylint

Pytest

FAISS

Groq API

python-dotenv



🧑‍💻 How To Run This Project------

Follow these steps carefully.

✅ Step 1 — Clone the Repository
git clone https://github.com/arjunishere2107/auto_bugfix.git
cd auto_bugfix
✅ Step 2 — Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

Mac/Linux:

python3 -m venv venv
source venv/bin/activate
✅ Step 3 — Install Dependencies
pip install -r requirements.txt
✅ Step 4 — Setup Environment Variables

Create a file in root directory named:

.env

Add your Groq API key:

GROQ_API_KEY=your_api_key_here

⚠ Important:

Do NOT add quotes

Do NOT push .env to GitHub

✅ Step 5 — Run the Project
python src/main.py
✅ Step 6 — Run Tests (Optional)
pytest
📂 Project Structure
auto_bugfix/
│
├── src/
│   ├── main.py
│   ├── detector.py
│   ├── generator.py
│   ├── retriever.py
│   ├── validator.py
│   ├── storage.py
│
├── sample_code/
├── data/
├── requirements.txt
├── .gitignore
├── README.md


🔐 Security Notes

API keys are stored using environment variables

.env file is excluded via .gitignore

No secrets are hardcoded

👨‍💻 Author

Arjun Bhardwaj
B.Tech CSE (AI)

💡 Future Improvements

Add Web UI

Dockerize the project

Add CI/CD pipeline

Improve RAG retrieval accuracy

🔥 Extra Professional Touch (Recommended)

Also create a file called:

.env.example

Inside it:

GROQ_API_KEY=your_api_key_here


RUN COMMAND - python src/main.py 
and if using after 28 march 2026 use this - 

