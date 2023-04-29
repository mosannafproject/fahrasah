from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count 
from django.contrib import messages
from .forms import EditProjectForm, EditPageForm, EditFieldForm

# Create your views here.

def all_projects(request):

    projects = Project.objects.all()
    pages = Page.objects.all() 

    context = {
        'projects': projects,
        'pages': pages, 
    }

    return render(request, 'fahrasah/all-projects.html', context)

def project(request, id): 
    
    project = Project.objects.get(id=id)
    
    pages = Page.objects.filter(project=project)

    fields = Field.objects.filter(project=project)



    context = {
        'project': project, 
        'pages': pages,
        'fields': fields, 
    } 

    return render(request, 'fahrasah/single-project.html', context)


def del_project(request, id):
    
    project = Project.objects.get(id=id) 
    project.delete()


    return redirect('/')


def del_page(request, id):
    page = Page.objects.get(id=id) 

    page.delete() 

    return redirect(request.META.get('HTTP_REFERER', '/'))

def del_duplicated_projects(request, field): 

    duplicates = Project.objects.values(field).annotate(count=Count('id')).filter(count__gt=1) 
    
    for duplicate in duplicates:
        items = Project.objects.filter(title=duplicate["title"]).order_by('id')
        items.exclude(id=items.first().id).delete() 

    return redirect('/')


def del_duplicated_pages(request, id): 

    project = Project.objects.get(id=id) 
    project_id = project.id 

    duplicates = Page.objects.filter(project=project).values("name").annotate(count=Count('id')).filter(count__gt=1) 
    
    for duplicate in duplicates:
        items = Page.objects.filter(project=project).filter(name=duplicate["name"]).order_by('id')
        items.exclude(id=items.first().id).delete() 

    # return redirect(f'/{project.id}')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def del_duplicated_fields(request, id): 

    project = Project.objects.get(id=id) 
    project_id = project.id 

    duplicates = Field.objects.filter(project=project).values("name").annotate(count=Count('id')).filter(count__gt=1) 
    
    for duplicate in duplicates:
        items = Field.objects.filter(project=project).filter(name=duplicate["name"]).order_by('id')
        items.exclude(id=items.first().id).delete() 

    # return redirect(f'/{project.id}')
    return redirect(request.META.get('HTTP_REFERER', '/'))



def add_project(request): 
    fields = WebsiteField.objects.all() 
    activities = WebsiteActivity.objects.all()

    if request.POST: 
        project_name = request.POST.get('project_name') 
        website_name = request.POST.get('website_name') 
        start_date = request.POST.get('start_date') 
        end_date = request.POST.get('end_date') 
        field = request.POST.get('field')
        field = WebsiteField.objects.get(name=str(field)) 

        activity = request.POST.get('project_activity')
        try:
            activity = WebsiteActivity.objects.get(name=str(activity))
        except: 
            activity = None 
        
        Project.objects.create(title=project_name, website_name=website_name, website_field=field, website_activity=activity, start_date=start_date, end_date=end_date)    

        messages.success(request, 'تمت إضافة المشروع بنجاح')

    

    context = {
        'fields': fields,
        'activities': activities
    } 
    return render(request, 'fahrasah/add-project.html', context)



def add_page(request, project_id):
    project = Project.objects.get(id=project_id)
    pages = Page.objects.filter(project=project) 


    if request.POST:
        page_name = request.POST.get('page_name') 
        page_reference = request.POST.get('page_reference') 
        page_url = request.POST.get('page_url') 

        Page.objects.create(project=project, name=page_name, reference=page_reference, url=page_url) 

        messages.success(request, 'تمت إضافة الصفحة بنجاح')


    context = {
        'project': project, 
        'pages': pages
    }
    return render(request, 'fahrasah/add-page.html', context)



def add_field(request, project_id):
    project = Project.objects.get(id=project_id)
    pages = Page.objects.filter(project=project)

    

    fields = Field.objects.filter(project=project) 
    databases = Database.objects.all()  


    if request.POST: 
        field_name = request.POST.get('field_name') 
        field_description = request.POST.get('field_description')
        field_reference = request.POST.get('field_reference') 
        field_page = request.POST['field_page'] 
        page_obj = Page.objects.filter(project=project).get(name=field_page)
        field_url = request.POST.get('field_url') 
        field_cmd = request.POST.get('field_cmd') 
        field_database = request.POST.get('field_database') 
        field_database = Database.objects.get(name=field_database)

        Field.objects.create(project=project, name=field_name, description=field_description, reference=field_reference, database=field_database, page=page_obj, url=field_url, cmd=field_cmd)

        messages.success(request, "تمت إضافة الحقل بنجاح") 
        
        

    context = {
        'project': project, 
        'fields': fields,
        'pages': pages, 
        'databases': databases,
    }
    return render(request, 'fahrasah/add-field.html', context)


def del_field(request, id):
    Field.objects.get(id=id).delete() 

    return redirect(request.META.get('HTTP_REFERER', '/'))


def edit_project(request, id): 
    project = Project.objects.get(id=id) 
    form = EditProjectForm(instance=project)

    if request.POST:
        form = EditProjectForm(request.POST, instance=project) 
        form.save() 

        messages.success(request, 'تم حفظ التعديلات بنجاح')




    context = {
        'form': form, 
    }
    return render(request, 'fahrasah/edit-project.html', context)


def edit_page(request, id):
    page = Page.objects.get(id=id)

    form = EditPageForm(instance=page) 


    if request.POST:
        form = EditPageForm(request.POST, instance=page) 
        form.save() 

        messages.success(request, 'تم حفظ التعديلات بنجاح')



    context = {
        'form': form, 
    }

    return render(request, 'fahrasah/edit-page.html', context)


def edit_field(request, id):
    field = Field.objects.get(id=id) 

    form = EditFieldForm(instance=field) 
    

    if request.POST:
        form = EditFieldForm(request.POST, instance=field)

        if form.is_valid(): 
            form.save() 
        
        
        messages.success(request, 'تم حفظ التعديلات بنجاح')


    context = {
        'form': form, 
    } 

    return render(request, 'fahrasah/edit-field.html', context)



def remove_repeated_text(request):

    duplicates = RemoveDuplicate.objects.all() 



    context = { 
        'duplicates': duplicates
    }
    return render(request, 'fahrasah/remove-repeated-text.html', context)