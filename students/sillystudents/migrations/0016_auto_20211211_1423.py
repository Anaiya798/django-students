from datetime import date
from django.db import migrations


def add_lectures(apps, schema_editor):
    Lecture = apps.get_model('sillystudents', 'Lecture')
    Course = apps.get_model('sillystudents', 'Course')

    general = Lecture.objects.create(name='Адаптация к обучению в университете', date=date(2021, 9, 5),
                                     course=Course.objects.get(name='Общий'))
    general.save()

    python1 = Lecture.objects.create(name='Язык Python. Базовые синтаксические конструкции', date=date(2021, 9, 15),
                                     course=Course.objects.get(name='Python'))
    python1.save()
    python2 = Lecture.objects.create(name='Наследование в Python', date=date(2021, 10, 12),
                                     course=Course.objects.get(name='Python'))
    python2.save()
    python3 = Lecture.objects.create(name='Фреймворк Django', date=date(2021, 11, 26),
                                     course=Course.objects.get(name='Python'))
    python3.save()

    java1 = Lecture.objects.create(name='Типы данных в Java', date=date(2021, 9, 10),
                                   course=Course.objects.get(name='Java'))
    java1.save()
    java2 = Lecture.objects.create(name='Интерфейсы в Java', date=date(2021, 10, 18),
                                   course=Course.objects.get(name='Java'))
    java2.save()
    java3 = Lecture.objects.create(name='Многопоточное программирование в Java', date=date(2021, 11, 30),
                                   course=Course.objects.get(name='Java'))
    java3.save()

    devops1 = Lecture.objects.create(name='Основные инструменты DevOps', date=date(2021, 9, 8),
                                     course=Course.objects.get(name='DevOps'))
    devops1.save()
    devops2 = Lecture.objects.create(name='DevOps. Непрерывная интеграция', date=date(2021, 12, 1),
                                     course=Course.objects.get(name='DevOps'))
    devops2.save()

    testing1 = Lecture.objects.create(name='Введение в тестирование ПО', date=date(2021, 10, 1),
                                      course=Course.objects.get(name='Testing'))
    testing1.save()
    testing2 = Lecture.objects.create(name='Регрессионное тестирование', date=date(2021, 12, 12),
                                      course=Course.objects.get(name='Testing'))
    testing2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('sillystudents', '0015_auto_20211211_1412'),
    ]

    operations = [
        migrations.RunPython(add_lectures),
    ]
