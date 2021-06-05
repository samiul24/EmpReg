from django.urls import path
from .views import DistrictList, Districts, ThanaList, Thanas, Designations, DesignationList, DepartmenttList, \
    EmpList, EmpListDetail, EmpSalaryList, EmpEducationList, EmpBasicInfoSalaryEducation

urlpatterns = [
    path('districtlist/', DistrictList.as_view()),
    path('district/<int:pk>/', Districts.as_view()),
    path('thanalist/', ThanaList.as_view()),
    path('thana/<int:pk>/', Thanas.as_view()),
    path('departmentlist/', DepartmenttList.as_view()),
    path('designationlist/', DesignationList.as_view()),
    path('designation/<int:pk>/', Designations.as_view()),
    path('emplist/', EmpList.as_view()),
    path('empinfosetup/', EmpBasicInfoSalaryEducation.as_view()),
    path('emplistdetail/', EmpListDetail.as_view()),
    path('empsalarylist/', EmpSalaryList.as_view()),
    path('empeducationlist/', EmpEducationList.as_view()),
    
]
