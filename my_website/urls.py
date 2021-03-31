from django.urls import path
from my_website import views

app_name = "my_website"

urlpatterns = [
    path('', views.index, name="index"),
    path('skills', views.skills, name="skills"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('work', views.work, name="work"),
    path('<int:pk>', views.project_details, name="project_details"),
]
