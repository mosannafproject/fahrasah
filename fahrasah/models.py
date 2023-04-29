from django.db import models

import arabic_reshaper 
from bidi.algorithm import get_display 

# Create your models here.
class RemoveDuplicate(models.Model):


    text = models.TextField(verbose_name='النص الأصلي')

    repeated_text = models.TextField(verbose_name='النص المعدل (يتم توليده تلقائياً)', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        results = []
        for word in self.text.split(" "):
            if not word in results:
                results.append(word)
        results = arabic_reshaper.reshape(" ".join(results))
        self.repeated_text = results 
        super(RemoveDuplicate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'حذف مكرر'
        verbose_name_plural = "حذف المكرر"




class WebsiteField(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم المجال") 

    def __str__(self):
        return self.name  


    class Meta:
        verbose_name = "مجال موقع"
        verbose_name_plural = "مجال موقع" 


class WebsiteActivity(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم النشاط")

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = "نشاط موقع"
        verbose_name_plural = "نشاط موقع" 


class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name="اسم المشروع") 
    website_name = models.CharField(max_length=200, verbose_name="اسم الموقع") 
    website_field = models.ForeignKey(WebsiteField, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="مجال المشروع") 
    website_activity = models.ForeignKey(WebsiteActivity, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="نشاط المشروع") 
    start_date = models.DateField(auto_now_add=False, verbose_name="تاريخ بداية المشروع")
    end_date = models.DateField(verbose_name="الموعد النهائي المتوقع")

    def __str__(self):
        return self.title 
    

class Page(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="المشروع")
    name = models.CharField(max_length=200, verbose_name="اسم الصفحة") 
    reference = models.CharField(max_length=200, verbose_name="مرجع الصفحة") 
    url = models.URLField(verbose_name="رابط الصفحة")
    
    def __str__(self):
        # return f"{self.project} | {self.name}"
        return self.name 

class Field(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="اسم الحقل")
    description = models.CharField(max_length=255, verbose_name="وصف الحقل")
    reference = models.CharField(max_length=200, verbose_name="مرجع الحقل") 
    database = models.ForeignKey("Database", on_delete=models.SET_NULL, null=True, blank=True, verbose_name='قاعدة البيانات')
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الصفحة")
    # page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الصفحة", limit_choices_to=lambda qs: qs.filter(project="project"))
    # page = models.CharField(max_length=250, verbose_name="الصفحة", choices=PAGE_CHOICES)
    url = models.CharField(max_length=250, verbose_name="رابط الحقل", null=True, blank=True)
    cmd = models.CharField(max_length=255, verbose_name="سطر الأمر")

    def __str__(self):
        return f"{self.project} | {self.name}" 
    

class Database(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم قاعدة البيانات")

    def __str__(self):
        return self.name 
    