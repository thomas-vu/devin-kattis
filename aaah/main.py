# Read Jon Marius's "aaah"
jon_aaah = input()

# Read doctor's required "aaah"
doctor_aaah = input()

# Compare lengths - Jon can go if his "aaah" is at least as long as the doctor's requirement
print("go" if len(jon_aaah) >= len(doctor_aaah) else "no")
