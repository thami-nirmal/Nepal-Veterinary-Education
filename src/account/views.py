import random
import smtplib
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from account.models import Profile
from django.contrib.auth import authenticate, login, logout
from personal.views import LevelAndMaterialDetails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.

# Send OTP on specific email
def send_otp_email(email, otp_token):
    # Email configuration
    smtp_server = 'smtp.gmail.com'                # SMTPserver address for Gmail
    smtp_port = 587                               # For TLS/STARTTLS
    sender_email = 'thaminirmal112@gmail.com'     # Replace with your Gmail account
    sender_password = 'wirjxmpsdiokmsux'          # Replace with your Gmail account password

    # Generate the email content
    subject = 'Your OTP Token'                    # Subject of the email
    message = f'Your OTP Token: {otp_token}'      # Email message containing the OTP token

    msg = MIMEMultipart()                         # Create a MIMEMultipart object to represent the email 
    msg['From'] = sender_email                    # Set the 'From' address of the email
    msg['To'] = email                             # Set the 'To' address of the email
    msg['Subject'] = subject                      # Set the subject of the email
    msg.attach(MIMEText(message, 'plain'))        # Attach the message to the email

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)         # Create an SMTP object
        server.starttls()                                     # Start a secure TLS connection 

        # Log in to your Gmail account
        server.login(sender_email, sender_password)           # Log in using sender credentials

        # Send the email
        server.sendmail(sender_email, email, msg.as_string())  # Send the email as a string

        # Close the connection to the SMTP server
        server.quit()

        return True  # Return True to indicate successful email sending

    except Exception as e:
        # If there's an exception during the process, print the error message
        print(f"Failed to send email: {e}")
        return False  # Return False to indicate email sending failure


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
        
        # Set the template for rendering
        template_name = 'signup.html'

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list   = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to tbe passed to the template
        context = {
            'level_material_detail_list'      : level_material_detail_list,
        }

        # Render the signup.html template with the given context and return it as the HTTP response
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request for processing user signup data
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: redirect on sign up page
        """

        # Set the template to be render
        template_name = 'signup.html'

        if request.method == 'POST':
            # Extract user data from the POST request
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            profile_image = request.POST.get('profile_images')

            # Check if passwords match
            if password != confirm_password:
                messages.error(request, 'Password do not match')
                # return redirect('signup')
            
            # Check if the email is already registered
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered')
                level_material_detail_list   = LevelAndMaterialDetails()
                context = {
                    'first_name':first_name,
                    'last_name':last_name,
                    'email':email,
                    'password':password,
                    'confirm_password':confirm_password,
                    'level_material_detail_list':level_material_detail_list
                }

                return render(request, template_name, context)
            else:
                # Create a new user 
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
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
                user = authenticate(request, username=email, password=password)

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

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list   = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to tbe passed to the template
        context = {
            'level_material_detail_list'      : level_material_detail_list,
        }

        # Render the tempate with provided context and return it as a HTTP response
        return render(request, template_name, context)
    
    
    def post(self, request, *args, **kwargs):
        """
        Handle HTTP POST request to process login form submissions.

        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered HTTP response or redirect to 'index' page on successful login
        """

        # Set the template for rendering
        template_name = 'login.html'

        # Check if the HTTP method is POST (this method is used to handle form submissions).
        if request.method == 'POST':
            # Retrieve the username and password from the POST data submitted by the user.
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Authenticate the user using the provided username and password.
            user = authenticate(request, username=email, password=password)
            
            # Check if the user is authenticated (i.e., if the credentials are valid).
            if user is not None:
                # If the user is authenticated, log the user in, and create a session.
                login(request, user)

                # Redirect the user to the 'index' page
                return redirect('index')
            else:
                # If the user is not authenticated (invalid credentials), display an error message.
                messages.error(request, 'Username and password incorrect')

                # Call the LevelAndMaterialDetails function to retrieve level and material data
                level_material_detail_list   = LevelAndMaterialDetails()

                # Create a context dictionary to store the data to tbe passed to the template
                context = {
                    'email': email,
                    'password':password,
                    'level_material_detail_list':level_material_detail_list
                }

                # Render the template with the provided context
                return render(request, template_name, context)

        # Render the 'login.html' template in case of GET request or if the login attempt failed.
        return redirect('login')


def UserLogout(request):
    """
    View to handle user logout.

    :param request: the HTTP request object
    :return: a redirect to the 'index' page
    """
    logout(request)
    return redirect('index')


class ResetPasswordView(View):
    """
    A class-based view to handle user reset password.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'reset_password.html'
        :param request: the HTTp request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        # Set the template for rendering
        template_name = 'reset_password.html'

        # Call the LevelAndMaterialDetails function to retrieve level an material data
        level_material_detail_list = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to the passed to the template
        context = {
            'level_material_detail_list'      : level_material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)
    
    def post(self, request, *args, **kwargs):
        """
        Handles the POST request for processing user input for resetting the password
        :param request: the HTTP request object
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: the rendered HTTP response or redirects to another view
        """

        # Set the template for rendering
        template_name = 'reset_password.html'

        # Check if the request method is POST
        if request.method == "POST":

            # Get the email entered by the user from the form
            email = request.POST.get('email')

            # Generate a random 5-digit number for OTP token
            otp_token = str(random.randint(10000, 99999))

            # Check if the provided email exists in the User model
            if User.objects.filter(email=email).exists():
                # Call the function to send the OTP token to the user's email
                if send_otp_email(email, otp_token):
                    # Redirect to the OTP verification page with the OTP token as a URL parameter
                    return redirect('otp_verification', otp_token=otp_token) 
                else:
                    # If OTP email sending fails, print an error message
                    print("Failed to send OTP email")
            else:
                # If the provided email does not exist in the User model, show an error message
                messages.error(request,"Email doesn't exists!!")

        # Call the LevelAndMaterialDetails function to retrieve level an material data
        level_material_detail_list = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to the passed to the template
        context = {
            'level_material_detail_list'      : level_material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class OTPVerificationView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'otp_page.html'
        :param request: the HTTp request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        " Set the template for rendering"
        template_name = 'otp_page.html'

        # Call the LevelAndMaterialDetails function to retrieve level an material data
        level_material_detail_list = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to the passed to the template
        context = {
            'level_material_detail_list'      : level_material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)
