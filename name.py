print("=" * 50)

fName = input("whats your first name?")
mName = input("whats your middle name?")
lName = input("whats your last name?")
email = input("what\'s your Email")
website = email[email.index("@")+1:]

fName = fName.capitalize().strip()
mName = mName.capitalize().strip()
lName = lName.capitalize().strip()
email = email.strip()

print(f"Hello {fName} {mName} {lName} Nice to meet you")
print("your Email is " f"{email}\nYour Websit is {website}\n Wellcome Sir")
