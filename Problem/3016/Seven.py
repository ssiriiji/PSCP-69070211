"""this is Seven"""
def main():
    """this is code"""
    x = int(input())
    list_pattern = [7, 9, 3, 1]
    if not x:
        print(7)
    else:
        print(list_pattern[(x - 1) % 4])
main()
