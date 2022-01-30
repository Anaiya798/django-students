from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        if item == 'name':
            return self.name
        elif item == 'start':
            return self.start
        elif item == 'end':
            return self.end
        else:
            raise ValueError(f'model Course does not have the {item} field')


class Student(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronic = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.CharField(max_length=100)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.patronic

    def __getitem__(self, item):
        if item == 'surname':
            return self.surname
        elif item == 'name':
            return self.name
        elif item == 'patronic':
            return self.patronic
        elif item == 'birth_date':
            return self.birth_date
        elif item == 'email':
            return self.email
        elif item == 'course':
            return self.course
        else:
            raise ValueError(f'model Student does not have the {item} field')


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        if item == 'name':
            return self.name
        elif item == 'date':
            return self.date
        elif item == 'course':
            return self.course
        else:
            raise ValueError(f'model Lecture does not have the {item} field')
