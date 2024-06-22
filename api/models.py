from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
    User_Types=(
        ('OpsUser','OpsUser'),
        ('Client','Client')
    )
    user_type=models.CharField(max_length=50,choices=User_Types)

    def __str__(self):
        return self.username

def validate_file_extensions(file):
    allowed_types=['pptx','docx','xlsx']
    if file.name.split('.')[-1] not in allowed_types:
        raise ValidationError('Only pptx, docx, and xlsx files are allowed')

class FileUpload(models.Model):
    file=models.FileField(upload_to='uploads/', validators=[validate_file_extensions])
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uploaded_by)



    
    