from django.contrib import admin

# Register your models here.
from .models import * 


admin.site.register(RemoveDuplicate) 

admin.site.register(Project)
admin.site.register(Page) 
admin.site.register(Field) 
admin.site.register(Database) 


admin.site.register(WebsiteField) 
admin.site.register(WebsiteActivity)
