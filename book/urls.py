from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('diary', views.DiaryViewSet)

router.register('book', views.BookViewSet)

urlpatterns = [ 
    path('', include(router.urls)),

]