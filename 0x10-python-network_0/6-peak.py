#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    
    # Get the length of the list
    n = len(list_of_integers)
    
    # Handle edge cases (first and last elements)
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    
    # Binary search to find a peak
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return list_of_integers[left]

