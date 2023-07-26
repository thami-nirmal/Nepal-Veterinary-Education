from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from account.models import Profile
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class SignupView(View):
    """
    A class-based view to handle user signup
    """
    def get(self, request, *args, **kwargs):
        """
        Handles the GET request for displaying the signup form
        :param request: the HTTP request object
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        template_name = 'signup.html'
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request for processing user signup data
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: redirect on sign up page
        """
        if request.method == 'POST':
            # Extract user data from the POST request
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            profile_image = request.POST.get('profile_images')

            # Check if passwords match
            if password1 != password2:
                messages.error(request, 'Password do not match')
                return redirect('signup')
            
            # Check if the email is already registered
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered')
            else:
                # Create a new user 
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password1)
                user.save()

                # Check if a user profile already exists and update profile image if provided
                if Profile.objects.filter(user=user).exists():
                    if profile_image:
                        Profile.objects.filter(user = user).update(profile_image=profile_image)
                    else:
                        default_profile_image = "profile_images/profile.png"
                        Profile.objects.filter(user=user).update(profile_image=default_profile_image)
                
                # To enter into the system after successfully signup
                # Authenticate the user using the provided username and password.
                user = authenticate(request, username=email, password=password1)

                # Check if the user is authenticated (i.e., if the credentials are valid).
                if user is not None:
                    # If the user is authenticated, log the user in, and create a session.
                    login(request, user)

                    # Redirect the user to the 'index' page (replace 'index' with the appropriate URL name).
                    return redirect('index')
                
        # Redirect to the signup page in case of form submission errors
        return redirect('signup')


class LoginView(View):
    """
    A class-based view to handle user login.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'login.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        # Set the template for rendering
        template_name = 'login.html'
        return render(request, template_name)
    
    def post(self, request, *args, **kwargs):
        """
        Handle HTTP POST request to process login form submissions.

        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered HTTP response or redirect to 'index' page on successful login
        """

        # Check if the HTTP method is POST (this method is used to handle form submissions).
        if request.method == 'POST':
            # Retrieve the username and password from the POST data submitted by the user.
            username = request.POST.get('username')
            pass1 = request.POST.get('pass')

            # Authenticate the user using the provided username and password.
            user = authenticate(request, username=username, password=pass1)

            # Check if the user is authenticated (i.e., if the credentials are valid).
            if user is not None:
                # If the user is authenticated, log the user in, and create a session.
                login(request, user)

                # Redirect the user to the 'index' page
                return redirect('index')
            else:
                # If the user is not authenticated (invalid credentials), display an error message.
                messages.error(request, 'Username and password incorrect')

        # Render the 'login.html' template in case of GET request or if the login attempt failed.
        return render(request, 'login.html')
    

def UserLogout(request):
    """
    View to handle user logout.

    :param request: the HTTP request object
    :return: a redirect to the 'index' page
    """
    logout(request)
    return redirect('index')