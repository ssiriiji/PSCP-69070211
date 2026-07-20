"""this is [LEARNING LOGS] หาร 10"""
def main():
    """this is function"""
    N = int(input())
    count = ""
    for i in range(N, -1, -1):
        if not i % 10:
            if not count:
                count += str(i)
            else:
                count += str(" " + str(i))
    print(count)
main()
