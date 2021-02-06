from django.shortcuts import render
from rest_framework import viewsets
#from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
#from rest_framework import status

# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    # def list(self, request, pk=None):
    #     stu = Student.objects.all()
    #     serializer = StudentSerializer(stu, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk):
    #     id = pk
    #     stu = Student.objects.get(id = id)
    #     serializer = StudentSerializer(stu)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Record is Created'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk):
    #     id = pk
    #     stu = Student.objects.get(id = id)
    #     serializer = StudentSerializer(stu, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Record is Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update_partial(self, request, pk):
    #     id = pk
    #     stu = Student.objects.get(id = id)
    #     serializer = StudentSerializer(stu, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Record is Partially Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk):
    #     id = pk
    #     stu = Student.objects.get(id = id)
    #     stu.delete()
    #     return Response({'msg':'Record is deleted'})