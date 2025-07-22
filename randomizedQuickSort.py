import random

def randomized_quicksort(arr):
    """
    Randomized QuickSort: picks a random pivot, partitions into <, ==, >,
    and recurses. Returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randrange(len(arr))]
    lt = [x for x in arr if x < pivot]
    eq = [x for x in arr if x == pivot]
    gt = [x for x in arr if x > pivot]
    return randomized_quicksort(lt) + eq + randomized_quicksort(gt)
