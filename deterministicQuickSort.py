def deterministic_quicksort(arr):
    """
    Deterministic QuickSort: always uses the first element as pivot.
    Returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lt = [x for x in arr if x < pivot]
    eq = [x for x in arr if x == pivot]
    gt = [x for x in arr if x > pivot]
    return deterministic_quicksort(lt) + eq + deterministic_quicksort(gt)