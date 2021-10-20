from django.shortcuts import render,HttpResponseRedirect
from .forms import usersignupform,userloginform,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html') 

# dash board
def user_dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        User = request.user
        full_name = User.get_full_name()
        gps = User.groups.all()
        return render(request,'blog/dashboard.html',{"posts":posts,'fname':full_name,'groups':gps}) 
    else:
        return HttpResponseRedirect('/signup/')     
#login func function          
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = userloginform(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'loged in succesfully!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = userloginform()
        return render(request,'blog/login.html',{'form':form}) 
    else:
        return HttpResponseRedirect('/dashboard/')    
#signup func          
def user_signup(request):
    if request.method == 'POST':
        form = usersignupform(request.POST)
        if form.is_valid():
            messages.success(request,'congratulation!!! you have become a AUTHOR')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:        
        form = usersignupform()
    return render(request,'blog/signup.html',{'form':form})  
#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')       
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm = PostForm()
        else:
            fm = PostForm()
        return render(request,'blog/addpost.html',{'addform':fm})
    else:
        return HttpResponseRedirect('/login/')   
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)        
        return render(request,'blog/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/') 
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')           
    else:
        return HttpResponseRedirect('/login/')                  
          

