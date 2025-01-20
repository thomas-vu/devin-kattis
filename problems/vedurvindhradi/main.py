def wind_level(speed):
    if speed <= 0.2:
        return "Andvari"
    elif speed <= 1.5:
        return "Kul"
    elif speed <= 3.3:
        return "Gola"
    elif speed <= 5.4:
        return "Stinningsgola"
    elif speed <= 7.9:
        return "Kaldi"
    elif speed <= 10.7:
        return "Stinningskaldi"
    elif speed <= 13.8:
        return "Allhvass vindur"
    elif speed <= 17.1:
        return "Hvassvidri"
    elif speed <= 20.7:
        return "Stormur"
    elif speed <= 24.4:
        return "Rok"
    else:
        return "Ofsavedur"

# Sample Input 1
speed = float(input())
print(wind_level(speed))

# Sample Input 2
speed = float(input())
print(wind_level(speed))

# Sample Input 3
speed = float(input())
print(wind_level(speed))