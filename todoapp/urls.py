from django.urls import  path
from .import views

 

urlpatterns=[
    path('',views.index,name='home'),
    path('addtask/',views.addtask,name='addtask'),
    # path('complete_task/<int:task_id>',views.complete_task,name='complete_task'),
    path('delete_task/<int:task_id>',views.delete_task,name='delete_task'),
    path('accounts/user_login/',views.user_login,name='user_login'),
    path('accounts/user_signup/',views.user_signup,name='user_signup'),
    path('account/logout/',views.logout,name='logout'),
    path('displya/',views.displya,name='displya'),
    ]