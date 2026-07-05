"""this is funct"""
import math as m

def main():
    """this is code"""
    RA = int(input())
    RB = int(input())
    whoWin_input = input()

    EA = 1/(1+(m.pow(10, (RB-RA)/400)))
    EB = 1/(1+(m.pow(10, (RA-RB)/400)))

    if whoWin_input == "A":
        print(f"{EA:.2f}")
    elif whoWin_input == "B":
        print(f"{EB:.2f}")
main()
