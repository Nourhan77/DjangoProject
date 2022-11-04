from unicodedata import name
from rest_framework.response import Response
from django.shortcuts import render,redirect , get_object_or_404


from .forms import ImageForm, ProjectForm ,CommentForm, TagForm
from .models import Categories, Project,Comment, ProjectImage
from users.models import User

def donate (request,project_id):
    project=get_object_or_404(Project,pk=project_id)
    user=get_object_or_404(User,pk=project.user_id)
    project.total_target = project.total_target + float(request.POST.get('donate0')or 0)
    project.avg_rate = (project.avg_rate + float(request.POST.get('rating') or 0 ))/2
    user.donations= user.donations + float(request.POST.get('donate0') or 0)
    user.save()
    project.save()
    comments=Comment.objects.filter(project=project.id)
    context={
        "project":project,
        "comments":comments

    }
    return render (request,"projects/Proj_details.html",context)



def reportComment(request,project_id,comment_id):

    comment=get_object_or_404(Comment,pk=comment_id)
    comment.reported=True
    comment.project.reported=True
    project=comment.project
    comment.save()
    project.save()
    comments=Comment.objects.filter(project=project.id)
   
    context={
        "project":project,
        "comments":comments
    }
    print(comment.project.reported)
    return render (request,"projects/Proj_details.html",context)


def categorypProjects (request,category):

    projects=Project.objects.filter(category=category)
    context={
        "projects":projects
    }
    return render (request,"projects/categoryProjects.html",context)



def searchedProjects (request,user_id):
    ptag=request.POST.get('ptag')
    ptitle=request.POST.get('ptitle')
    projects=Project.objects.all()
    # print("Project",projects[0].Tags.values()[1]["name"])
    for project in projects:
        if ptag:
            for key in project.Tags.values():
                if  ptag == key["name"]:
                    projects=Project.objects.filter( Tags__iexact=key["id"])
                
        
        elif ptitle:

            projects=Project.objects.filter(title__iexact=ptitle)


    context={
        "projects":projects,

        "user_id":user_id
    }

    return render (request,"projects/searchedProjects.html",context)


def allProjects (request,user_id):
    
    projects=Project.objects.all()
    context={
        "projects":projects,
        "user_id":user_id
    }
    return render (request,"projects/allProjects.html",context)




def CreateProject (request,user_id):
    user=get_object_or_404(User,pk=user_id)
    if request.method=="POST":
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user=user
            project=form.save()
            # print(request.POST['Tags'])
            # project.save()
            print(project)
            return redirect('Proj_details',project_id=project.id)
    else:
        form = ProjectForm()
    return render (request ,'projects/project_form.html' , {'user_id':user_id,'form':form})





def DeleteProject(request,project_id):
    project=get_object_or_404(Project,pk=project_id)
    if request.method=="POST":
        if project:
            project.delete()
            return redirect ('home')
    return render (request ,'projects/delete.html',{'project_id':project.id})






def CreateComment (request,project_id):
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=request.POST.get('comment')
            project=get_object_or_404(Project,pk=project_id)
            form.instance.project=project
            form.instance.comment=comment
            form.save()
           
            return redirect ("Proj_details",project_id=project.id)
    else:
        form = CommentForm()
    return render (request ,'projects/comment.html' , {'form':form})


def uploadimages(request,project_id):
    if request.method=="POST": 
        project=get_object_or_404(Project,pk=project_id)
        name=project.title
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=request.FILES.get('images')
            form.instance.project=project
            form.instance.images=image
            form.instance.name=name            
            form.save()
            project.image=image
            project.save()
            photos = ProjectImage.objects.filter(project=project.id)

            # print("Photo",photos[0], name,type(photos))

            return redirect ("Proj_details",project_id=project.id)
    else:
        form = ImageForm()
    return render (request ,'projects/photos.html' , {'form':form})



def details (request,project_id):

    project=Project.objects.get(id=project_id)
    comments=Comment.objects.filter(project=project.id)
    photos = ProjectImage.objects.filter(project=project.id)
    context={
        "project":project,
        "comments":comments,
        "photos":photos
    }
    return render (request,"projects/Proj_details.html",context)




def home(request,user_id):
    highest_projects= Project.objects.order_by('-avg_rate')[:5]
    latest_projects= Project.objects.order_by('avg_rate')[:5]
    categories=Categories.objects.all()

    context={
        "highest_projects":highest_projects,
        "latest_projects":latest_projects,
        "categories":categories,
        "user_id":user_id
    }
    return render(request,"projects/home.html",context)




