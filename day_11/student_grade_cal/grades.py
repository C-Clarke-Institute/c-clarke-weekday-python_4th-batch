#business logic

def calculate_marks_grade(marks):

    if not 0 <= marks <= 100:
        raise ValueError("Marks Must Be between 0 and 100")

    if marks >= 75:
        return "A"
    if marks >= 65 :
        return "B"
    if marks >= 55 :
        return "C"
    if marks >= 40:
        return "S"
    else:
        return "W"