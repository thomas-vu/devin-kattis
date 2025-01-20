import sys

def CheckPassword(pwd1, pwd2):
    if len(pwd1) != len(pwd2):
        return False
    for i in range(len(pwd1)):
        if pwd1[i] != pwd2[i]:
            return False
    return True

def main():
    for _ in range(2500):
        pwd = sys.stdin.readline().strip()
        if CheckPassword(pwd, "Hunter2"):
            print("ACCESS GRANTED")
            return
        else:
            time_taken = int(sys.stdin.readline().strip().split()[-1])
            print("ACCESS DENIED ({0} ms)".format(time_taken))

if __name__ == "__main__":
    main()