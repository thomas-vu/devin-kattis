Here's the Python code to solve the problem:

```python
def days_in_month(m):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 28

m = int(input())
print(days_in_month(m))