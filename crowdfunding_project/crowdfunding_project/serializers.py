from rest_framework import serializers
from users.forms import User
from projects.models import Project,Comment,Tag,ProjectImage,Categories





class CommentSerializer ( serializers.ModelSerializer ) :
    class Meta : 
        model = Comment
        fields = ( 'id' , 'comment' ) 





class CategorySerializer ( serializers.ModelSerializer ) :
    class Meta : 
        model = Categories
        fields = ( 'category', ) 
    
    def create ( self , validated_data ) :
            project_id = validated_data.pop ( "project_id" ) 
            category=Categories.objects.create ( ** validated_data ) 
            category.project_id =project_id 
            category.save ( )
            return category


class ProjectSerializer ( serializers.ModelSerializer ) :
    comment = CommentSerializer ( read_only = True ) 
    comment_id = serializers.IntegerField ( write_only = True )
    category = CategorySerializer ( read_only = True ) 
    category_id = serializers.IntegerField ( write_only = True )


    
    class Meta : 
        model = Project
        fields = ( 'id' , 'title' ) 
        extra_kwargs = {'Tags': {'required': False}}

    def create ( self , validated_data ) :
        extra_kwargs = validated_data.pop ( "Tags" ) 
        project=Project.objects.create ( ** validated_data )
        project=super.save ( )
        project.Tags.set([extra_kwargs] )
        project.save ( )
        return project



    


class UserSerializer ( serializers.ModelSerializer ) :
        project = ProjectSerializer ( read_only = True ) 
        project_id = serializers.IntegerField ( write_only = True )

        class Meta :
            model = User 
            fields = ( 'id' ,"First_name","Last_name","Email","password", "confirm_password","mobile_phone","project_id")

        def create ( self , validated_data ) :
            project_id = validated_data.pop ( "project_id" ) 
            user=User.objects.create ( ** validated_data ) 
            user.project_id =project_id 
            user.save ( )
            return user



class TagSerializer(serializers.ModelSerializer):
    project = ProjectSerializer ( read_only = True ) 
    project_id = serializers.IntegerField ( write_only = True )
    class Meta:
        model = Tag
        fields = ("name", )
        extra_kwargs = {'projects': {'required': False}}



class ImageSerializer(serializers.ModelSerializer):
    project = ProjectSerializer ( read_only = True ) 
    project_id = serializers.IntegerField ( write_only = True )
    class Meta:
        model = ProjectImage
        fields = ("project","images" )