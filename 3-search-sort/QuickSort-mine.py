"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) < 2:
        return array
    stack_of_index = []
    index = (0, len(array) - 1)
    stack_of_index.append(index)
    for index in stack_of_index:
        e_index = index[0]
        pivot_index = index[1]
        while pivot_index > e_index:
            pivot = array[pivot_index]
            e = array[e_index]
            if e > pivot:
                array[pivot_index] = e
                array[e_index] = array[pivot_index - 1]
                array[pivot_index - 1] = pivot
                pivot_index -= 1
            else:
                e_index += 1
        low = index[0]
        high = index[1]
        if pivot_index > 1 and low < pivot_index - 1:
            stack_of_index.append((low, pivot_index - 1))
        if pivot_index < len(array) -1 and pivot_index + 1 < high:
            stack_of_index.append((pivot_index + 1, high))
    return array
            

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))