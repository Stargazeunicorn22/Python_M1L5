while True:
    x = input("Enter the current temperature in °F: ")
    try:
        temperature = float(x)
        break 
    except ValueError:
        print("That is not a temperature... try again and input the right temperature.")

if temperature >= 80:
    print("It is warm enough! You can safely wear light and soft clothes.")
    print("But make sure to put sunscreen!")
elif temperature >= 70:
    print("It is mild. Consider light layers like a long-sleeve shirt.")
else:
    print("It is super duper cold! Stick to your jacket to avoid catching a cold.")
