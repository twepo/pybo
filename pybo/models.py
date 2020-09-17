from django.db import models

from django.contrib.auth.models import User

from django.shortcuts import reverse


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()    
    modify_date = models.DateTimeField(null=True,blank=True)


    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    voter = models.ManyToManyField(User, related_name='voter_question')

    # 추천자야.
    
    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('pybo:detail', args=[self.id])
        


class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')

    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True)
    answer = models.ForeignKey(Answer,null=True,blank=True,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,null=True,blank=True,on_delete=models.CASCADE)
    
    # 아..구동방식이. type이 아니라, 클래스유무로 가린다


class Todo(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=124)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
        














class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name



    





        
    
    