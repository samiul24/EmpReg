from django.db.models.aggregates import Count
from rest_framework import fields, serializers
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

    """def to_representation(self, instance):
        print(self)
        print(instance)
        test=super().to_representation(instance)
        print(test['district'])
        print(type(test))
        return super().to_representation(instance)"""
       

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields='__all__'
    
"""class EmpBasicInfoSerialiser(serializers.ModelSerializer):
    district=DistrictSerializer()
    thana=ThanaSerializer()
    department=DepartmentSerializer()
    designation=DesignationSerializer()
    class Meta:
        model=EmpBasicInfo
        fields=[ 'id','first_name', 'last_name', 'department','designation', 'district', 'thana', ]"""

class EmpBasicInfoSerialiser(serializers.ModelSerializer):
    class Meta:
        model=EmpBasicInfo
        fields='__all__'
        

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


class EmpBasicInfoSalaryEducationSerialiser(serializers.ModelSerializer):
    #salary=EmpSalarySerializer()
    class Meta:
        model=EmpBasicInfo
        #fields="__all__"
        fields=[
                    'id','emp_id','first_name', 'last_name', 
                    'dob', 'phone', 'email', 
                    'thana', 'district', 'joiningdate', 
                    'department', 'designation', 'status',
        ]







