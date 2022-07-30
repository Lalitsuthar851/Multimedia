from django.db import models

# Create your models here.
from django.db import models


class notes_storage(models.Model):
    Id = models.AutoField(primary_key=True, unique=True)
    Date = models.DateTimeField(auto_now_add= True)
    Title = models.CharField(max_length=50)
    Text = models.TextField(null=True)

    def __str__(self):
        return self.Title


# Create your models here.

