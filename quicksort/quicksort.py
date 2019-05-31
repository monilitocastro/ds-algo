import math

def sortList(unsorted):
    result = []


    return result

def split(unsorted):
    left = []
    right = []
    length = len(unsorted)
    midLength = (length-1) // 2
    midIndex= midLength - 1
    midValue = unsorted[midIndex]
    middle = [midValue]
    for x in range(len(unsorted)):
        if x == midIndex:
            continue
        curr = unsorted[x]
        if curr <= midValue:
            left.insert(len(left), curr)
        else:
            right.insert(len(right), curr)

    return [left, middle, right]