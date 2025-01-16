import requests
import os
from bs4 import BeautifulSoup


def read_problem_description(problem_id):
    file_path = f"problems/{problem_id}/problem.html"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            # Extract text from problembody div, removing HTML tags
            problem_body = soup.find('div', class_='problembody')
            if problem_body:
                return problem_body.get_text(strip=True)
            return html_content
    except Exception as e:
        print(f"Error reading problem {problem_id}: {e}")
        return None


def prompt_local_model(prompt, api_url="http://localhost:1234/v1/chat/completions"):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 10000
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to LMStudio: {e}")
        return None


def solve_problems():
    with open('problems.txt', 'r') as f:
        problems = [line.strip() for line in f.readlines()]

    for problem_id in problems:
        print(f"\nSolving problem: {problem_id}")
        problem_desc = read_problem_description(problem_id)
        if not problem_desc:
            continue

        prompt = f"""You are solving a programming problem. Here is the problem description:

{problem_desc}

Output ONLY the complete, runnable solution in Python 3, and nothing else."""

        response = prompt_local_model(prompt)
        if response:
            # Create problem directory if it doesn't exist
            problem_dir = f"problems/{problem_id}"
            os.makedirs(problem_dir, exist_ok=True)

            # Clean up the response to ensure it's just code
            code = response.strip()
            if code.startswith("```python\n"):
                code = code[9:]
            elif code.startswith("```\n"):
                code = code[4:]
            if code.endswith("\n```"):
                code = code[:-4]
            elif code.endswith("```"):
                code = code[:-3]
            code = code.strip()

            # Save the solution to main.py
            with open(f"{problem_dir}/main.py", 'w') as f:
                f.write(code)
            print(f"Solution saved to {problem_dir}/main.py")
        else:
            print(f"Failed to get solution for {problem_id}")


if __name__ == "__main__":
    solve_problems()
