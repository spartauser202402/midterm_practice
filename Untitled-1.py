def get_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    avg = total / len(numbers)
    return avg

nums = [10, 20, 30, 40]
print(get_average(nums))
