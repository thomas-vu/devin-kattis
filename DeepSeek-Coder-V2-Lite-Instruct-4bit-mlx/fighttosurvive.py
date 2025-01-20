def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    S = int(data[0])
    m = int(data[1])
    survivors_healths = list(map(int, data[2:S+2]))
    e = int(data[S+2])
    events = [input().strip() for _ in range(e)]
    
    survivors = sorted([{"health": h, "in_battle": False} for h in survivors_healths], key=lambda x: (-x["health"], x["in_battle"]))
    medical_ward = []
    medicine_prepared = False
    
    for i, event in enumerate(events):
        if event == "ATTACK":
            if survivors and not medicine_prepared:
                z = zombies.pop(0)
                s = survivors.pop(0)
                while s["in_battle"]:
                    s = survivors.pop(0)
                s["health"] -= z["health"]
                z["health"] -= s["health"]
                if z["health"] <= 0:
                    survivors.append({"health": 0, "in_battle": False})
                elif s["health"] <= 0:
                    medical_ward.append(s)
                    survivors.remove(s)
                else:
                    survivors.insert(0, s)
                if not zombies and not survivors:
                    print("success")
                    return
            elif medicine_prepared:
                if medical_ward:
                    healed_survivor = medical_ward.pop(0)
                    healed_survivor["health"] = int(healed_survivor["health"] / 2)
                    survivors.append(healed_survivor)
                medicine_prepared = False
        elif event.startswith("APPROACH"):
            z = {"health": int(event.split()[1]), "in_battle": False}
            zombies.append(z)
        elif event == "ATTACK":
            if not medicine_prepared:
                survivors = sorted([{"health": h, "in_battle": False} for h in survivors_healths], key=lambda x: (-x["health"], x["in_battle"]))
            medicine_prepared = True if (i + 1) % m == 0 else False
    
    print("overrun")

if __name__ == "__main__":
    main()