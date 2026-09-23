from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import ContactMessage


# =========================================================
# HOME
# =========================================================

def home(request):

    return render(
        request,
        'home.html'
    )


# =========================================================
# ABOUT
# =========================================================

def about(request):

    return render(
        request,
        'about.html'
    )


# =========================================================
# RESUME
# =========================================================

def resume(request):

    return render(
        request,
        'resume.html'
    )


# =========================================================
# CONTACT US
# =========================================================

def contact(request):

    if request.method == "POST":

        name = request.POST.get('name', '').strip()

        email = request.POST.get('email', '').strip()

        comment = request.POST.get('comment', '').strip()


        # Validation

        if not name or not email or not comment:

            messages.error(
                request,
                "Please fill all the fields."
            )

            return redirect('contact')


        # Save message

        ContactMessage.objects.create(

            name=name,

            email=email,

            comment=comment

        )


        messages.success(
            request,
            "Thank you! Your message has been sent successfully."
        )

        return redirect('contact')


    return render(
        request,
        'contactus.html'
    )


# =========================================================
# ADMIN LOGIN
# =========================================================

def admin_login(request):

    if request.user.is_authenticated:

        return redirect('admin_dashboard')


    if request.method == "POST":

        username = request.POST.get('username', '').strip()

        password = request.POST.get('password', '')


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None and user.is_staff:

            login(request, user)

            return redirect('admin_dashboard')


        messages.error(
            request,
            "Invalid username or password."
        )


    return render(
        request,
        'admin_login.html'
    )


# =========================================================
# ADMIN DASHBOARD
# =========================================================

@login_required(login_url='admin_login')
def admin_dashboard(request):

    # Only staff/admin can access

    if not request.user.is_staff:

        logout(request)

        return redirect('admin_login')


    contact_messages = ContactMessage.objects.all()


    total_messages = ContactMessage.objects.count()

    unread_messages = ContactMessage.objects.filter(
        is_read=False
    ).count()

    read_messages = ContactMessage.objects.filter(
        is_read=True
    ).count()


    context = {

        'contact_messages': contact_messages,

        'total_messages': total_messages,

        'unread_messages': unread_messages,

        'read_messages': read_messages,

    }


    return render(
        request,
        'admin.html',
        context
    )


# =========================================================
# MARK MESSAGE AS READ
# =========================================================

@login_required(login_url='admin_login')
def mark_message_read(request, message_id):

    if not request.user.is_staff:

        return redirect('admin_login')


    contact_message = get_object_or_404(
        ContactMessage,
        id=message_id
    )


    contact_message.is_read = True

    contact_message.save()


    return redirect('admin_dashboard')


# =========================================================
# DELETE MESSAGE
# =========================================================

@login_required(login_url='admin_login')
def delete_message(request, message_id):

    if not request.user.is_staff:

        return redirect('admin_login')


    contact_message = get_object_or_404(
        ContactMessage,
        id=message_id
    )


    if request.method == "POST":

        contact_message.delete()


    return redirect('admin_dashboard')


# =========================================================
# ADMIN LOGOUT
# =========================================================

@login_required(login_url='admin_login')
def admin_logout(request):

    logout(request)

    return redirect('admin_login')