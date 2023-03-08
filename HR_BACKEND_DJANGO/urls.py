
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    #------ myapps URLS ------#
    path('', include('hr_system.urls')),
    #path('v1/', include('admin.urls')),


    #Django auth
    path('', auth_views.LoginView.as_view(), name='login'),  #<--to login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #<--to logout
    

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
