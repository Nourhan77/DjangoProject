from django import forms
from .models import Project,Comment, ProjectImage,Tag


class ProjectForm (forms.ModelForm):
    class Meta:
        model =Project
        fields=("title","details","category","Tags", "sdate","edate","rate","donate","total_target",'reported')


class CommentForm (forms.ModelForm):
    class Meta:
        model =Comment
        fields=('comment','reported')


class TagForm (forms.ModelForm):
    class Meta:
        model =Tag
        fields=('name',)



class ImageForm (forms.ModelForm):
    class Meta:
        model =ProjectImage
        fields=('images','project')