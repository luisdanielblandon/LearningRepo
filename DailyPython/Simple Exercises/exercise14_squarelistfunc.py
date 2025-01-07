def square_lists(numbers):      
      numbers = [number ** 2 for number in numbers]
      return numbers

data = [1, 2, 3, 4]

print(square_lists(data))
