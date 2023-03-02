# Binary search

sample_list = [1, 3, 5, 6, 6, 7, 8, 10]


def binarySearch(arr, x, low, high, mid):
    if x == mid:
        return (f'Found {x} at index {arr.index(x)}')
    elif x > mid:
        new_mid = ((high-low) // 2) + mid
        return binarySearch(arr, x, mid, high, new_mid)
    elif x < mid:
        new_mid = mid - ((high-low) // 2)
        return binarySearch(arr, x, low, mid, new_mid)

middle = (len(sample_list)-1) // 2

print(binarySearch(sample_list, 8, 0, len(sample_list)-1, middle))
