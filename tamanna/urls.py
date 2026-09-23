from django.urls import path

from . import views


urlpatterns = [

    # Main pages

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'resume/',
        views.resume,
        name='resume'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),


    # Admin

    path(
        'secure-admin/',
        views.admin_login,
        name='admin_login'
    ),

    path(
        'secure-admin/dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'secure-admin/message/<int:message_id>/read/',
        views.mark_message_read,
        name='mark_message_read'
    ),

    path(
        'secure-admin/message/<int:message_id>/delete/',
        views.delete_message,
        name='delete_message'
    ),

    path(
        'secure-admin/logout/',
        views.admin_logout,
        name='admin_logout'
    ),

]