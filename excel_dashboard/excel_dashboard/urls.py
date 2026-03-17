from excel_dash_app.views import fileview , brandsview
from django.contrib import admin
from django.urls import path , include
from rest_framework import routers  

router = routers.DefaultRouter()
router.register(r'brands', brandsview, basename='brand')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', fileview.as_view(), name='file-upload'),
    path('api/', include(router.urls)),

]
