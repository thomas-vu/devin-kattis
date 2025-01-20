def astrological_sign(day, month):
    if month == 'May' and day >= 21 or month == 'Jun' and day <= 20:
        return 'Gemini'
    elif month == 'Jun' and day >= 21 or month == 'Jul' and day <= 22:
        return 'Cancer'
    elif month == 'Jul' and day >= 23 or month == 'Aug' and day <= 22:
        return 'Leo'
    elif month == 'Aug' and day >= 23 or month == 'Sep' and day <= 22:
        return 'Virgo'
    elif month == 'Sep' and day >= 23 or month == 'Oct' and day <= 22:
        return 'Libra'
    elif month == 'Oct' and day >= 23 or month == 'Nov' and day <= 21:
        return 'Scorpio'
    elif month == 'Nov' and day >= 22 or month == 'Dec' and day <= 21:
        return 'Sagittarius'
    elif month == 'Dec' and day >= 22 or month == 'Jan' and day <= 19:
        return 'Capricorn'
    elif month == 'Jan' and day >= 20 or month == 'Feb' and day <= 18:
        return 'Aquarius'
    elif month == 'Feb' and day >= 19 or month == 'Mar' and day <= 20:
        return 'Pisces'
    elif month == 'Mar' and day >= 21 or month == 'Apr' and day <= 19:
        return 'Aries'
    elif month == 'Apr' and day >= 20 or month == 'May' and day <= 20:
        return 'Taurus'

t = int(input())
for _ in range(t):
    day, month = input().split()
    day = int(day)
    print(astrological_sign(day, month))