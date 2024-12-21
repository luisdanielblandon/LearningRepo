def calcsum(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

def calcaverage(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    average = total_sum / len(numbers)
    return average

def calcmax(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def calcmin(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number


# List of numbers
numbers = [10, 20, 30, 40, 50]

# Print the results
print(f"Sum: {calcsum(numbers)}")
print(f"Average: {calcaverage(numbers)}")
print(f"Maximum: {calcmax(numbers)}")
print(f"Minimum: {calcmin(numbers)}")