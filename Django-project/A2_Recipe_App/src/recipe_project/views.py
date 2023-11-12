from django.shortcuts import render, redirect
# Django authentication libraries
from django.contrib.auth import authenticate, login, logout
# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm


# define a function view called login_view that takes a request from user
def login_view(request):
    error_message = None
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("recipes:recipes_list_signed_users")
        else:
            error_message = "ooops.. something went wrong"

    # prepare data to send from view to template
    context = {"form": form, "error_message": error_message}
    return render(request, "auth/login.html", context)


# define a function view called logout_view that takes a request from user
def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')
