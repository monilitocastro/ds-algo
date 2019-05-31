import unittest
import quicksort

class Test(unittest.TestCase):

    def test_sort(self):
        unsorted = [7, 5, 8, 3, 6, 5, 9, 4]
        expected = [3, 4, 5, 5, 6, 7, 8, 9]
        result = quicksort.sortList(unsorted)

        self.assertListEqual(result, expected)

    def test_split_even_width(self):
        # will expect 3 arrays given back in array
        # where 0th index has 1 width less than 2nd index
        # and 1st index is 1 item
        unsortedEvenWidth = [7, 5, 8, 3, 6, 5, 9, 4]
        expectedLeftWidth = 3
        expectedMiddleWidth = 1
        expectedRightWidth = 4
        result = quicksort.split(unsortedEvenWidth)
        self.assertEqual(len(result[0]), expectedLeftWidth, "Expecting left width to be " + str(expectedLeftWidth))
        self.assertEqual(len(result[1]), expectedMiddleWidth, "Expecting middle width to be " + str(expectedMiddleWidth))
        self.assertEqual(len(result[2]), expectedRightWidth, "Expecting right width to be " + str(expectedRightWidth))

    def test_split_odd_width(self):
        # will expect 3 arrays given back in array
        # where 0th index and 2nd index have same length
        # and 1st index is 1 item
        unsortedEvenWidth = [7, 5, 8, 3, 6, 5, 9]
        expectedLeftWidth = 3
        expectedMiddleWidth = 1
        expectedRightWidth = 3
        result = quicksort.split(unsortedEvenWidth)
        self.assertEqual(len(result[0]), expectedLeftWidth, "Expecting left width to be " + str(expectedLeftWidth))
        self.assertEqual(len(result[1]), expectedMiddleWidth, "Expecting middle width to be " + str(expectedMiddleWidth))
        self.assertEqual(len(result[2]), expectedRightWidth, "Expecting right width to be " + str(expectedRightWidth))
        

    def test_split_even(self):
        # will expect 3 arrays given back in array
        # where 0th index array has numbers less than middle
        # and 2nd index array has numbers greater than middle
        unsortedEvenWidth = [7, 5, 8, 3, 6, 5, 9, 4]
        expectedLeft = [3, 4, 5]
        expectedMiddle = [5]
        expectedRight = [6, 7, 8, 9]
        result = quicksort.split(unsortedEvenWidth)
        self.assertListEqual(result[0], expectedLeft, "Expecting left width to be " + str(expectedLeft) + ", instead we get " + str(result[0]))
        self.assertListEqual(result[1], expectedMiddle, "Expecting middle width to be " + str(expectedMiddle) + ", instead we get " + str(result[1]))
        self.assertListEqual(result[2], expectedRight, "Expecting right width to be " + str(expectedRight) + ", instead we get " + str(result[2]))

        

    def test_split_odd(self):
        # will expect 3 arrays given back in array
        # where 0th index array has numbers less than middle
        # and 2nd index array has numbers greater than middle
        unsortedEvenWidth = [7, 5, 8, 3, 6, 5, 4]
        expectedLeft = [3, 4, 5]
        expectedMiddle = [5]
        expectedRight = [6, 7, 8]
        result = quicksort.split(unsortedEvenWidth)
        self.assertListEqual(result[0], expectedLeft, "Expecting left width to be " + str(expectedLeft) + ", instead we get " + str(result[0]))
        self.assertListEqual(result[1], expectedMiddle, "Expecting middle width to be " + str(expectedMiddle) + ", instead we get " + str(result[1]))
        self.assertListEqual(result[2], expectedRight, "Expecting right width to be " + str(expectedRight) + ", instead we get " + str(result[2]))

if __name__ == "__main__":
    unittest.main()