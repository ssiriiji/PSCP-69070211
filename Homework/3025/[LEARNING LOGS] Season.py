"""this is [LEARNING LOGS] Season"""
def main():
    """this is code"""
    month = int(input())
    date = int(input())

    winter = [1, 2, 3]
    spring = [4, 5, 6]
    summer = [7, 8, 9]
    fall = [10, 11, 12]

    if month in winter:
        set_month = "winter"
    elif month in spring:
        set_month = "spring"
    elif month in summer:
        set_month = "summer"
    elif month in fall:
        set_month = "fall"
    else:
        set_month = ""

    seasons_order = ["winter", "spring", "summer", "fall"]

    if not month % 3 and date >= 21:
        idx = seasons_order.index(set_month)
        season = seasons_order[((idx+1)%4)]
        print(season)
    else:
        print(set_month)
main()
