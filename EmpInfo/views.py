from datetime import date
import time

from django.shortcuts import render
from django.http import Http404
from django.db.models import Max, Min, Avg, F, OuterRef, Subquery
from django.db.models import Q
from django.db.models.functions import Length
from django.db.models import CharField, Count
CharField.register_lookup(Length)

from .models import District, Thana, Department, Designation, EmpBasicInfo, EmpSalary, EmpEducation
from .serializers import DistrictSerializer, ThanaSerializer, DepartmentSerializer, DesignationSerializer, \
                        EmpBasicInfoSerialiser, EmpBasicInfoDetailSerialiser, EmpSalarySerializer, EmpEducationSerializer, \
                        EmpBasicInfoSalaryEducationSerialiser

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, viewsets
from rest_framework import status


# Create your views here.
class DistrictList(APIView):
    def get(self, request):
        district_list=District.objects.all()
        serializer=DistrictSerializer(district_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Districts(APIView):
    def get_object(self, pk):
        try:
            return District.objects.get(pk=pk)
        except District.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        district=self.get_object(pk)

        #Example of related_name
        """d = District.objects.get(id=4)
        print(d)
        print(type(d))
        #e = d.district.all()
        #SELECT "EmpInfo_thana"."id", "EmpInfo_thana"."district_id", "EmpInfo_thana"."name" FROM "EmpInfo_thana" WHERE "EmpInfo_thana"."district_id" = 1
        #e = d.district.filter(id=3)
        #SELECT "EmpInfo_thana"."id", "EmpInfo_thana"."district_id", "EmpInfo_thana"."name" FROM "EmpInfo_thana" WHERE ("EmpInfo_thana"."district_id" = 4 AND "EmpInfo_thana"."id" = 3)
        #e = d.district.filter(id=3, district__name='Dhaka')
        #SELECT "EmpInfo_thana"."id", "EmpInfo_thana"."district_id", "EmpInfo_thana"."name" FROM "EmpInfo_thana" INNER JOIN "EmpInfo_district" ON ("EmpInfo_thana"."district_id" = "EmpInfo_district"."id") WHERE ("EmpInfo_thana"."district_id" = 4 AND "EmpInfo_district"."name" = Dhaka AND "EmpInfo_thana"."id" = 3)
        print(e)
        print(e.query)
        print(type(e))"""

        #Example of related_query_name
        """d = District.objects.filter(Q(tag__name="Mohammadpur") | Q(tag__name="Gulshan")).distinct()
        #SELECT "EmpInfo_district"."id", "EmpInfo_district"."name" FROM "EmpInfo_district" INNER JOIN "EmpInfo_thana" ON ("EmpInfo_district"."id" = "EmpInfo_thana"."district_id") WHERE "EmpInfo_thana"."name" = Mohammadpur
        #d = District.objects.filter(tag__name="Mohammadpur")
        #SELECT DISTINCT "EmpInfo_district"."id", "EmpInfo_district"."name" FROM "EmpInfo_district" INNER JOIN "EmpInfo_thana" ON ("EmpInfo_district"."id" = "EmpInfo_thana"."district_id") WHERE ("EmpInfo_thana"."name" = Mohammadpur OR "EmpInfo_thana"."name" = Gulshan)
        print(d.query)
        print(d)"""
  

        serializer=DistrictSerializer(district)
        return Response(serializer.data)
    
    def put(self, request, pk):
        district=self.get_object(pk)
        serializer=DistrictSerializer(district, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        district=self.get_object(pk)
        district.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ThanaList(APIView):
    def get(self, request):
        thana_list=Thana.objects.all()
        #print(type(thana_list))
        serializer=ThanaSerializer(thana_list, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=ThanaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Thanas(APIView):
    def get_object(self, pk):
        try:
            return Thana.objects.get(pk=pk)
        except Thana.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        thana=self.get_object(pk)

        serializer=ThanaSerializer(thana)
        return Response(serializer.data)
    
    def put(self, request, pk):
        thana=self.get_object(pk)
        serializer=ThanaSerializer(thana, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        thana=self.get_object(pk)
        thana.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DepartmenttList(APIView):
    def get(self, request):
        department_list=Department.objects.all()
        serializer=DepartmentSerializer(department_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DesignationList(APIView):
    def get(self, request):
        designation_list=Designation.objects.all()
        serializer=DesignationSerializer(designation_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=DesignationSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data) #Order Dictionary 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Designations(APIView):
    def get_object(self, pk):
        try:
            return Designation.objects.get(pk=pk)
        except Designation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        #designation=Designation.objects.get(pk=pk)
        designation=self.get_object(pk)
        serializer=DesignationSerializer(designation)
        return Response(serializer.data)

    def put(self, request, pk):
        designation=Designation.objects.get(pk=pk)
        #designation=self.get_object(pk)
        serializer=DesignationSerializer(designation, request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpList(APIView):
    def get(self, request):
        print(type(request.data))
        print(request.data)
        employee_list=EmpBasicInfo.objects.all()
        
        serializer=EmpBasicInfoSerialiser(employee_list, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        today=date.today()
        day_month_year_dept_desig=f'{today.day:02}'+f'{today.month:02}'+str(today.year)[2:]+f'{request.data["department"]:02}'+f'{request.data["designation"]:02}'
        try:
            maximum_id=EmpBasicInfo.objects.aggregate(Max('id'))['id__max']
            maximum_id_info=EmpBasicInfo.objects.filter(id=maximum_id).values('emp_id','first_name','last_name','dob')
            for x in maximum_id_info:
                print(x['first_name'])
            print(maximum_id_info)
            #print(type(maximum_id_info))
        except:
            maximum_id=0
        emp_id=maximum_id+1
        print(emp_id)
        request.data["emp_id"]=day_month_year_dept_desig+str(emp_id)

        serializer=EmpBasicInfoSerialiser(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpListDetail(APIView):
    def get(self, request):
        employee_list=EmpBasicInfo.objects.all()
        serializer=EmpBasicInfoDetailSerialiser(employee_list, many=True)
        return Response(serializer.data)

class EmpSalaryList(APIView):
    def get(self, request):
        salary_list=EmpSalary.objects.all()
        serializer=EmpSalarySerializer(salary_list, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=EmpSalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class EmpEducationList(APIView):
    def get(self, request):
        salary_list=EmpEducation.objects.all()
        serializer=EmpEducationSerializer(salary_list, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=EmpEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class EmpBasicInfoSalaryEducation(APIView):
    def get(self, request):
        employee_list=EmpBasicInfo.objects.all()
        
        serializer=EmpBasicInfoSalaryEducationSerialiser(employee_list, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        phone=request.data["phone"]
        print(phone)
        if len(phone) != 11:
            context={
                "error":"True",
                "message":"Invalid Ph No",
            }
            return Response (context)
        salary=request.data.get("salary")
        education=request.data["education"]
        
        today=date.today()
        day_month_year_dept_desig=f'{today.day:02}'+f'{today.month:02}'+str(today.year)[2:]+f'{request.data["department"]:02}'+f'{request.data["designation"]:02}'
        day_month_year_dept_desig=f'{today.day:02}{today.month:02}{(today.year)[2:]}{request.data["department"]:02}{request.data["designation"]:02}'
        try:
            maximum_id=EmpBasicInfo.objects.aggregate(Max('id'))['id__max']
        except:
            maximum_id=0
        emp_id=maximum_id+1
        request.data["emp_id"]=day_month_year_dept_desig+str(emp_id)
        
        try:
            serializer=EmpBasicInfoSalaryEducationSerialiser(data=request.data)
            if serializer.is_valid():
                emp_id=serializer.save()

            salary.update({"employee":int(emp_id.id)})
            salaryserializer=EmpSalarySerializer(data=salary)
            if salaryserializer.is_valid():
                emp_salary=salaryserializer.save()
            
            if bool(education):
                for emp_education in education:
                    emp_education.update({"employee":emp_id.id})
                    education_serializer=EmpEducationSerializer(data=emp_education)
                    if education_serializer.is_valid():
                        education_serializer.save()         

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


