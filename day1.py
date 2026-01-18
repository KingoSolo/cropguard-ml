# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def find_even_numbers(numbers):
#      "Return a list of even numbers"
#      even_numbers = []
#      for number in numbers:
#           if number % 2 == 0:
#                even_numbers.append(number)
#      return even_numbers

# print(find_even_numbers(numbers))

# family = {'father': 'John','mother': 'Jane','son': 'Mike'}

# grades = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'B', 'A']
# def count_grades(grades):
#     "Return a dictionary with the count of each grade"
#     grade_count = {}

#     for grade in grades:
#         if grade in grade_count:
#             grade_count[grade] += 1
#         else:
#             grade_count[grade] = 1
#     return grade_count

# print(count_grades(grades))

from tkinter.font import names


def student_summary(names,scores):
    "Returns a dictionary of student summaries"
    summary = {}
    for name, score in zip(names, scores):
        summary[name] = score
    return summary
print(student_summary(['Alice', 'Bob', 'Charlie'], [85, 92, 78]))