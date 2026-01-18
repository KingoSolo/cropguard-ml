numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_even_numbers(numbers):
     "Return a list of even numbers"
     even_numbers = []
     for number in numbers:
          if number % 2 == 0:
               even_numbers.append(number)
     return even_numbers

print(find_even_numbers(numbers))