from datetime import date
from django.db import migrations


def add_courses(apps, schema_editor):
    Course = apps.get_model('sillystudents', 'Course')

    course1 = Course.objects.create(name='Python', start=date(2021, 9, 15), end=date(2021, 12, 16))
    course1.save()

    course2 = Course.objects.create(name='Java', start=date(2021, 9, 10), end=date(2021, 12, 21))
    course2.save()

    course3 = Course.objects.create(name='Общий', start=date(2021, 9, 5), end=date(2021, 11, 30))
    course3.save()

    course4 = Course.objects.create(name='DevOps', start=date(2021, 9, 8), end=date(2021, 12, 25))
    course4.save()

    course5 = Course.objects.create(name='Testing', start=date(2021, 10, 1), end=date(2021, 12, 28))
    course5.save()

class Migration(migrations.Migration):

    dependencies = [
        ('sillystudents', '0013_alter_course_id_alter_lecture_id_alter_student_id'),
    ]

    operations = [
        migrations.RunPython(add_courses),
    ]
