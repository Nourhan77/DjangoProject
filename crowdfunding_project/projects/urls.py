from unicodedata import category
from django.contrib import admin
from django.urls import path 
from .views import  uploadimages,CreateComment, CreateTag, DeleteProject, categorypProjects, donate ,CreateProject,details, home, reportComment, searchedProjects

urlpatterns = [
 path('total/<int:project_id>', donate, name='total'),
 path('project_form/<int:user_id>', CreateProject, name='project_form'),
 path('Proj_details/<int:project_id>', details, name="Proj_details"),
 path('comment/<int:project_id>', CreateComment, name='comment'),
 path('delete/<int:project_id>', DeleteProject, name='project_delete'),
 path('report/<int:project_id>/<int:comment_id>', reportComment, name='report'),
 path('home', home, name='home'),
 path('tag/<int:project_id>', CreateTag, name='tag'),
 path('category/<str:category>', categorypProjects, name='category'),
 path('searchedProjects',searchedProjects, name='searchedProjects'),
path('photos/<int:project_id>', uploadimages, name='photos'),

 ]

