import requests

# 🔑 Paste your OpenRouter API key here
API_KEY = "YOUR_API_KEY"


# 🔹 Function to call LLM
def call_llm(prompt):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "Smart Task Agent"
            },
            json={
                "model": "openrouter/free",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an intelligent AI agent that plans tasks and executes them step by step."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        data = response.json()

        if "choices" not in data:
            print("Error:", data)
            return "Error in response"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"

# 🔹 Planner: Breaks task into structured steps
def planner(user_input):
    prompt = f"""
    You are an AI agent.

    Break the given task into minimal, clear, and logical steps that can be executed sequentially.

    Task: {user_input}

    Rules:
    - Keep steps concise
    - Each step should perform a real action
    - Avoid repetition

    Format:
    1. Step one
    2. Step two
    3. Step three
    """

    return call_llm(prompt)


# 🔹 Executor: Executes each step cleanly
def executor(steps):
    results = []

    for step in steps.split("\n"):
        step = step.strip()

        # Skip invalid lines
        if not step or not step[0].isdigit():
            continue

        print(f"\n🔹 {step}")

        result = call_llm(f"""
        Execute the following step and return only the final result.
        Do NOT repeat the step.
        Be concise and clear.

        Step: {step}
        """)

        results.append(result.strip())

    return "\n\n".join(results)


# 🔹 Main program
if __name__ == "__main__":
    print("=== 🚀 Smart Task Agent ===")

    user_input = input("\nEnter your task: ")

    print("\n🧠 Planning...\n")
    steps = planner(user_input)
    print(steps)

    print("\n⚙️ Executing...\n")
    output = executor(steps)

    print("\n📌 Task Completed Successfully\n")
    print("✅ Final Output:\n")
    print(output)