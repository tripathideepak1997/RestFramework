from django.contrib import admin
from django.urls import path
from app1.views import question_detail,question_list, choices_detail, choices_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/',question_list),
    path('question/<int:pk>',question_detail),
    path('choices/',choices_list),
    path('choices/<int:pk>',choices_detail)
]