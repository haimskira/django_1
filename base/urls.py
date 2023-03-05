from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/',views.tasks ),
    path('tasks/<int:id>',views.tasks),
    path('student/',views.student_view ),
    path('student/<int:id>',views.student_view),
    path('login/', views.MyTokenObtainPairView.as_view()),
]
