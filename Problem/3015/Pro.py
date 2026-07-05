"""this is funct"""
def main():
    """this is code"""
    x = int(input())
    y = int(input())
    price = int(input())
    count_person = int(input())

    if x >= y:
        if count_person < x:
            pay = price*count_person
            print(pay)
        elif count_person >= x:
            pay = ((count_person % x)*price) + ((count_person//x)*(price*y))
            print(pay)
main()
