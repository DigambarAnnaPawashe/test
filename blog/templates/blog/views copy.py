from django.shortcuts import render
from .forms import FormHome, ValueOfSpliteData, FormOnoff
from django.shortcuts import render, HttpResponseRedirect
from .models import OnoffValue




def sign_up(request):
    if request.method == 'GET':
        fm = FormHome(request.GET)
        if fm.is_valid():
            uname = fm.cleaned_data['id']
            x,y,a,s,i,q,w,e = uname.split("a")
            
            print('id:', x)
            print('rvolt: ',y)
            print('rcurrent: ',a)
            print('yvolt: ',s)
            print('ycurrent: ',i)
            print('bvolt: ',q)
            print('bcurrent: ',w)
            print('battery: ',e)
            # pst = ValueOfSpliteData()
            pst = ValueOfSpliteData(id=x, rvolt=y,rcurrent=a,yvolt=s,ycurrent=i,bvolt=q,bcurrent=w,battery=e)
            pst.save()
            # fm = OnoffValue.objects.all()
            # pi = OnoffValue.objects.all()
            print('pi befor')
            # pi = OnoffValue.objects.get(pk=int(x))
            print('pi: ')
            print('..................')
            return render(request, 'split/home.html')
            # fm.save()
           
    else:        
        print('**************************')
        fm = FormHome()
    print('_____________________________')
    return render(request, 'split/home.html', {'form':fm})

def showdata(request):
    posts = ValueOfSpliteData.objects.all()
    return render(request, 'split/showsplitdata.html', {'posts':posts})

def showdataindividual_data(request, my_id):
    id = my_id
    posts = ValueOfSpliteData.objects.all()
    pi = ValueOfSpliteData.objects.get(pk=id)
    return render(request, 'split/showdataindividual.html', {'posts':posts, 'onlydata': pi})
    

def on_RYB_data(request, my_id, my_value):
    form = FormOnoff(request.POST)
    title = my_id
    pst = OnoffValue(id=title, onoff=my_value)
    pst.save()
    print('in if save RYB0')
    print()
    return HttpResponseRedirect('/showdata')

def off_RYB_data(request, my_id, my_value):
    form = FormOnoff(request.POST)
    title = my_id
    pst = OnoffValue(id=title, ronoff=my_value)
    pst.save()
    print('save RYB0')
    return HttpResponseRedirect('/showdata')
    
    
    # update post
# def update_post(request, id ):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             pi = Post.objects.get(pk=id)
#             form = PostForm(request.POST, instance=pi)
#             if form.is_valid():
#                 form.save()
#         else:
#             pi = Post.objects.get(pk=id)
#             form = PostForm(instance=pi)
#         return render(request, 'blog/updatepost.html', {'form':form, 'active':'active'})
#     else:
#         return HttpResponseRedirect('/login/')

# add
# def add_post(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 title = form.cleaned_data['title']
#                 desc = form.cleaned_data['desc']
#                 pst = Post(title=title, desc=desc)
#                 pst.save()
#                 form = PostForm()
#         else:
#             form = PostForm()
#         return render(request, 'blog/addpost.html', {'form':form, 'active':'active'})
#     else:
#         return HttpResponseRedirect('/login/')

