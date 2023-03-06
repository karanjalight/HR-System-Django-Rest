from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index' ),
    path('register/', views.register, name='register'), #<--to register new users
    
    #=====================   LIST AND DETAIL VIEW OF THE APIS  =====================
    # -------  Employer  ----------
    path('employer/', views.employer_list, name='employer'),
    path('employer/<int:pk>/',views.employer_detail, name='employee-detail'),


    # ---------    Employee ----------------
    path('employee/', views.employee_view , name='EmployeeView'),
    path('employee/<int:pk>/',views.employee_detail, name='employee-detail'),

    # ------  Company Assets api views  ------#
    path('asset/', views.CompanyAssets_list),
    path('asset/<int:pk>/', views.companyasset_detail),

    # ---------  Company Inventory  --------
    path('inventory/', views.CompanyInventoy_list),
    path('inventory/<int:pk>/', views.CompanyInventory_detail),

    # -------- Time Off  ---------------
    path('timeoff/', views.TimeOff_list, name='timeoff'),
    path('timeoff/<int:pk>/', views.TimeOff_detail, name='timeoff'),

    
]