import requests
from bs4 import BeautifulSoup


def scrape_problem(problem_id):
    # URL of the problem
    url = f'https://open.kattis.com/problems/{problem_id}'

    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the problembody div
        problem_body = soup.find('div', class_='problembody')

        if problem_body:
            # Save the content to a file
            with open(f'problems/{problem_id}/problem.html', 'w', encoding='utf-8') as f:
                f.write(str(problem_body))
            print(f"Successfully saved problem content for {problem_id}")
            return True
        else:
            print(f"Could not find problem body content for {problem_id}")
            return False
    except Exception as e:
        print(f"Error processing {problem_id}: {str(e)}")
        return False


# Read all problems from problems.txt
with open('problems.txt', 'r') as f:
    problems = [line.strip() for line in f.readlines()]

# Process each problem
for problem_id in problems:
    scrape_problem(problem_id)
