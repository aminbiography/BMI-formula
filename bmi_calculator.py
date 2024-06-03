def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()
