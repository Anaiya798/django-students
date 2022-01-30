from django.shortcuts import render
from .my_statistics import q1, q2_q3_q4_q7, q5, q6, q8, q9
from .models import Course, Student, Lecture
from django.http import HttpResponse, HttpRequest


def show_statistics(request: HttpRequest) -> HttpResponse:
    lectures = Lecture.objects.all()
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'sillystudents/index.html', {
        'ans1': q1(courses, students, lectures),
        'ans2': q2_q3_q4_q7(courses, students, lectures)[0],
        'ans3': q2_q3_q4_q7(courses, students, lectures)[1],
        'ans4': q2_q3_q4_q7(courses, students, lectures)[2],
        'ans5': q5(lectures),
        'ans6': q6(courses, students),
        'ans7': q2_q3_q4_q7(courses, students, lectures)[3],
        'ans8': q8(courses, students, lectures),
        'ans9': q9(courses, lectures)
    })


def hello(request: HttpRequest) -> HttpResponse:
    return render(request, 'sillystudents/main_page.html')

