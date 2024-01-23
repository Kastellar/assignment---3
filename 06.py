def filter_students_info(student_info):
    names_below_18 = [name for name, age, grade in student_info if age < 18]
    grades_above_18 = [grade for name, age, grade in student_info if age >= 18]
    return names_below_18, grades_above_18
