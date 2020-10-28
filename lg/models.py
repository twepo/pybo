from django.db import models

from django.contrib.auth.models import User

# Create your models here.




class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)
    new_test = models.CharField(default='NEW_TEST', max_length=50)

    def __str__(self):
        return self.todo


class Category(models.Model):
    eng_name = models.CharField(max_length=100)
    kor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.eng_name


class Channel(models.Model):
    eng_name = models.CharField(max_length=100)
    kor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.eng_name


class Campaign(models.Model):


    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='camp_user')

    company_name = models.CharField(max_length=100)
    company_tel = models.CharField(max_length=30)
    company_email = models.CharField(max_length=100)

    channel_title = models.CharField(max_length=20)
    channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING, related_name='camp_channel',null=True)


    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)

    category_title = models.CharField(max_length=20,null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='camp_category',null=True)


    camp_local = models.CharField(max_length=20,null=True)
    camp_address = models.CharField(max_length=200,null=True)
    camp_type = models.CharField(max_length=20,null=True)

    content_offer = models.TextField()
    content_keyword = models.TextField()
    content_guide = models.TextField()
    content_caution = models.TextField()

    quantity = models.PositiveSmallIntegerField(default=0)
    created_time= models.DateTimeField(null=True,blank=True)
    start_date= models.DateTimeField(null=True,blank=True)
    end_date= models.DateTimeField(null=True,blank=True)
    win_date= models.DateTimeField(null=True,blank=True)

    img_path = models.CharField(max_length=200,null=True)
    img_array = models.CharField(max_length=250,null=True)

    lat = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6,null=True)

    apply = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title
