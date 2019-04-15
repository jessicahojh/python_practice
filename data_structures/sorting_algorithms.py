def bubble_sort(lst):
    """Runtime: 0(n^2)"""

    for i in range(len(lst) - 1):  # for i in [0, 1, 2, 3, 4]

        # keep track of whether we made a swap
        made_swap = False

        for j in range(len(lst) - 1 - i): # for j in [1, 2, 3, 4]
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True

        if not made_swap:
            # if no swap, list already sorted
            break

    return lst

print(bubble_sort([4, 2, 10, 6, 9, 1]))

print(range(5))


##############################################################################

def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine.
    Runtime: O(n log n)"""

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        # merge-lecture-snippet-start
        left_index = right_index = new_index = 0

        # Interleave left and right into list

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1
        # merge-lecture-snippet-end

        # If lists were uneven length, add remainder of longer list

        while left_index < len(left):
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1

    return lst

print(merge_sort([8, 2, 1, 9, 10, 5]))

###############################################################################

def quicksort(lst):
    """Quicksort.

    Iteratively pivot, sort lists, and combine.

    Runtime: O(n log n)
    """

    import random

    def _quicksort(lst, first, last):
        if first < last:

            # Find pivot point

            pivot = first + random.randrange(last - first + 1)
            lst[pivot], lst[last] = lst[last], lst[pivot]

            pivot = first

            for i in range(pivot, last):
                if lst[i] <= lst[last]:
                    lst[i], lst[pivot] = lst[pivot], lst[i]
                    pivot += 1

            lst[pivot], lst[last] = lst[last], lst[pivot]

            # Recurse
            _quicksort(lst, first, pivot - 1)
            _quicksort(lst, pivot + 1, last)

    _quicksort(lst, 0, len(lst) - 1)

    return lst

print(quicksort([5, 1, 9, 3, 2, 4]))