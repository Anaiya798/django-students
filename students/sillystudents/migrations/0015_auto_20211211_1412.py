from datetime import date
from django.db import migrations


def add_students(apps, schema_editor):
    Student = apps.get_model('sillystudents', 'Student')
    Course = apps.get_model('sillystudents', 'Course')

    ivanov = Student.objects.create(surname='Иванов', name='Иван', patronic='Алексеевич', birth_date=date(2002, 9, 25),
                                    email='kukusik@yandex.ru')
    ivanov.course.add(Course.objects.get(name='Общий'))
    ivanov.course.add(Course.objects.get(name='Python'))
    ivanov.course.add(Course.objects.get(name='Java'))
    ivanov.save()

    astakhov = Student.objects.create(surname='Астахов', name='Кирилл', patronic='Сергеевич', birth_date=date(2000, 3, 13),
                                      email='kirusha@yandex.ru')
    astakhov.course.add(Course.objects.get(name='Общий'))
    astakhov.course.add(Course.objects.get(name='Java'))
    astakhov.save()

    shmeleva = Student.objects.create(surname='Шмелева', name='Ксения', patronic='Витальевна',
                                      birth_date=date(2001, 4, 15),
                                      email='astro-zeneka2001@gmail.com')
    shmeleva.course.add(Course.objects.get(name='Общий'))
    shmeleva.course.add(Course.objects.get(name='Java'))
    shmeleva.course.add(Course.objects.get(name='DevOps'))
    shmeleva.save()

    voronina = Student.objects.create(surname='Воронина', name='Ксения', patronic='Игоревна',
                                      birth_date=date(2002, 11, 11),
                                      email='i_am_vorona@gmail.com')
    voronina.course.add(Course.objects.get(name='Общий'))
    voronina.save()

    petrov = Student.objects.create(surname='Петров', name='Андрей', patronic='Петрович',
                                    birth_date=date(1999, 12, 28),
                                    email='privet-andrey99@gmail.com')
    petrov.course.add(Course.objects.get(name='Общий'))
    petrov.course.add(Course.objects.get(name='Java'))
    petrov.course.add(Course.objects.get(name='DevOps'))
    petrov.course.add(Course.objects.get(name='Testing'))
    petrov.save()

    krilin = Student.objects.create(surname='Крилин', name='Андрей', patronic='Викторович',
                                    birth_date=date(2001, 12, 16),
                                    email='privet-andrey01@gmail.com')
    krilin.course.add(Course.objects.get(name='Общий'))
    krilin.course.add(Course.objects.get(name='Java'))
    krilin.course.add(Course.objects.get(name='Testing'))
    krilin.save()

    ostashko = Student.objects.create(surname='Осташко', name='Руслан', patronic='Олегович',
                                      birth_date=date(2001, 5, 5),
                                      email='rus-rus@yandex.ru')
    ostashko.course.add(Course.objects.get(name='Общий'))
    ostashko.course.add(Course.objects.get(name='Python'))
    ostashko.save()

    lodyr = Student.objects.create(surname='Лодырь', name='Илья', patronic='Михайлович',
                                   birth_date=date(2001, 5, 15),
                                   email='iluha-ha-ha-ha@yandex.ru')
    lodyr.course.add(Course.objects.get(name='Общий'))
    lodyr.save()

    sorokin = Student.objects.create(surname='Сорокин', name='Сергей', patronic='Сергеевич',
                                     birth_date=date(2002, 6, 9),
                                     email='sorokin.sergey@gmail.com')
    sorokin.course.add(Course.objects.get(name='Общий'))
    sorokin.course.add(Course.objects.get(name='Java'))
    sorokin.save()

    kholodova = Student.objects.create(surname='Холодова', name='Наталья', patronic='Вениаминовна',
                                       birth_date=date(2000, 6, 16),
                                       email='natasha-ne-natalie@gmail.com')
    kholodova.course.add(Course.objects.get(name='Общий'))
    kholodova.course.add(Course.objects.get(name='Testing'))
    kholodova.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sillystudents', '0014_auto_20211211_1407'),
    ]

    operations = [
        migrations.RunPython(add_students),
    ]
