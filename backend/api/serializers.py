from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "projectmanager",
            "start_date",
            "end_date",
            "comments",
            "status",
        )


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = ("name", "id")

#------------------------------------------------------------------------------------ for print data
# print if is't suc   #  Project ， ID  1
project_instance = Project.objects.get(
    pk=1
)  
project_serializer = ProjectSerializer(instance=project_instance)
print(project_serializer.data,"aa")


#  ProjectManagerSerializer  #  ProjectManager instance，ID 1
project_manager_instance = ProjectManager.objects.get(
    pk=1
)
project_manager_serializer = ProjectManagerSerializer(instance=project_manager_instance)
print(project_manager_serializer.data,"bb")
