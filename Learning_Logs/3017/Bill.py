"""this is funct"""
def main():
    """this is code"""
    money = int(input())
    if money < 500:
        key = 50
        key2 = key+money
        result = key2+(key2*7/100)
        print(f"{result:.2f}")
    elif money > 10000:
        key = 1000
        key2 = key+money
        result = key2+(key2*7/100)
        print(f"{result:.2f}")
    elif 500 <= money <= 10000:
        key = money*(10/100)
        key2 = key+money
        result = key2+(key2*7/100)
        print(f"{result:.2f}")
main()
