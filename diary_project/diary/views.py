from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .models import DiaryEntry
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")
        # Add logic to create user and redirect to login page
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists")
            return render(request, "register.html")
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("home")
    
    return render(request, "register.html")



def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "invalid username or password")
    return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")

@login_required
def home_view(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by("-created_at")
    context = {
        "entries": entries
    }
    return render(request, "home.html", context)

@login_required
def add_entry_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            DiaryEntry.objects.create(user=request.user, title=title, content=content)
            messages.success(request, "Entry added successfully.")
            return redirect("home")
        else:
                messages.error(request, "Both title and content are required.")
    return render(request, "add_entry.html")


@login_required
def delete_entry_view(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    if request.method == "POST":
        entry.delete()
        messages.success(request, "Entry deleted successfully.")
        return redirect("home")
    return render(request, "delete_entry.html", {"entry": entry})



@login_required
def edit_entry_view(request, entry_id):

    entry = get_object_or_404(
        DiaryEntry,
        id=entry_id,
        user=request.user
    )

    if request.method == "POST":

        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()

        if title and content:

            entry.title = title
            entry.content = content

            entry.save()

            messages.success(
                request,
                "Entry updated successfully."
            )

        else:
            messages.error(
                request,
                "Both title and content are required."
            )

    return redirect("home")


    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            entry.title = title
            entry.content = content
            entry.save()
            messages.success(request, "Entry updated successfully.")
            return redirect("home")
        else:
                messages.error(request, "Both title and content are required.")