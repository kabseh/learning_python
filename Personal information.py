fName = input("whats your first name?")
mName = input("whats your middle name?")
lName = input("whats your last name?")
email = input("what\'s your Email")
website = email[email.index("@")+1:]
age = int(input("what\'s your age?").strip())

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
fName = fName.capitalize().strip()
mName = mName.capitalize().strip()
lName = lName.capitalize().strip()
email = email.strip()

print(f"Hello {fName} {mName} {lName} Nice to meet you")
print("your Email is " f"{email}\nYour Websit is {website}\n Wellcome Sir")
print("you Lived for:")
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,}Seconds.")
