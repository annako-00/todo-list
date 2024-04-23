from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import todoSerializer
from rest_framework import viewsets
from .serializer import *


# Create your views here.
def todo(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    todos = Todo.objects.filter(project=project)

    if request.method == 'POST':
        todo_form = todoForm(request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.project = project
            todo.save()
            return redirect('project_detail', projectid=project_id)
    else:
        todo_form = todoForm()

    return render(request, 'todo.html', {'project': project, 'todos': todos, 'todo_form': todo_form})

def project(request):
     projects=Project.objects.all()
     return render(request,'project.html',{'projects':projects})

def loginpage(request):
     if request.method=='POST':
          user=request.POST['username']
          pass1=request.POST['passw1']
          user=authenticate(request,username=user,password=pass1)
          if user:
               login(request,user)
               messages.success(request,'user has been logged in')
               return redirect(project)
          else:
               print('invaild login')
     return render(request,'login.html')

def logoutpage(request):
     logout(request)
     messages.success(request,'user has been logged out')
     return redirect(project)


from django.http import JsonResponse

def add_todo_ajax(request):
    if request.method == 'POST':
        serializer = todoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)
    
def update_todo_status(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.filter(id=todo_id).first()
        if todo:
            status = request.POST.get('status', '')
            todo.status = status == 'true'  # Assuming 'true' is sent as string
            todo.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Todo not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

def eedit(request, description):
    try:
        todo = get_object_or_404(Todo, id=description)
    except Todo.DoesNotExist:
        return HttpResponse("Todo does not exist")

    if request.method == 'POST':
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.description = form.cleaned_data['description']
            todo.status = form.cleaned_data['status']
            todo.save()
            return redirect('todo', project_id=todo.project.projectid) 
    else:
        form = TodoForm(initial={'description': todo.description, 'status': todo.status})

    return render(request, 'edit.html', {'f1': form, 'description': todo.description})

def dtl(request, description):
    todo = get_object_or_404(Todo, id=description)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo', project_id=todo.project.projectid)  
    return render(request, 'delete.html', {'todo': todo})

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer

@api_view(['GET'])
def allproject(request):
     pro=Project.objects.all()
     serializer=projectSerializer(pro,many=True)
     return Response(serializer.data)

@api_view(['GET'])
def oneproject(request,id):
     pr=Todo.objects.get(id=id)
     serializer=todoSerializer(pr,many=False)
     return Response(serializer.data)
