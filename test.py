#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


def run_kattis_test(problem_dir):
    """Run 'kattis test' for a given problem directory."""
    print(f"\nTesting problem: {problem_dir}")
    print("=" * 50)

    try:
        result = subprocess.run(
            ['kattis', 'test'],
            cwd=str(problem_dir),
            capture_output=True,
            text=True,
            timeout=5
        )

        print(result.stdout)
        if result.stderr:
            print("Errors:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)

        # Check for various error conditions in output
        has_error = (
            result.returncode != 0 or
            'Traceback' in result.stderr or
            'Error:' in result.stderr or
            'Wrong Answer' in result.stdout or
            'Runtime Error' in result.stdout or
            'Time Limit Exceeded' in result.stdout
        )

        if has_error:
            return False

        # Count number of test cases and correct results
        test_cases = result.stdout.count('Running test case:')
        correct_results = result.stdout.count('Correct')

        # All test cases must pass
        return test_cases > 0 and test_cases == correct_results

    except subprocess.TimeoutExpired:
        print(f"{RED}Error: Test timed out after 5 seconds{RESET}", file=sys.stderr)
        return False
    except subprocess.SubprocessError as e:
        print(f"Error running tests for {problem_dir}: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error for {problem_dir}: {e}", file=sys.stderr)
        return False


def main():
    # Get the script's directory and problems directory
    script_dir = Path(__file__).parent.absolute()
    problems_file = script_dir / 'problems.txt'
    problems_dir = script_dir / 'problems'

    try:
        # Read problems
        with open(problems_file, 'r') as f:
            problems = [line.strip() for line in f if line.strip()]

        print(f"Running tests:")
        for prob in problems:
            print(f"- {prob}")
        print("\nStarting tests...")

        # Track results
        results = []

        # Run tests for each problem
        for problem in problems:
            problem_dir = problems_dir / problem
            if not problem_dir.is_dir():
                print(f"\nSkipping {problem}: Directory not found")
                results.append((problem, False))
                continue

            success = run_kattis_test(problem_dir)
            results.append((problem, success))

        # Print summary
        print("\nTest Summary:")
        print("=" * 50)
        passed = sum(1 for _, success in results if success)
        total = len(results)
        print(
            f"Passed: {GREEN if passed == total else RED}{passed}/{total}{RESET}")

        for problem, success in results:
            status = f"{GREEN}✓ PASS{RESET}" if success else f"{RED}✗ FAIL{RESET}"
            print(f"{status}: {problem}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
