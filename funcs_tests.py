# Project 4 - Word Search
#
# Name: Kelsey Nguyen
# Instructor: Workman

import unittest
from funcs import *

class TestCases(unittest.TestCase):
    
    def test_organize_puzzle0(self):
        strings = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        expected = ["WAQHGTTWEE", "CBMIVQQELS", "APXWKWIIIL", "LDELFXPIPV", "PONDTMVAMN", "OEDSOYQGOB", "LGQCKGMMCT", "YCSLOACUZM", "XVDMGSXCYZ", "UUIUNIXFNU"]
        actual = organize_puzzle(strings)
        self.assertEqual(expected, actual)

    def test_organize_words0(self):
        words = "UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST"
        expected = ["UNIX", "CALPOLY", "GCC", "SLO", "CPE", "COMPILE", "VIM", "TEST"]
        actual = organize_words(words)
        self.assertEqual(expected, actual)

    def test_organize_words1(self):
        words = "SLACK HIGH HIGHLAND CHORRO PEACH BROAD GRAND OSOS MORRO HIGUERA MARSH FOOTHILL NIPOMO MILL PALM"
        expected = ["SLACK", "HIGH", "HIGHLAND", "CHORRO", "PEACH", "BROAD", "GRAND", "OSOS", "MORRO", "HIGUERA", "MARSH", "FOOTHILL", "NIPOMO", "MILL", "PALM"]
        actual = organize_words(words)
        self.assertEqual(expected, actual)

    def test_go_foward0(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "UNIX"
        expected = (9,3)
        actual = go_forward(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_foward1(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "KELSEY"
        expected = (-1,-1)
        actual = go_forward(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_backward0(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "VIM"
        expected = (1,4)
        actual = go_backward(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_backward1(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "KELSEY"
        expected = (-1,-1)
        actual = go_backward(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_down0(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "BTM"
        expected = (5, 9)
        actual = go_down(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_down2(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "CALPOLY"
        expected = (1, 0)
        actual = go_down(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_down3(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "KELSEY"
        expected = (-1, -1)
        actual = go_down(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_up0(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "DNE"
        expected = (5, 2)
        actual = go_up(puzzle, word)
        self.assertEqual(expected, actual)
    
    def test_go_up1(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "YLOP"
        expected = (7, 0)
        actual = go_up(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_up3(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "KELSEY"
        expected = (-1, -1)
        actual = go_up(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_diagonal0(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "DOG"
        expected = (4, 3)
        actual = go_diagonal(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_diagonal1(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "GCC"
        expected = (6, 5)
        actual = go_diagonal(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_diagonal2(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "SLO"
        expected = (-1,-1)
        actual = go_diagonal(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_diagonal3(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "WPA"
        expected = (2, 5)
        actual = go_diagonal(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_diagonal4(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "FMQM"
        expected = (3, 4)
        actual = go_diagonal(puzzle, word)
        self.assertEqual(expected, actual)

    def test_go_diagonal5(self):
        puzzle = organize_puzzle("WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
        word = "UYU"
        expected = (7, 7)
        actual = go_diagonal(puzzle, word)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
   unittest.main()

