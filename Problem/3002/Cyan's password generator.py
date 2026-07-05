"""this is code"""
def main():
    """this is code"""
    name = input()
    surname = input()
    ages = input()

    if len(name) >= 5 and len(surname) >= 5:
        password = name[0:2] + surname[-1] + ages[-1]
        print(password)
    else:
        password = name[0] + ages + surname[-1]
        print(password)
main()
