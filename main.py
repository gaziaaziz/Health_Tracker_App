import csv
import os

print("Welcome to the HealthTrack App!")

# Get and format name
name = input("\nEnter your name: ").capitalize()

# Get and validate age
while True:
    try:
        age = float(input("\nEnter your age: "))
        if age <= 0:
            raise ValueError("Age must be greater than zero.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

# Validate weight
while True:
    try:
        weight_kgs = float(input("\nEnter weight (in kgs): "))
        if weight_kgs <= 0:
            raise ValueError("Weight must be greater than zero.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

# Validate height
while True:
    try:
        height_cms = float(input("\nEnter height (in cms): "))
        if height_cms <= 0:
            raise ValueError("Height must be greater than zero.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

# Calculate BMI
def calc_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)

bmi = round(calc_bmi(weight_kgs, height_cms), 1)
print(f"\nHello {name}, Your BMI is: {bmi}")

# BMI Feedback
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are in the normal range.")
elif 24.9 <= bmi < 29:
    print("You are overweight.")
else:
    print("You are obese.")

# Get health info
print("\nLet's log today's health info.")

# Steps
while True:
    try:
        steps = int(input("How many steps did you walk today? "))
        if steps <= 0:
            raise ValueError("Steps must be greater than zero.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

# Water intake
while True:
    try:
        litres = float(input("How many litres of water did you drink today? "))
        if litres <= 0:
            raise ValueError("Litres must be greater than zero.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

# Sleep hours
while True:
    try:
        hours = float(input("How many hours did you sleep? "))
        if hours <= 0:
            raise ValueError("Sleep hours must be greater than zero.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

# Activity Level
if steps < 3000:
    print("Activity Level: Low Activity")
elif 3000 <= steps < 6999:
    print("Activity Level: Moderate Activity")
else:
    print("Activity Level: High Activity")

# Water Feedback
if litres < 1.5:
    print("Hydration Feedback: Drink more water")
elif 1.5 <= litres < 2.5:
    print("Hydration Feedback: Good hydration")
else:
    print("Hydration Feedback: Excellent!")

# Sleep Feedback
if hours < 6:
    print("Sleep Feedback: Not enough rest")
elif 6 <= hours < 8:
    print("Sleep Feedback: Healthy Sleep")
else:
    print("Sleep Feedback: Oversleeping")

# Health Summary
def health_summary(steps, litres, hours):
    print("\n🟢 Health Summary for today:")
    print(f"- Steps: {steps} steps")
    print(f"- Water: {litres} L")
    print(f"- Sleep: {hours} hrs")

health_summary(steps, litres, hours)

def save_log_to_csv(name, age, bmi, steps, litres, hours):
    file_exists = os.path.isfile("health_log.csv")
    with open("health_log.csv", mode= "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists or os.stat("health_log.csv").st_size == 0:
            writer.writerow(["Name", "Age", "BMI", "Steps", "Water Intake (L)", "Sleep (Hrs)"])
        writer.writerow([name, age, bmi, steps, litres, hours])

save_log_to_csv(name, age, bmi, steps, litres, hours)
print("Your Health Log has been saved!")


# Final Encouragement
if steps >= 5000 and litres >= 2 and hours >= 7:
    print("\n💪 Great job! Well done!")
else:
    print("\n🚀 You're doing good. But there's always room for improvement!")

print("\n“Your body deserves the best. Keep going!” 💚")
