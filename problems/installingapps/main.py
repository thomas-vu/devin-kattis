import sys
from collections import deque

def main():
    # Read the number of apps and available disk space
    n, c = map(int, sys.stdin.readline().split())
    
    # Read the download size and storage size for each app
    apps = []
    for i in range(n):
        d, s = map(int, sys.stdin.readline().split())
        apps.append((d, s, i + 1))
    
    # Sort the apps by the maximum required disk space (max(d, s))
    apps.sort(key=lambda x: max(x[0], x[1]))
    
    # Use a deque to simulate the installation process
    queue = deque()
    installed_apps = []
    
    for app in apps:
        d, s, idx = app
        if not queue or (queue[-1] < max(d, s)):
            queue.append(max(d, s))
            installed_apps.append(idx)
        elif queue[-1] == max(d, s):
            continue  # Skip this app as it cannot be installed now
    
    print(len(installed_apps))
    if installed_apps:
        print(' '.join(map(str, installed_apps)))

if __name__ == "__main__":
    main()