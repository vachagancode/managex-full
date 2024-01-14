from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from .models import User
from .models import Task

from .serializers import UserSerializer, TasksSerializer

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    # Create a Response object instead of HttpResponse
    response = Response(serializer.data)

    # Set CORS headers
    response["Access-Control-Allow-Origin"] = "http://localhost:5173"
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "Content-Type"

    return response

@api_view(['GET', 'PUT'])
def getDataSingleObject(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def addData(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    Response(serializer.data)["Access-Control-Allow-Origin"] = "http://localhost:5173"
    Response(serializer.data)["Access-Control-Allow-Methods"] = "GET"
    Response(serializer.data)["Access-Control-Allow-Headers"] = "Content-Type"

    return Response(serializer.data)

@api_view(['GET'])
def getTasksData(request):
    tasks = Task.objects.all()
    serializer = TasksSerializer(tasks, many=True) 

    response = Response(serializer.data)

    response["Access-Control-Allow-Origin"] = "http://localhost:5173"
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "Content-Type"

    return response

@api_view(['POST'])
def addTasksData(request):
    serializer = TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = Response(serializer.data)
    else:
        response = Response(serializer.errors, status=400)

    response["Access-Control-Allow-Origin"] = "http://localhost:5173"
    response["Access-Control-Allow-Methods"] = "POST"
    response["Access-Control-Allow-Headers"] = "Content-Type"

    return response

@api_view(['PUT'])
def putTasksData(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TasksSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteTasksData(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response({"success": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)