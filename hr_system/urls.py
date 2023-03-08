from django.urls import path
from . import views
from knox import views as knox_views

from .views import RegisterAPI, LoginAPI

urlpatterns = [
    #user urlls
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    

    ##################    THis are Page navigators ######################
    path('home/', views.index, name='index' ),
    path('register/', views.register, name='register'), #<--to register new users
    path('employee/', views.employee, name='employee'),
    path('inventory/', views.inventory, name='inventory'),
    path('leave/', views.leave, name='leave'),
    path('asset/', views.asset, name='asset'),
    
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