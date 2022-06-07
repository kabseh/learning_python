from asyncore import write


print("Hello")

fName = input("whats your first name?")
mName = input("whats your middle name?")
lName = input("whats your last name?")
age = int(input("what\'s your age?").strip())

unit = input(
    'pleas choose time unit: Monthes, Weeks, Days, Hours, Minutes, Seconds  ').strip().lower()


months = int(age) * 12
weeks = months * 4
days = int(age) * 365
hours = int(days) * 24
minutes = int(hours) * 60
seconds = int(minutes) * 60

fName = fName.capitalize().strip()
mName = mName.capitalize().strip()
lName = lName.capitalize().strip()

print(f"Hello {fName} {mName} {lName} Nice to meet you")

if unit == 'months' or unit == 'mo':
    print("You choosed the unit Months.")
    print(f"You lived for{months:,}Months.")

elif unit == 'weeks' or unit == 'w':
    print("You choosed the unit weeks")
    print(f"You lived for{weeks:,}Weeks.")

elif unit == 'Days' or unit == 'd':
    print("You choosed the unit Days")
    print(f"You lived for {days:,}Days.")

elif unit == 'hours' or unit == 'h':
    print("You choosed the unit hours")
    print(f"You lived for {hours:,}Hours.")

elif unit == 'minutes' or unit == 'mi':
    print("You choosed the unit minutes")
    print(f"You lived for {minutes:,}minutes.")

elif unit == 'seconds' or unit == 's':
    print("You choosed the unit seconds")
    print(f"You lived for {seconds:,}seconds.")
