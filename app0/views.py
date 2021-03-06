
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import User
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UserForm
from django.views.generic.edit import DeleteView
from .forms import UserForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q

def index1(request):
    users = User.objects.all()
    template = loader.get_template('app0/index1.html')
    context = {
        'users': users
    }
    return HttpResponse(template.render(context, request=request))


def detail_element(request,user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'user_id':user.id ,
         'user_name':user.name,
         'user_number': user.carNumber,
         'created':user.created_at,
         'phone':user.phone
    }
    return render(request, 'app0/det.html', context)


def delete(request, user_id ,template_name='app0/confirm_delete.html'):
    user= get_object_or_404(User, pk=user_id)   
    if request.method=='POST' and 'yes' in request.POST:
        user.delete()
        return HttpResponseRedirect('/app0/')
    if request.method=='POST' and 'no' in request.POST:
        return HttpResponseRedirect('/app0/')       
    context = {
        'user_id':user.id ,
        'user_name':user.name,
    }
    return render(request, template_name, { 'user_name':user.name},)




def edit(request,user_id, template_name='app0/edit.html'):
    user= get_object_or_404(User,pk=user_id)
    form = UserForm(request.POST or None, user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/app0/')
       
    return render(request, template_name, {'form':form})





def ajouter(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            carNumber = request.POST.get('carNumber')
            user = User.objects.filter(carNumber=carNumber)
            if not user.exists():
                user =User.objects.create(
                     name=name,
                     carNumber= carNumber
                                     )
            messages.success(request,'successfully!')
            return HttpResponseRedirect('/app0/')
        else:
            context = {
               'form': form
             }
            return HttpResponseRedirect('/app0/')
    else:
        form = UserForm()
        context['form'] = form  
    return render(request, 'app0/add.html',context)



def search(request):
    if request.method=='GET':
        search = request.GET.get('s')
        users=User.objects.all().filter(name=search)
        # return HttpResponseRedirect('app0/work.html')
        return render(request, 'app0/list.html' , {'users':users} )        


# def delete(request, user_id ,template_name='app0/confirm_delete.html'):
#     user= get_object_or_404(User, pk=user_id)   
#     if request.method=='POST' and 'yes' in request.POST:
#         user.delete()
#         return HttpResponseRedirect('/app0/')
#     if request.method=='POST' and 'no' in request.POST:
#         return HttpResponseRedirect('/app0/')       
#     context = {
#         'user_id':user.id ,
#         'user_name':user.name,
#     }
#     return render(request, template_name, { 'user_name':user.name},)
# 

# def index1(request):
#     return render(request, 'app0/index1.html')
def users(request):
    return render(request, 'users.html')
def list(request):
    return render(request, 'app0/list.html')

def work(request):
    return render(request, 'app0/work.html')

  