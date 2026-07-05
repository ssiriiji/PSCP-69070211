"""this is Safe Password"""
def main():
    """this is code"""
    char = input()
    number = input()

    password = "H4567"

    if char == password[0] and number == password[1:]:
        print("safe unlocked")
    elif char == password[0]:
        print("safe locked - change digit")
    elif number == password[1:]:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
