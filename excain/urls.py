from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    # path('admin/',include('dashboard.urls')),
    path("", include("accounts.urls")),
    path('djrichtextfield/', include('djrichtextfield.urls'))
]
