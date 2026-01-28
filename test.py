def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers



def count_grades(grades):
    grade = {}
    count = 0

    for grade_letter in grades:
        if grade_letter not in grade:
            grade[grade_letter] = 1
        else:
            grade[grade_letter] += 1
        count += 1
    return grade


def analyze_numbers(numbers):
    analyze = {}


    even_numbers = []
    odd_numbers = []
    total_sum = 0
    average = 0.0

    for num in numbers:
        total_sum += num
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
  
    average = total_sum / len(numbers)
    analyze['even_numbers'] = even_numbers
    analyze['odd_numbers'] = odd_numbers
    analyze['total_sum'] = total_sum
    analyze['average'] = average

    return analyze

print(filter_even_numbers([1,2,3,4,5,6,7,8,9,10]))
print(count_grades(['A','B','A','C','A','B','B']))
print(analyze_numbers([10,15,20,25,30]))