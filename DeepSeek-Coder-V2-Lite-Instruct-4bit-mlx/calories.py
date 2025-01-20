def calculate_calories(fat, protein, sugar, starch, alcohol):
    calories_from_fat = fat * 9 if 'g' in fat else int(fat.replace('%', '')) * 9
    calories_from_protein = protein * 4 if 'g' in protein else int(protein.replace('%', '')) * 4
    calories_from_sugar = sugar * 4 if 'g' in sugar else int(sugar.replace('%', '')) * 4
    calories_from_starch = starch * 4 if 'g' in starch else int(starch.replace('%', '')) * 4
    calories_from_alcohol = alcohol * 7 if 'g' in alcohol else int(alcohol.replace('%', '')) * 7
    
    total_calories = (calories_from_fat + calories_from_protein + calories_from_sugar +
                      calories_from_starch + calories_from_alcohol)
    percent_calories_from_fat = (calories_from_fat / total_calories) * 100
    return round(percent_calories_from_fat)

def main():
    while True:
        inputs = []
        while True:
            line = input().strip()
            if line == '-':
                break
            inputs.append(line)
        
        for item in inputs:
            fat, protein, sugar, starch, alcohol = map(str, item.split())
            print(calculate_calories(fat, protein, sugar, starch, alcohol))
        break  # Assuming only one test case for simplicity

if __name__ == "__main__":
    main()