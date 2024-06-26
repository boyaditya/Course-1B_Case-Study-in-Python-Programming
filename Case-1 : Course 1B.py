def calculate_mileage():
    total_miles = 0.0
    total_gallons = 0.0

    while True:
        gallons_used = float(input("Enter the gallons used (-1 to end): "))
        if gallons_used == -1:
            break

        miles_driven = float(input("Enter the miles driven: "))

        if gallons_used != 0:  # To avoid division by zero
            mpg = miles_driven / gallons_used
            print(f"The miles/gallon for this tank was {mpg:.6f}")
        else:
            print("Gallons used cannot be zero.")

        total_miles += miles_driven
        total_gallons += gallons_used

    if total_gallons != 0:
        overall_mpg = total_miles / total_gallons
        print(f"The overall average miles/gallon was {overall_mpg:.6f}")
    else:
        print("No gallons were used.")

calculate_mileage()
