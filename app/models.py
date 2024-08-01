from django.db import models

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_image')
    create_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-create_at"]

    def __str__(self) -> str:
            return self.title    
        

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
      ordering = ["-created_at"]

    def __str__(self):
       return self.content
    

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)


class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ["-created_at"]

    def __str__(self):
       return self.email


        