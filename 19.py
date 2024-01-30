def get_total_count_of_courses(students: dict) -> dict[str, int]:
    courses = [t for i in students.values() for t in i]
    return {course: courses.count(course) for course in set(courses)}


students = {
    "Name1": ["Calculus", "Programming", "Linear Algebra", "Culturology"],
    "Name2": ["Calculus", "Physical Education", "Politology"],
    "Name3": ["Programming", "Discrete Mathematics", "Politology"],
    "Name4": ["Politology", "Culturology", "Programming"],
}

print(get_total_count_of_courses(students))
