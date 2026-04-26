from utils import calculate_mpg

distance = float(input("Enter distance (miles): "))
fuel = float(input("Enter fuel (gallons): "))

mpg = calculate_mpg(distance, fuel)

# print("MPG:", mpg)

print(f"Final MPG: {mpg:.2f} miles/gallon")

