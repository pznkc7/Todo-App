from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def home(request):
    if request.method== 'POST':
        var1 = request.POST.get('title')
        if var1:
            Todo.objects.create(task = var1)
        return redirect('home')
    
    todo = Todo.objects.all()
    return render(request,'home.html',{'todos':todo})

def delete_todo(request,id):
    todo123 = Todo.objects.get(id=id)
    todo123.delete()
    return redirect('home')


