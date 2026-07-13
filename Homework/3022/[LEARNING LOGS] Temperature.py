"""this is temp"""
def main():
    """this is code"""
    temp = float(input())
    unit_from = input()
    unit_to = input()

    if unit_from == "C":
        set_c = temp
    elif unit_from == "F":
        set_c = (temp - 32) * 5/9
    elif unit_from == "K":
        set_c = temp - 273.15
    elif unit_from == "R":
        set_c = temp*5/9 - 273.15
    else:
        set_c = ""

    if unit_to == "C":
        final_temp = set_c
        print(f"{final_temp:.2f}")
    elif unit_to == "F":
        final_temp = (set_c * 9/5)+32
        print(f"{final_temp:.2f}")
    elif unit_to == "K":
        final_temp = set_c + 273.15
        print(f"{final_temp:.2f}")
    elif unit_to == "R":
        final_temp = (set_c + 273.15) * 9/5
        print(f"{final_temp:.2f}")
main()
