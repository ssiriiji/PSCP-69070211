"""this is function"""
def main():
    """this is code"""
    c1 = input().strip().capitalize()
    c2 = input().strip().capitalize()

    primary = ["Blue", "Red", "Yellow"]

    mix = {"RedYellow":"Orange", "BlueRed":"Violet", "BlueYellow":"Green"}

    if c1 in primary and c2 in primary:
        if c1 == c2:
            print(c1)
        else:
            key = "".join(sorted([c1, c2]))
            if key in mix:
                print(mix[key])
            else:
                print("Error")
    else:
        print("Error")
main()
