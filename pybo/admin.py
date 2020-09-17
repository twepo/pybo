from django.contrib import admin

# Register your models here.


from .models import *



class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']



admin.site.register(Question,QuestionAdmin)

admin.site.register(Book)
admin.site.register(Store)


admin.site.register(Department)
admin.site.register(Employee)


