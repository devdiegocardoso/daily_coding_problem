"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""



def add_up_to_k(numbers, k):
    """_summary_

    Args:
        numbers (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i, value_i in enumerate(numbers):
        for j in range(i+1,len(numbers)):
            if value_i + numbers[j] == k:
                return True
    return False

def add_up_to_k_one_step(numbers: list, k):
    """_summary_

    Args:
        numbers (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    numbers.sort()
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == k:
            return True
        elif numbers[i] + numbers[j] > k:
            j -= 1
        else:
            i += 1
    return False

print(add_up_to_k([10,15,3,7],17))
print(add_up_to_k_one_step([10,15,3,7],17))
