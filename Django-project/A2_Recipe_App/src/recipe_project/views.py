from django.shortcuts import render, redirect
# Django authentication libraries
from django.contrib.auth import authenticate, login, logout
# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserAdminCreationForm  # Import your custom form
from accounts.views import favorite_list, created_recipe


def signup_view(request):
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)  # Use the custom form
        if form.is_valid():
            form.save()
            print("User created successfully")
            return redirect('login')
        else:
            print("User creation failed")
            print(form.errors)
    else:
        form = UserAdminCreationForm()  # Use the custom form

    return render(request, 'auth/signup.html', {'form': form})

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

# define a function view called profile_view that takes a request from user
def profile_view(request):
    favorite_recipes = favorite_list(request)
    created_recipes = created_recipe(request)
    return render(request, 'accounts/profile.html', {'favorite_recipes': favorite_recipes, 'created_recipes': created_recipes})


# define a function view called logout_view that takes a request from user
def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')
