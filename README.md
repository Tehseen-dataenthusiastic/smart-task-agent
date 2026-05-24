# 🚀 Smart Task Agent

## Overview
Smart Task Agent is a simple agentic system that converts high-level user goals into executable steps and completes them.

Instead of just responding like a chatbot, the system:
- Understands the task
- Breaks it into logical steps
- Executes each step
- Produces a final result

---

## 🔍 What it does

Input:
> "Explain blockchain and write a LinkedIn post"

Output:
- Step-by-step plan
- Executed results (explanation + post)

---

## ⚙️ How it works

The system follows a basic agent loop:

### 1. Planner
- Takes a user goal
- Breaks it into structured steps

### 2. Executor
- Processes each step
- Generates outputs for each action

### 3. Final Output
- Combines all results into a meaningful response

---

## 🧠 Key Idea

Most AI tools are **assistive** (they respond to prompts).

This project explores a shift toward **agentic systems** that:
> Take a goal → plan → execute → complete tasks

---

## 🛠 Tech Stack

- Python
- LLM API (OpenRouter / similar)
- Requests library

---

## ▶️ How to run

1. Install dependencies:

2. Run the program:

3. Enter a task:

---

## 💡 Example Use Cases

- Content generation (emails, posts)
- Summarization
- Explanation tasks
- Multi-step workflows

---

## ⚠️ Note

API keys are not included in this repository for security reasons.

---

## 📌 Future Improvements

- Add memory between steps
- Improve planning accuracy
- Add UI (React frontend)
- Integrate real tools (APIs, file handling)

---

## 👩‍💻 Author

Tehseen Shaikh
