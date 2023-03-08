from rest_framework import routers,serializers,viewsets
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    

# --------------------  Employer ----------------------------
class EmployerModelSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField    
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=Employer.objects.all(),  many=False)  
  
    class Meta:
        model = Employer
        fields = [ 'pk', 'user', 'role', 'company', 'email', 'phone_number', 'employee_number', 'tasks']
  
# -----------------   Employee --------------------
class EmployeeModelSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    user = serializers.PrimaryKeyRelatedField(queryset=Employer.objects.all(),  many=False)
    employer_name = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),  many=False)
      
    class Meta:
        model = Employee
        fields = [ 'pk', 'employer_name', 'user', 'role',  'dob',  'phone_number', 'id_number', 'kra_pin']


# -------- Company assets ----------------
class CompanyAssetSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = CompanyAsset
        fields = [ 'pk','asset_name', 'available', 'tasks']


# ------  Company Inventory -------------

#------------ Time Off ---------------------
class TimeOffSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Employer.objects.all(),  many=False)  
  
    class Meta:
        model = TimeOff
        fields = [ 'pk','user', 'start', 'end', 'comments']


#------------- Company Inventory  ----------------------
class CompanyInventorySerializer(serializers.HyperlinkedModelSerializer):
    emp_id = serializers.PrimaryKeyRelatedField(queryset=CompanyInventory.objects.all(),  many=False)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=CompanyInventory.objects.all(),  many=False) 
    asset_id =  serializers.PrimaryKeyRelatedField(queryset=CompanyInventory.objects.all(),  many=False) 
  
 
    class Meta:
        model = CompanyInventory
        fields = [ 'pk', 'emp_id', 'employee_id', 'asset_id', 'taking', 'returning', 'returned']



 

 
class EmployeeeSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
    class Meta:
        model = Employees
        fields = (
            'pk',
            'emp_id',
            'name',
            'gender',
            'designation',
            'tasks')
  
  
class EmployeeTaskSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    employee = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all(), many=False)     
  
    class Meta:
        model = EmployeeTask
        fields = (
            'pk',
            'task_name',
            'employee',
            'task_desc',
            'created_date',
            'deadline')
        