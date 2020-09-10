"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    cur_index = 0
    zero_index = 0
    while cur_index < len(arr):
        if arr[cur_index] != 0:
            swap_index = cur_index - zero_index
            arr[swap_index], arr[cur_index] = arr[cur_index], arr[swap_index]
        else:
            zero_index += 1

        cur_index += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
