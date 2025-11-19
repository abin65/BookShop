from django.shortcuts import render,redirect
from adminapp .models import categorydb, bookdb
from webapp.models import registrationdb, contactdb

# Create your views here.
def home_page(request):
    categories = categorydb.objects.all()
    return render(request,"home.html",{'categories':categories})
def about_page(request):
    categories = categorydb.objects.all()
    return render(request,"about.html",{'categories':categories})
def popular_books(request):
    categories = categorydb.objects.all()
    books = bookdb.objects.all()
    return render(request,"popular_books.html",{'books':books,'categories':categories})
def contact_us(request):
    categories = categorydb.objects.all()
    return render(request,"contact_us.html",{'categories':categories})
def checkout_page(request):
    categories = categorydb.objects.all()
    return render(request,"check_out.html",{'categories':categories})
def filtered_books(request,book_category):
    categories = categorydb.objects.all()
    books = bookdb.objects.filter(book_category=book_category)
    return  render(request,"filtered_books.html",{'books':books,'categories':categories,'book_category':book_category})
def book_details(request,book_id):
    categories = categorydb.objects.all()
    book = bookdb.objects.get(id=book_id)
    return  render(request,"book_details.html",{'books':book,'categories':categories})
def login_user_signin(request):
    return render(request,"login_user.html")
def signup_user(request):
    return render(request,"signup_user.html")
def signup_user_data(request):
    if request.method == "POST":
        a = request.POST.get("user_name")
        b = request.POST.get("password")
        c = request.POST.get("conform_password")
        d = request.POST.get("email")
        obj = registrationdb(reg_user_name=a,reg_password=b,reg_conform_password=c,reg_email=d)
        if registrationdb.objects.filter(reg_user_name=a).exists():
            return redirect(signup_user)
        elif registrationdb.objects.filter(reg_email=d).exists():
            return redirect(signup_user)
        obj.save()
        return redirect(login_user_signin)
def user_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('password')
        if registrationdb.objects.filter(reg_user_name=un,reg_password=pswd).exists():
            request.session['reg_user_name'] = un
            request.session['reg_password'] = pswd
            return redirect(home_page)
        else:
            return redirect(login_user_signin)
    else:
        return redirect(login_user_signin)
def user_logout(request):
    del request.session['reg_user_name']
    del request.session['reg_password']
    return redirect(login_user_signin)
def contact_data_save(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        obj = contactdb(contact_name=name,contact_email=email,contact_subject=subject,contact_message=message)
        obj.save()
        return redirect(contact_us)
def cart_page(request):
    return render(request,"cart.html")


