# START

minutes = int(input("How many minutes did the meal take? "))
price = float(input("How much did it cost? "))

is_quick_service = minutes < 15
is_expensive = price > 100

if is_quick_service and not is_expensive:
    print("recommended")
else:
    print("not recommended")

# STOP