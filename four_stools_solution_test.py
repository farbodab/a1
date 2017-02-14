from tour import *
import sys
sys.setrecursionlimit(2000)

def four_stools_solution_test(model, cheese_amount, start_stool, end_stool, inter_stool1, inter_stool2, i_value):
    """
    Function used to find the optimal i value in the four-stool solution. Use this function to test various
    i values and approximate.

    @param model: TOAHModel
    @param cheese_amount: int
    @param start_stool: int
    @param end_stool: int
    @param inter_stool1: int
    @param inter_stool2: int
    """
    x = cheese_amount
    y1 = x - i_value
    y2 = x - y1
    if cheese_amount == 1:
        model.move(start_stool, end_stool)
    elif cheese_amount == 2:
        three_stools_solution(model, y1, start_stool, inter_stool2, inter_stool1)
        three_stools_solution(model, y2, start_stool, end_stool, inter_stool1)
        three_stools_solution(model, y1, inter_stool2, end_stool, inter_stool1)
    else:
        four_stools_solution(model, y1, start_stool, inter_stool1, inter_stool2, end_stool)
        three_stools_solution(model, y2, start_stool, end_stool, inter_stool2)
        four_stools_solution(model, y1, inter_stool1, end_stool, start_stool, inter_stool2)

"""if __name__ == '__main__':
    for i in range(0, 16):
        print("n = {}".format(i) )
        x = i - 1
        while x >= 1:
            print("x = {}".format(x))
            A = TOAHModel(4)
            A.fill_first_stool(i)
            four_stools_solution_test(A, i, 0, 3, 1, 2, x)
            print(A.moves)
            x = x-1
"""
if __name__ == '__main__':
    for i in range (0, 4):
        A = TOAHModel(4)
        A.fill_first_stool(i)
        four_stools_solution(A, i, 0, 3, 1, 2)

