from django.shortcuts import render, redirect
from .models import categorydb, bookdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import contactdb

# Create your views here.
def index_page(request):
    category = categorydb.objects.count()
    books = bookdb.objects.count()

    return render(request,"index.html",{'category':category,'books':books})
def add_category(request):
    return render(request,"add_category.html")
def add_category_data(request):
    if request.method == "POST":
        a = request.POST.get("name")
        b = request.POST.get("description")
        c = request.FILES["cover_image"]
        obj = categorydb(cat_name=a,cat_description=b,cat_cover_image=c)
        obj.save()
        return redirect(add_category)
def display_category(request):
    data = categorydb.objects.all()
    return render(request,"display_category.html",{'data':data})
def edit_category(request,category_id):
    category = categorydb.objects.get(id=category_id)
    return  render(request,"edit_category.html",{'category':category})
def update_category(request,cat_id):
    if request.method == "POST":
        a = request.POST.get("name")
        b = request.POST.get("description")
        try:
            img = request.FILES['cover_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=cat_id).cat_cover_image
        categorydb.objects.filter(id=cat_id).update(cat_name=a,cat_description=b,cat_cover_image=file)
        return redirect(display_category)
def delete_category(request,c_id):
    category = categorydb.objects.filter(id=c_id)
    category.delete()
    return redirect(display_category)



def add_books(request):
    categories = categorydb.objects.all()
    return render(request,"add_books.html",{'categories':categories})
def add_books_data(request):
    if request.method == "POST":
        a = request.POST.get("title")
        b = request.POST.get("author")
        c = request.POST.get("category")
        d = request.POST.get("price")
        e = request.POST.get("publisher")
        f = request.POST.get("description")
        g = request.FILES["cover_image"]
        obj = bookdb(book_title=a,book_author=b,book_category=c,book_price=d,book_publisher=e,book_description=f,book_cover_image=g)
        obj.save()
        return redirect('add_books')
def display_books(request):
    data = bookdb.objects.all()
    return render(request,"display_books.html",{'data':data})
def edit_books(request,book_id):
    books = bookdb.objects.get(id=book_id)
    categories = categorydb.objects.all()
    return render(request,"edit_books.html",{'books':books,'categories':categories})
def update_books(request,book_id):
    if request.method == "POST":
        a = request.POST.get("title")
        b = request.POST.get("author")
        c = request.POST.get("category")
        d = request.POST.get("price")
        e = request.POST.get("publisher")
        f = request.POST.get("description")
        try:
            img = request.FILES['cover_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = bookdb.objects.get(id=book_id).book_cover_image
        bookdb.objects.filter(id=book_id).update(book_title=a,book_author=b,book_category=c,book_price=d,book_publisher=e,book_description=f,book_cover_image=file)
        return redirect(display_books)
def delete_books(request,b_id):
    book = bookdb.objects.filter(id=b_id)
    book.delete()
    return redirect(display_books)

def login_Admin(request):
    return render(request,"Login.html")

def login_admin_data(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pswd = request.POST.get("password")
        if User.objects.filter(username__contains = un).exists():
            data = authenticate(username=un,password=pswd)
            if data is not None:
                login(request, data)
                request.session['username']=un
                request.session['password']=pswd
                return redirect(index_page)
            else:
                return redirect(login_Admin)
        else:
            return redirect(login_Admin)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_Admin)

def view_contact_data(request):
    data = contactdb.objects.all()
    return render(request,"view_contact_data.html",{'data':data})
def delete_message(request,message_id):
    message = contactdb.objects.filter(id=message_id)
    message.delete()
    return redirect(view_contact_data)









