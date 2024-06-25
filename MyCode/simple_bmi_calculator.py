# simple_bmi_calculator.py
def calculate_bmi(weight, height):
    return weight / (height ** 2)

if __name__ == "__main__":
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi:.2f}")
