from django.contrib import admin
from projects.models import Project,Comment,Tag,ProjectImage,Categories
from .models import User


# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(ProjectImage)
admin.site.register(Categories)