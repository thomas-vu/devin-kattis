class Window:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains_point(self, px, py):
        return self.x <= px < self.x + self.w and self.y <= py < self.y + self.h

    def move(self, dx, dy):
        if abs(dx) > 0:
            self.x = min(max(self.x + dx, 0), x_max - self.w)
        if abs(dy) > 0:
            self.y = min(max(self.y + dy, 0), y_max - self.h)
        return abs(dx) if dx != 0 else abs(dy)

    def resize(self, w, h):
        if self.x + w <= x_max and self.y + h <= y_max:
            self.w = w
            self.h = h
            return True
        return False

    def __str__(self):
        return f"{self.x} {self.y} {self.w} {self.h}"

windows = []
x_max, y_max = map(int, input().split())
command_number = 0
errors = []

while True:
    try:
        command_number += 1
        line = input().split()
        cmd = line[0]
        if cmd == 'OPEN':
            x, y, w, h = map(int, line[1:])
            if any(w_win.contains_point(x, y) for w_win in windows):
                errors.append((command_number, cmd, "window does not fit"))
            else:
                windows.append(Window(x, y, w, h))
        elif cmd == 'CLOSE':
            x, y = map(int, line[1:])
            found = False
            for w_win in windows:
                if w_win.contains_point(x, y):
                    windows.remove(w_win)
                    found = True
                    break
            if not found:
                errors.append((command_number, cmd, "no window at given position"))
        elif cmd == 'RESIZE':
            x, y, w, h = map(int, line[1:])
            found = False
            for w_win in windows:
                if w_win.contains_point(x, y):
                    found = True
                    if not w_win.resize(w, h):
                        errors.append((command_number, cmd, "window does not fit"))
                    break
            if not found:
                errors.append((command_number, cmd, "no window at given position"))
        elif cmd == 'MOVE':
            x, y, dx, dy = map(int, line[1:])
            found = False
            for w_win in windows:
                if w_win.contains_point(x, y):
                    found = True
                    moved = w_win.move(dx, dy)
                    if moved != abs(dx + dy):
                        errors.append((command_number, cmd, f"moved {moved} instead of {abs(dx + dy)}"))
                    break
            if not found:
                errors.append((command_number, cmd, "no window at given position"))
    except EOFError:
        break

print(f"{len(windows)} window(s):")
for w_win in windows:
    print(w_win)