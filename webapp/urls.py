from django.urls import path
from webapp import views

urlpatterns = [
    path('home_page/',views.home_page, name="home_page"),
    path('about_page/', views.about_page, name="about_page"),
    path('popular_books/', views.popular_books, name="popular_books"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('filtered_books/<book_category>/', views.filtered_books,name="filtered_books"),
    path('book_details/<int:book_id>/',views.book_details, name="book_details"),
    path('login_user_signin/', views.login_user_signin, name="login_user_signin"),
    path('signup_user/', views.signup_user, name="signup_user"),
    path('signup_user_data/', views.signup_user_data, name="signup_user_data"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('contact_data_save/', views.contact_data_save, name="contact_data_save"),
    path('cart_page/', views.cart_page, name="cart_page"),
]