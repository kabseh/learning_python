tries = 4
mainPassword = "12345"

inputPassword = input("Write yor password please : ")
while inputPassword != mainPassword:
    tries -= 1
    print(f"wrong password, {'Last' if tries == 0 else tries } Chance left ")
    inputPassword = input("Write yor password please ")
    if tries == 0:
        print("All tries is finished.")
        break
        print("will not print")
else:
    print("Wellcome")
