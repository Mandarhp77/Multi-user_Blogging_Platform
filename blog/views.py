from django.shortcuts import render, redirect
from . models import Post, Details
from django.core.files.storage import FileSystemStorage
#from . forms import ImageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
#from PIL import image

user_name = ""
def writer(request):
    global user_name
    print(user_name)
    if request.method == "POST" and request.FILES["image_file"]:
        title = request.POST['title']
        category = request.POST['category']
        category = category.title()
        content = request.POST['description']
        image = request.FILES["image_file"]

        fs = FileSystemStorage()
        url = fs.url(image)
        #form = ImageForm(request.POST, request.FILES)
        post = Post(title=title, category=category, content=content, image=url, username = user_name)
        #form.save()
        post.save()
        
        return redirect("writer")
    return render(request, 'writer.html')

def reader(request):
    data = Post.objects.all()
    cat = []

    for row in data:
        if row.category in cat:
            pass
        else:
            cat.append(row.category)
      
    return render(request, 'reader.html',{"data":data, "cat":cat})

def user(request):
    return render(request, "user.html")

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        sirname = request.POST['sirname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')

        new_user = Details(name=name, sirname=sirname, username=username, email= email)
        new_user.save()
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = name
        myuser.last_name = sirname
        myuser.email = email
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!" )       
        return redirect('user')
    return render(request, 'register.html')

def login(request):
    global user_name
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user_name, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "writer.html", {"username":user_name})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('user')
    return render(request, 'login.html')

def logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def search_cat(request):
    if request.method == "POST":
        cat = request.POST['category']
        cat_post = Post.objects.filter(category=cat)
        return render(request, "category.html", {"cat":cat_post})
    
    return render(request, "category.html")

def search_user(request):
    if request.method == "POST":
        username = request.POST['user_name']
        user_post = Post.objects.filter(username=username)
        return render(request, "category.html", {"cat":user_post})
    
    return render(request, "category.html")
    
def blog(request):
    if request.method == "POST":
        blog_name = request.POST['blog_name']
        print(blog_name)
        blog =  Post.objects.filter(title=blog_name)
        return render(request, "blog.html", {"blog":blog})
    
    return render(request, "blog.html")

