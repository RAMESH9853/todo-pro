from django.shortcuts import render,redirect
from .models import TodoData
# Create your views here.

    
def tododata(request):
    emp = TodoData.objects.all()
    return render(request,'mainpage.html',{'emps':emp})

def addemp(request):
    if request.method == 'GET':
        return render(request,'addtask.html')
    else:
        TodoData(
            title = request.POST['title'],
            description =  request.POST['description'],
            date =  request.POST['date'],
        ).save()

        return redirect(tododata)
    
def detailsform(request,id):
    data = TodoData.objects.get(id=id)
    return render(request,'detailsdata.html',{'data':data})

def update(request, id):
    task = TodoData.objects.get(id=id)
    return render(request,'updatingtask.html',{'task':task})

def update_task(request, id):
    task = TodoData.objects.get(id=id)
    task.title = request.POST['title']
    task.description = request.POST['description']
    task.date = request.POST['date']
    task.save()
    return redirect(tododata)

def delete(request, id):
    task = TodoData.objects.get(id=id)
    task.delete()
    return redirect(tododata)