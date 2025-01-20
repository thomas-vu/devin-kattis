def main():
    t, b = map(int, input().split())
    package_versions = {}
    for _ in range(t):
        name, version = input().split()
        package_versions[name] = int(version)
    
    store_packages = [{} for _ in range(b)]
    package_counts = list(map(int, input().split()))
    
    for i in range(b):
        for _ in range(package_counts[i]):
            name, version = input().split()
            store_packages[i][name] = int(version)
    
    for i in range(b):
        steps = 0
        for package, version in store_packages[i].items():
            if package_versions[package] != version:
                steps += 1
        print(steps)

if __name__ == "__main__":
    main()