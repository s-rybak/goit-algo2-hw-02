def find_min_max(numbers):
    """
    Знаходить мінімальне і максимальне значення в списку чисел

    Args:
        numbers: Список чисел

    Returns:
        Кортеж з мінімальним і максимальним значеннями
    """
    if len(numbers) == 1:
        return (numbers[0], numbers[0])
    else:
        mid = len(numbers) // 2
        left_min, left_max = find_min_max(numbers[:mid])
        right_min, right_max = find_min_max(numbers[mid:])
        return (min(left_min, right_min), max(left_max, right_max))


print(find_min_max([1, 2, 3]))  # (1, 3)
print(find_min_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # (1, 10)
print(find_min_max([-1, 2, 3, 4, 500]))  # (-1, 500)
