weather = input("enter the weather (sunny, rainy, cold): ").lower()
if weather == "sunny":
    print("Wear sunglasses")
elif weather == "rainy":
    print("take an umbrella")
elif weather == "cold":
    print("wear a jacket")
else:
    print("I don't know that weather type.")
