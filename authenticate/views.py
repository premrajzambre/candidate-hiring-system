from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	return render(request, 'authenticate/home.html', {})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#messages.success(request, ('You Have Been Logged In!'))
			return redirect('/mainapp/hr_admin')
			#return render(request, 'mainapp/upload.html', {})

		else:
			messages.success(request, ('Error Logging In - Please Try Again...'))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your HR account.'
			message = render_to_string('authenticate/acc_active_email.html',{
			'user': user,
			'domain': current_site.domain,
			'uid':urlsafe_base64_encode(force_bytes(user.pk)),
			'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')
			#username = form.cleaned_data['username']
			#password = form.cleaned_data['password1']
			#user = authenticate(username=username, password=password)
			#login(request, user)
			#messages.success(request, ('You Have Registered...'))
			#return redirect('login')
	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Your Profile...'))
			return redirect('/mainapp/hr_admin')
	else:
		form = EditProfileForm(instance=request.user)

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You Have Edited Your Password...'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)

def about_home(requests):
	return render(requests, 'authenticate/about_home.html',{})

def login_success(requests):
	return render(requests, 'authenticate/login_success.html',{})

def acc_active_email(requests):
	return render(requests, 'authenticate/acc_active_email.html', {})

def activate(request,uidb64,token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user,token):
		user.is_active = True
		user.save()
		login(request,user)
		#return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
		return render(request,'authenticate/login_success.html',{})
	else:
		return HttpResponse('Activation link is invalid!')

"""def password_reset_form(request):
	if request.method == 'POST':
		form = PasswordResetForm(data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request)
			messages.success(request, ('You Have Edited Your Password...'))
			return redirect('login')
	else:
		form = PasswordResetForm()

	context = {'form': form}
	return render(request, 'authenticate/password_reset_form.html', context)
"""
