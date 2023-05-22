from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *

# Create your views here.

def index(request):
	tasks = Task.objects.all()
	form  = TaskForm()
	#https://docs.djangoproject.com/en/4.1/topics/forms/
	if request.method == 'POST':
		form = TaskForm(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'tasks': tasks, 'form': form}
	return render(request, 'tasks/list.html', context) 


def updateTask(request, pk):
	task = Task.objects.get(id = pk)
	form = TaskForm(instance = task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance = task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
	del_task = Task.objects.get(id = pk)

	if request.method == 'POST':
		del_task.delete()
		return redirect('/')

	context = {'del_task': del_task}
	return render(request, 'tasks/delete.html', context)

def testPage(request):
	tasks = Task.objects.all()
	form  = TaskForm()
	
	context = {'tasks': tasks, 'form': form}
	return render(request, 'tasks/test.html', context)
