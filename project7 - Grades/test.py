student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


def define_grade(score):
    if score <= 70:
        return "Fail"
    if score <= 80:
        return "Acceptable"
    if score <= 90:
        return "Exceeds Expectations"

    return "Outstanding"


student_grades = {}

for k in student_scores:
    student_grades[k] = define_grade(student_scores[k])

print(student_grades)