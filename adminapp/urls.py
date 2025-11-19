from django.urls import path
from adminapp import views

urlpatterns = [
    path('index_page/',views.index_page, name="index_page"),


    path('add_category/', views.add_category, name="add_category"),
    path('add_category_data/', views.add_category_data, name="add_category_data"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:category_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:cat_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:c_id>/', views.delete_category, name="delete_category"),
    path('view_contact_data/', views.view_contact_data, name="view_contact_data"),
    path('delete_message/<int:message_id>/', views.delete_message, name="delete_message"),



    path('add_books/', views.add_books, name="add_books"),
    path('add_books_data/', views.add_books_data, name="add_books_data"),
    path('display_books/', views.display_books, name="display_books"),
    path('edit_books/<int:book_id>/', views.edit_books, name="edit_books"),
    path('update_books/<int:book_id>/', views.update_books, name="update_books"),
    path('delete_books/<int:b_id>/', views.delete_books, name="delete_books"),


    path('login_admin/', views.login_Admin, name="login_admin"),
    path('login_admin_data/', views.login_admin_data, name="login_admin_data"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
]