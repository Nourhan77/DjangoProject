from django.urls import path
from .views import editUser, login_user, register,profile,CreateTag

urlpatterns = [
   path('Register', register, name='Register'),
   path('profile/<int:user_id>', profile, name="profile"),
   path('login', login_user, name="login"),
   path('edit/<int:user_id>', editUser, name="edit"),
    path('tag/<int:user_id>', CreateTag, name='tag'),


]
