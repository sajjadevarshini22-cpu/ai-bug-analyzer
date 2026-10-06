# 🐞 AI Bug Analyzer

An AI-powered QA tool that analyzes software bug reports and generates structured defect analysis using Google Gemini API.

## 🚀 Overview

AI Bug Analyzer helps QA engineers analyze bug reports automatically.

The application accepts a bug report as input and uses an LLM to generate:

- Bug Summary
- Possible Root Cause
- Severity
- Priority
- Bug Category
- Affected Module
- Steps to Reproduce
- Expected Result
- Actual Result
- Suggested Fix
- Recommended Test Cases

The analysis can also be downloaded as an Excel report.

---

## ✨ Features

- 🤖 AI-powered bug analysis
- 🔍 Possible root-cause analysis
- 📊 Severity classification
- 🚨 Priority classification
- 🏷️ Bug category classification
- 📦 Affected module identification
- 🔁 Steps-to-reproduce generation
- 🧪 Recommended regression test cases
- ✅ AI response validation
- 📥 Excel report generation
- ⚠️ Error handling
- 🔐 Secure API-key management using `.env`
- 🖥️ Streamlit web interface

---

## 🏗️ Architecture

```text
Bug Report
    ↓
Streamlit UI
    ↓
Prompt Engineering
    ↓
Google Gemini API
    ↓
Structured JSON
    ↓
Validation Layer
    ↓
AI Bug Analysis
    ↓
Streamlit Display
    ↓
Excel Export

Export

🛠️ Tech Stack
Technology	Purpose
Python	Application development
Google Gemini API	AI-powered analysis
google-genai	Gemini API integration
Streamlit	Web UI
JSON	Structured AI output
OpenPyXL	Excel generation
python-dotenv	Environment variable management
Git	Version control
GitHub	Source code hosting


📁 Project Structure
ai-bug-analyzer/
│
├── src/
│   ├── app.py
│   ├── ai_analyzer.py
│   ├── prompt.py
│   ├── validator.py
│   └── excel_generator.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-bug-analyzer.git

2. Navigate to the project
cd ai-bug-analyzer

3. Create virtual environment
python -m venv venv

4. Activate virtual environment
Windows:
venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

🔑 Environment Setup
Create a .env file in the project root:
GEMINI_API_KEY=your_api_key_here

Never commit the .env file to GitHub.
▶️ Run the Application
streamlit run src/app.py

The application will open in your browser.
🧪 Example Bug Report
Login button is not working when I enter a valid username and password.
The user remains on the login page and no error message is displayed.

The AI analyzes the defect and generates structured QA information including severity, priority, root cause, expected/actual results, and recommended test cases.
📊 Excel Export
The generated analysis can be downloaded as:
ai_bug_analysis.xlsx

The Excel report contains:
- Bug Summary
- Possible Root Cause
- Severity
- Priority
- Bug Category
- Affected Module
- Steps to Reproduce
- Expected Result
- Actual Result
- Suggested Fix
- Recommended Test Cases
🧠 QA Concepts Demonstrated
This project demonstrates practical knowledge of:
- Defect Reporting
- Severity vs Priority
- Bug Classification
- Root Cause Analysis
- Functional Testing
- Regression Testing
- Test Case Design
- API Integration
- Validation
- Error Handling
- AI-assisted Testing
🤖 AI Concepts Demonstrated
- LLM API integration
- Prompt Engineering
- Structured JSON generation
- AI output validation
- AI-assisted defect analysis
- AI-generated test recommendations
🧪 Testing Performed
The application was tested with:
- Functional bugs
- Empty bug reports
- UI bugs
- Performance bugs
- Security bugs
- Excel export
- Invalid AI responses
- API errors
All primary functional test cases passed successfully.
🔮 Future Enhancements
Possible future improvements:
- Jira integration
- Automatic Jira bug creation
- Screenshot-based bug analysis
- Browser console-log analysis
- API response analysis
- Duplicate bug detection
- Bug similarity detection
- AI-generated Jira tickets
- RAG-based historical bug analysis
- Integration with automated testing frameworks
👩‍💻 Author
Sajja Devarshini
QA Engineer | Manual Testing | Playwright | API Testing | AI-assisted QA