from django.db.models.aggregates import Count
from rest_framework import serializers
from .models import District, Thana, Department, Designation, EmpBasicInfo, EmpSalary, EmpEducation

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields='__all__'

class ThanaSerializer(serializers.ModelSerializer):
    #district=DistrictSerializer()
    class Meta:
        model=Thana
        fields='__all__'
        #fields=['id','name', 'district']
       

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields='__all__'
    
class EmpBasicInfoSerialiser(serializers.ModelSerializer):    
    department_name = serializers.SerializerMethodField('get_department_name')
    designation_name = serializers.SerializerMethodField('get_designation_name')
    district_name = serializers.SerializerMethodField('get_district_name')
    thana_name = serializers.SerializerMethodField('get_thana_name')

    def get_department_name(self,employee_list):
        print(employee_list)
        department_name=employee_list["department__name"]
        return department_name

    def get_designation_name(self,employee_list):
        print(employee_list)
        designation_name=employee_list["designation__name"]
        return designation_name

    def get_district_name(self,employee_list):
        print(employee_list)
        district_name=employee_list["district__name"]
        return district_name
    
    def get_thana_name(self,employee_list):
        print(employee_list)
        thana_name=employee_list["thana__name"]
        return thana_name

    class Meta:
        model=EmpBasicInfo
        fields=[ 'id','first_name', 'last_name', 'department_name','designation_name', 'district_name', 'thana_name', ]
        #depth=2

class EmpBasicInfoDetailSerialiser(serializers.ModelSerializer):
    district=DistrictSerializer()
    thana=ThanaSerializer()
    department=DepartmentSerializer()
    designation=DesignationSerializer()
    class Meta:
        model=EmpBasicInfo
        fields=[
                    'id','emp_id','first_name', 'last_name', 
                    'dob', 'phone', 'email', 
                    'thana', 'district', 'joiningdate', 
                    'department', 'designation', 'status'
        ]
        #depth=2

class EmpSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=EmpSalary
        fields='__all__'

class EmpEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmpEducation
        fields='__all__'




