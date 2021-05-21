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
    class Meta:
        model=EmpBasicInfo
        fields=['first_name','last_name','email',]
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




