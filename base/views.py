from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Task, Student


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
        
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def student_view(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_task=Student.objects.get(id=id)
                return Response (StudentSerializer(temp_Student,many=False).data)
            except Student.DoesNotExist:
                return Response ("not found")
        all_Students=StudentSerializer(Student.objects.all(),many=True).data
        return Response ( all_Students)
    if req.method =='POST':
        print (req.data)
        tsk_serializer = StudentSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post...")
        else:
            return Response (tsk_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_Student=Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response ("not found")    
       
        temp_Student.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_Student=Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response ("not found")
       
        ser = StudentSerializer(data=req.data)
        old_Student = Student.objects.get(id=id)
        res = ser.update(old_Student, req.data)
        return Response(res)        
 
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def tasks(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_task=Task.objects.get(id=id)
                return Response (TaskSerializer(temp_task,many=False).data)
            except Task.DoesNotExist:
                return Response ("not found")
        all_tasks=TaskSerializer(Task.objects.all(),many=True).data
        return Response ( all_tasks)
    if req.method =='POST':
        print (req.data)
        tsk_serializer = TaskSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post...")
        else:
            return Response (tsk_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_task=Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")    
       
        temp_task.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_task=Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")
       
        ser = TaskSerializer(data=req.data)
        old_task = Task.objects.get(id=id)
        res = ser.update(old_task, req.data)
        return Response(res)
    
def index(req):
    return JsonResponse('hello', safe=False)
