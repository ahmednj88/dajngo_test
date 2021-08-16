from django.db import models

# Create your models here.
class posts(models.Model):
      title = models.TextField(null=True)
      def __str__(self):
            return self.title

class employeemodels(models.Model):
      name=models.TextField()
      age=models.IntegerField()
      post=models.ForeignKey(posts,related_name='post_id' ,on_delete=models.CASCADE)
      def __str__(self):
          return self.name

class company(models.Model):
      name=models.TextField()
      employees=models.ForeignKey(employeemodels,on_delete=models.CASCADE)
