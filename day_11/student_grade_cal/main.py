from day_11.input_validators.input_util import get_integer
from day_11.student_grade_cal.grades import calculate_marks_grade
from day_11.student_grade_cal.validations import get_number

marks = get_number("Enter a Subject Mark : ")
print(calculate_marks_grade(marks))


age = get_integer("Enter a age : ")