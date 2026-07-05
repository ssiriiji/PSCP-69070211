"""this is EuclideanDistance2D"""
import math as m

def main():
    """this is code"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())

    distance = m.sqrt((q1-p1)**2 + (q2-p2)**2)
    print(distance)
main()
