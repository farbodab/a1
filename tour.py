"""
functions to run TOAH tours.
"""
# this is commit 3
#this is gonna be amazing
#why wont this be commit 2
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
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=True):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """

    def three_stools_solution(model, cheese_amount, start_stool, end_stool, inter_stool):
        """
        Solution for three-peg TOAH model

        @param model: TOAHModel
        @param start_stool: int
        @param end_stool: int
        @param inter_stool: int
        """
        if cheese_amount >= 1:
            three_stools_solution(model, cheese_amount - 1, start_stool, inter_stool, end_stool)
            model.move(start_stool, end_stool)
            three_stools_solution(model, cheese_amount - 1, inter_stool, end_stool, start_stool)

    n = len(model._stools[0])
    three_stools_solution(model, n-1, 0, 2, 1)
    model.move(0, 3)
    three_stools_solution(model, n-1, 2, 3, 1)

if __name__ == '__main__':
    num_cheeses = 5
    delay_between_moves = 0.5
    console_animate = False

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
