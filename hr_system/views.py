from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse
#-------   Rest framework dependancies ----------#
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse

# Serialization
from .serializers import *
# Compant asset model
from .models import *
from django.contrib.auth.decorators import login_required

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
#login Api
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)





#============    Register New User  ================#
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Succesfully!"   )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# ---------- Company Dashboards ----------------
@login_required(login_url='register')
def index(request): 
    user = User.objects.all()
    print(user)

    return render(request, 'index.html',{'user':user})


def employee(request): 
       
    return render(request, 'employee.html')

def asset(request): 
       
    return render(request, 'asset.html')

def inventory(request): 
       
    return render(request, 'inventory.html')

def leave(request): 
       
    return render(request, 'leave.html')


#################################  REST API VIEWS #########################

# ---------------------   Employer
# =============  Create and Read ============== 
@csrf_exempt
def employer_list(request):
    if request.method == 'GET':
        emp = Employer.objects.all()
        emp_serializer = EmployerModelSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)
  
    elif request.method == 'POST':
        emp_data = JSONParser().parse(request)
        emp_serializer = EmployerModelSerializer(data=emp_data)
          
        if emp_serializer.is_valid():
            emp_serializer.save()
            return JsonResponse(emp_serializer.data,  status=201)
        return JsonResponse(emp_serializer.errors, status=400)  

# =============  Update and Delete ==============  
@csrf_exempt
def employer_detail(request, pk):
    try:
        emp = Employer.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        emp_serializer = EmployerModelSerializer(emp)
        return JsonResponse(emp_serializer.data)
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)
  
# ---------------------   Employee
# =============  Create and Read ============== 
@csrf_exempt
def employee_view(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        emp_serializer = EmployeeModelSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)
  
    elif request.method == 'POST':
        emp_data = JSONParser().parse(request)
        emp_serializer = EmployeeModelSerializer(data=emp_data)
          
        if emp_serializer.is_valid():
            emp_serializer.save()
            return JsonResponse(emp_serializer.data,  status=201)
        return JsonResponse(emp_serializer.errors, status=400)  

# =============  Update and Delete ==============  
@csrf_exempt
def employee_detail(request, pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        emp_serializer = EmployeeModelSerializer(emp)
        return JsonResponse(emp_serializer.data)
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)

# ---------------------   Company Assets
# =============  Create and Read ============== 
@csrf_exempt
def CompanyAssets_list(request):
   
    print('companyassets')
    if(request.method == 'GET'):
        # get all the tasks
        tasks = CompanyAsset.objects.all()
        # serialize the task data
        serializer = CompanyAssetSerializer(tasks, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = CompanyAssetSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

# =============  Update and Delete ============== 
@csrf_exempt
def companyasset_detail(request, pk):
    try:
        emp = CompanyAsset.objects.get(pk=pk)
    except CompanyAsset.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        emp_serializer = CompanyAssetSerializer(emp)
        return JsonResponse(emp_serializer.data)
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)
      

# ---------------------   Company Inventory
# =============  Create and Read ============== 
@csrf_exempt
def CompanyInventoy_list(request):
   
    print('companyassets')
    if(request.method == 'GET'):
        # get all the tasks
        tasks = CompanyInventory.objects.all()
        # serialize the task data
        serializer = CompanyInventorySerializer(tasks, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = CompanyInventorySerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
# =============  Update and Delete ============== 
@csrf_exempt
def CompanyInventory_detail(request, pk):
    try:
        emp = CompanyInventory.objects.get(pk=pk)
    except CompanyInventory.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        emp_serializer = CompanyInventorySerializer(emp)
        return JsonResponse(emp_serializer.data)
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)
      
# ---------------------   Time Off
# =============  Create and Read ============== 
@csrf_exempt
def TimeOff_list(request):
   
    print('companyassets')
    if(request.method == 'GET'):
        # get all the tasks
        tasks = TimeOff.objects.all()
        # serialize the task data
        serializer = TimeOffSerializer(tasks, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = TimeOffSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
# =============  Update and Delete ============== 
@csrf_exempt
def TimeOff_detail(request, pk):
    try:
        emp = TimeOff.objects.get(pk=pk)
    except TimeOff.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        emp_serializer = TimeOffSerializer(emp)
        return JsonResponse(emp_serializer.data)
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)
      


