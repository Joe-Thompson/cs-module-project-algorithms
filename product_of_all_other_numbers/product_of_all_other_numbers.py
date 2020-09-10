"""
Input: a List of integers
Returns: a List of integers
"""


def product_of_all_other_numbers(arr):
    current_index = 0
    copy_arr = [arr[i] for i in range(0, len(arr))]
    while current_index < len(arr):
        sum_of_products = 1
        for i in range(0, len(copy_arr)):
            if current_index == i:
                continue
            sum_of_products *= copy_arr[i]
        arr[current_index] = sum_of_products
        current_index += 1
    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8,
           5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
