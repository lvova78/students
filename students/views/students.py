from django.http import HttpResponse
from django.shortcuts import render


def students_list(request):
    students = (
        {'id': 1,
        'first_name': 'Арнольд',
        'last_name': 'Шварценеггер',
        'ticket': 235,
        'image': 'img/Schwarzenegger.jpg'},

        {'id': 2,
        'first_name': 'Джекі',
        'last_name': 'Чан',
        'ticket': 2123,
        'image': 'img/JackieChan.jpg'},

        {'id': 3,
         'first_name': 'Квентін',
         'last_name': 'Тарантіно',
         'ticket': 777,
         'image': 'img/Tarantino.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)