from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post, OnoffValue, ValueOfSpliteData
from django.contrib.auth.models import Group
# Create your views here.
from .forms import  AddDataForSplite, FormOnoff


from django.shortcuts import get_object_or_404
from django.http import (JsonResponse, HttpResponse, HttpRequest)


def sign_up1(request, my_id,  rvolt, rcurrent, yvolt, ycurrent,  bvolt, bcurrent , battery):
    print("Sign up 1")
    if request.method == 'GET':
        print(request.method)
        # pi = get_object_or_404(OnoffValue, pk=my_id)
        try:
            pst = ValueOfSpliteData(id=my_id, rvolt=rvolt,rcurrent=rcurrent,yvolt=yvolt,ycurrent=ycurrent,bvolt=bvolt,bcurrent=bcurrent,battery=battery)
            pst.save()

        except:
            pass



        try:
            pi = OnoffValue.objects.get(pk=my_id)
        except:
            data = OnoffValue(id=my_id,ronoff='0', yonoff='0', bonoff='0')
            data.save()
            pi = OnoffValue.objects.get(pk=my_id)
            print(pi)
        return render(request, 'blog/deviceresponce.html',{'form': pi}) 
        

# ========================================================================================

def showdata(request):
    if request.user.is_authenticated:
        posts = ValueOfSpliteData.objects.all()
        return render(request, 'blog/showsplitdata.html', {'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

def showdataindividual_data(request, my_id):
    if request.user.is_authenticated:
        id = my_id
        posts = ValueOfSpliteData.objects.all()
        pi = ValueOfSpliteData.objects.get(pk=id)
        return render(request, 'blog/showdataindividual.html', {'posts':posts, 'onlydata': pi})
    else:
        return HttpResponseRedirect('/login/')
# ===============================================================================================
def ron_data(request, my_id, my_value):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'GET':
            print(request.method)
            
            try:
                print("try")
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=my_value, yonoff=student.yonoff, bonoff=student.bonoff)
                pst.save()
            except:
                print("except")
                data = OnoffValue(id=my_id,ronoff='0', yonoff='0', bonoff='0')
                data.save()
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=my_value, yonoff=student.yonoff, bonoff=student.bonoff)
                pst.save()
            return HttpResponseRedirect('/showdataindividual/'+ str(my_id) + '/')
    else:
        return HttpResponseRedirect('/login/')

def roff_data(request, my_id, my_value):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'GET':
            
            try:
                print("try")
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=my_value, yonoff=student.yonoff, bonoff=student.bonoff)
                pst.save()
            except:
                print("except")
                data = OnoffValue(id=my_id,ronoff='0', yonoff='0', bonoff='0')
                data.save()
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=my_value, yonoff=student.yonoff, bonoff=student.bonoff)
                pst.save()
            return HttpResponseRedirect('/showdataindividual/'+ str(my_id) + '/')
    else:
        return HttpResponseRedirect('/login/')

# ===============================================================================================
def yon_data(request, my_id, my_value):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'GET':
            print(request.method)
            
            try:
                print("try")
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=my_value, bonoff=student.bonoff)
                pst.save()
            except:
                print("except")
                data = OnoffValue(id=my_id,ronoff='0', yonoff='0', bonoff='0')
                data.save()
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=my_value, bonoff=student.bonoff)
                pst.save()
            
            return HttpResponseRedirect('/showdataindividual/'+ str(my_id) + '/')
    else:
        return HttpResponseRedirect('/login/')

def yoff_data(request, my_id, my_value):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'GET':
            
            try:
                print("try")
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=my_value, bonoff=student.bonoff)
                pst.save()
            except:
                print("except")
                data = OnoffValue(id=my_id,ronoff='0', yonoff='0', bonoff='0')
                data.save()
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=my_value, bonoff=student.bonoff)
                pst.save()
            return HttpResponseRedirect('/showdataindividual/'+ str(my_id) + '/')
    else:
        return HttpResponseRedirect('/login/')


# ===============================================================================================
def bon_data(request, my_id, my_value):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'GET':
            print(request.method)
            
            try:
                print("try")
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=student.yonoff, bonoff=my_value)
                pst.save()
            except:
                print("except")
                data = OnoffValue(id=my_id,ronoff='0', yonoff='0', bonoff='0')
                data.save()
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=student.yonoff, bonoff=my_value)
                pst.save()
            return HttpResponseRedirect('/showdataindividual/'+ str(my_id) + '/')
    else:
        return HttpResponseRedirect('/login/')

def boff_data(request, my_id, my_value):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'GET':
            
            try:
                print("try")
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=student.yonoff, bonoff=my_value)
                pst.save()
            except:
                print("except")
                data = OnoffValue(id=my_id,ronoff='0', yonoff='0', bonoff='0')
                data.save()
                student = OnoffValue.objects.get(pk=my_id)
                pst = OnoffValue(id=my_id, ronoff=student.ronoff, yonoff=student.yonoff, bonoff=my_value)
                pst.save()
            return HttpResponseRedirect('/showdataindividual/'+ str(my_id) + '/')
    else:
        return HttpResponseRedirect('/login/')
    
# Home
def home(request):
    if not request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {'posts':posts, 'active': 'active'})
    else:
        return HttpResponseRedirect('/dashboard/')

# About
def about(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/about.html', {'active': 'active'})
    else:
        return HttpResponseRedirect('/dashboard/')
        

# contact
def contact(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/contact.html', {'active':'active'})
    else:
        return HttpResponseRedirect('/dashboard/')

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip', 0)
        return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':gps,'ip': ip, 'active':'active'})
    else:
        return HttpResponseRedirect('/login/')

# user_logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

# user_signup
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Congratulations!! You have become an Author.')
                form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                form = SignUpForm()
        else:
            form = SignUpForm()
        return render(request, 'blog/signup.html' , {'form': form, 'active':'active'})
    else:
        return HttpResponseRedirect('/showdata/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/showdata/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form, 'active':'active'})
    else:
        return HttpResponseRedirect('/showdata/')

# add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form, 'active':'active'})
    else:
        return HttpResponseRedirect('/login/')

# update post
def update_post(request, id ):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form, 'active':'active'})
    else:
        return HttpResponseRedirect('/login/')

# delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')