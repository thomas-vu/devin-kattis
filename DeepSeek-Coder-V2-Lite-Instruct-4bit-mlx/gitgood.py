def main():
    N = int(input())
    commands = [input().strip() for _ in range(N)]
    
    file_paths = []
    current_dir = ""
    
    for command in commands:
        if command == "cd ..":
            index = current_dir.rfind("/")
            if index != -1:
                current_dir = current_dir[:index]
        elif command.startswith("cd"):
            dir_name = command[3:]
            if current_dir:
                current_dir += "/" + dir_name
            else:
                current_dir = dir_name
        elif command.startswith("nano"):
            file_path = current_dir + "/" + command[5:]
            if file_path not in file_paths:
                file_paths.append(file_path)
    
    file_paths.sort()
    for file_path in file_paths:
        print(f"git add {file_path}")
    print("git commit")
    print("git push")

if __name__ == "__main__":
    main()