
def array_testing():
    arr = [2, 6, 3, 4, 5]
    print(f'Original arr: {arr}')
    
    arr.pop()
    print(f'Pop: {arr}')

    print(f'Index of number 3: {arr.index(3)}')

    arr.append(9)
    print(f'9 appended: {arr}')

    print(f'Size of arr: {len(arr)}')

    print(f'How many twos in arr: {arr.count(2)}')

    arr.reverse()
    print(f'Reversed: {arr}')

    arr.remove(3)
    print(f'Removing 3: {arr}')

    arr.sort()
    print(f'Sorted: {arr}')

    arr.clear()
    print(f'Removing all elements: {arr}')

array_testing()
