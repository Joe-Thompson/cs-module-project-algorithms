"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    if len(arr) <= 1:
        return arr
    print(f"this is the arr: {arr}")
    starter = arr[0]
    print(f"this is the end_pointer: {starter}")
    for num in arr[1:]:
        if num == starter:
            arr.remove(num)
            arr.remove(starter)
            single_number(arr)
    return arr[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
