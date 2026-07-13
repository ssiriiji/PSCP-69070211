"""this is [LEARNING LOGS] SurprisingVote"""
def main():
    """this is code"""
    sum_input = float(input())
    max_input = float(input())

    if sum_input - max_input <= max_input:
        min_set = 0
    else:
        min_set = (sum_input-max_input) - max_input
    if max_input - min_set > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
