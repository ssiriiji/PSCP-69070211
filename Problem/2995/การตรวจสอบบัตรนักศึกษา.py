"""this is funct"""
def main():
    """this is code"""
    key = input()
    len_key = len(key)

    if len_key == 8:
        if key[2] == "1" and key[3] == "6":
            print("yes")
        else:
            print("no")
main()
