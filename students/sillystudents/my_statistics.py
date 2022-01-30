import numpy as np
from .models import Student


def q1(courses, students, lectures):
    courses_lectures = {}
    students_lectures = {}

    for course in courses:
        courses_lectures[course['name']] = 0

    for student in students:
        key_repr = student['surname'] + ' ' + student['name'] + ' ' + student['patronic']
        students_lectures[key_repr] = 0

    for lecture in lectures:
        courses_lectures[lecture['course']['name']] = courses_lectures[lecture['course']['name']] + 1

    for student in students:
        key_repr = student['surname'] + ' ' + student['name'] + ' ' + student['patronic']
        student_courses = Student.objects.get(id=student.id).course.all()
        for student_course in student_courses:
            students_lectures[key_repr] = students_lectures[key_repr] + courses_lectures[student_course['name']]

    return students_lectures


def q2_q3_q4_q7(courses, students, lectures):
    courses_students = {}
    most_popular_lectures = []
    least_popular_lectures = []
    least_popular_courses = []
    more_mean_value = []
    emails = []

    for course in courses:
        courses_students[course['name']] = 0

    for student in students:
        student_courses = Student.objects.get(id=student.id).course.all()
        for student_course in student_courses:
            courses_students[student_course['name']] = courses_students[student_course['name']] + 1
    maximum = max(courses_students.values())
    minimum = min(courses_students.values())
    mean_value = np.array(list(courses_students.values())).mean()

    for lecture in lectures:
        if courses_students[lecture['course']['name']] == maximum:
            most_popular_lectures.append(lecture['name'])
        if courses_students[lecture['course']['name']] == minimum:
            least_popular_lectures.append(lecture['name'])
            least_popular_courses.append(lecture['course']['name'])
        if courses_students[lecture['course']['name']] > mean_value:
            more_mean_value.append(lecture['name'])

    for student in students:
        student_courses = Student.objects.get(id=student.id).course.all()
        checkmark = False
        for student_course in student_courses:
            if student_course['name'] in least_popular_courses:
                checkmark = True
                break
        if not checkmark:
            emails.append(student['email'])

    return most_popular_lectures, least_popular_lectures, more_mean_value, emails


def q5(lectures):
    CURRENT_YEAR = 2021
    res = []

    for lecture in lectures:
        if lecture['course']['start'].year == CURRENT_YEAR:
            res.append(lecture['name'])

    return res


def q6(courses, students):
    courses_students = {}

    for course in courses:
        courses_students[course['name']]= []

    for student in students:
        student_courses = Student.objects.get(id=student.id).course.all()
        for student_course in student_courses:
            courses_students[student_course['name']].append(student['birth_date'].year)

    for k in courses_students.keys():
        courses_students[k] = round(np.array(courses_students[k]).mean())

    return courses_students


def q8(courses, students, lectures):
    courses_students = {}
    lectures_count = 0

    for course in courses:
        courses_students[course['name']] = 0

    for student in students:
        student_courses = Student.objects.get(id=student.id).course.all()
        for student_course in student_courses:
            courses_students[student_course['name']] = courses_students[student_course['name']] + 1

    for lecture in lectures:
        if courses_students[lecture['course']['name']] > 2:
            lectures_count = lectures_count + 1

    return lectures_count


def q9(courses, lectures):
    courses_lectures = {}

    for course in courses:
        courses_lectures[course['name']] = []

    for lecture in lectures:
        days = (lecture['date'].year - 1) * 365 + (lecture['date'].month - 1) * 30 + lecture['date'].day
        courses_lectures[lecture['course']['name']].append(days)

    for k in courses_lectures.keys():
        courses_lectures[k] = sorted(courses_lectures[k], reverse=True)
        for i in range(len(courses_lectures[k]) - 1):
            courses_lectures[k][i] = courses_lectures[k][i] - courses_lectures[k][i+1]
        courses_lectures[k][len(courses_lectures[k]) - 1] = 0
        courses_lectures[k] = round(np.array(courses_lectures[k]).mean())

    return courses_lectures





