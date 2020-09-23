from django.http import HttpResponse
from django.shortcuts import render

def groups_list(request):
    groups = (
        {'name': 'MTM-21',
         'leader': 'Шварценеггер'},

        {'name': 'MTM-22',
         'leader': 'Чан'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)