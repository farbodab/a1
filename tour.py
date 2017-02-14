"""
functions to run TOAH tours.
"""
# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
import math
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not

    >>>> M = TOAHModel(4)
    >>>> M.fill_first_stool(6)
    >>>> tour_of_four_stools(M)
    """
    cheecount = len(model._stools[0])
    if animate is True:
        animated_four_stools(model, cheecount, 0, 3, 1, 2, delay_btw_moves)
        print("Number of moves: {}".format(model.moves))
    else:
        four_stools_solution(model, cheecount, 0, 3, 1, 2)
        print("Number of moves: {}".format(model.moves))


def three_stools_solution(model, ch_num, start_stool, end_stool, inter_stool):
    """
    Solution for three-peg TOAH model. Moves ch_num cheeses from start_stool
    to end_stool via inter_stool using the optimal three-stool solution.

    @param model: TOAHModel
    @param start_stool: int
    @param end_stool: int
    @param inter_stool: int
    """
    if ch_num >= 1:
        three_stools_solution(model, ch_num - 1, start_stool, inter_stool, end_stool)
        model.move(start_stool, end_stool)
        three_stools_solution(model, ch_num - 1, inter_stool, end_stool, start_stool)


def animated_three_stools(model, ch_num, start_stool, end_stool, inter_stool, delay_btw_moves):
    """
    @param model:
    @param ch_num:
    @param start_stool:
    @param end_stool:
    @param inter_stool:
    @param delay_btw_moves:
    """
    if ch_num >= 1:
        animated_three_stools(model, ch_num- 1, start_stool, inter_stool, end_stool, delay_btw_moves)
        model.move(start_stool, end_stool)
        print(model)
        animated_three_stools(model, ch_num - 1, inter_stool, end_stool, start_stool, delay_btw_moves)
        time.sleep(delay_btw_moves)


def four_stools_solution(model, ch_num, start_stool, end_stool, inter_stool1, inter_stool2):
    """
    Solution for four-stool TOAH model. Moves ch_num cheese from start_stool to end_stool
    via inter_stool1 and inter_stool2

    @param model: TOAHModel
    @param ch_num: int
    @param start_stool: int
    @param end_stool: int
    @param inter_stool1: int
    @param inter_stool2: int
    """
    x = ch_num
    y1 = x - math.floor(0.0007*x**2 + 0.1806*x + 2.265)
    y2 = x - y1
    if ch_num == 1:
        model.move(start_stool, end_stool)
    elif ch_num == 2:
        three_stools_solution(model, y1, start_stool, inter_stool2, inter_stool1)
        three_stools_solution(model, y2, start_stool, end_stool, inter_stool1)
        three_stools_solution(model, y1, inter_stool2, end_stool, inter_stool1)
    else:
        four_stools_solution(model, y1, start_stool, inter_stool1, inter_stool2, end_stool)
        three_stools_solution(model, y2, start_stool, end_stool, inter_stool2)
        four_stools_solution(model, y1, inter_stool1, end_stool, start_stool, inter_stool2)


def animated_four_stools(model, ch_num, start_stool, end_stool, inter_stool1, inter_stool2, delay_btw_moves):
    """
    I cannot seem to implement animations using the optimal solution without hitting the python recusion limit;
    sub-optimal solution animated.

    @param model: TOAHModel
    @param ch_num: int
    @param start_stool: int
    @param end_stool: int
    @param inter_stool1: int
    @param inter_stool2: int
    @param delay_btw_moves: float
    """
    x = ch_num
    y1 = x - math.floor(0.0007*x**2 + 0.1806*x + 2.265)
    y2 = x - y1
    if ch_num == 1:
        model.move(start_stool, end_stool)
        print(model)
    elif ch_num == 2:
        animated_three_stools(model, y1, start_stool, inter_stool2, inter_stool1, delay_btw_moves)
        animated_three_stools(model, y2, start_stool, end_stool, inter_stool1, delay_btw_moves)
        animated_three_stools(model, y1, inter_stool2, end_stool, inter_stool1, delay_btw_moves)
    else:
        animated_four_stools(model, y1, start_stool, inter_stool1, inter_stool2, end_stool, delay_btw_moves)
        animated_three_stools(model, y2, start_stool, end_stool, inter_stool2, delay_btw_moves)
        animated_four_stools(model, y1, inter_stool1, end_stool, start_stool, inter_stool2, delay_btw_moves)



if __name__ == '__main__':
    num_cheeses = 6
    delay_between_moves = 0.5
    console_animate = True

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folderwwa
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
