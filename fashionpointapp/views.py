from django.shortcuts import render
from django.http import HttpResponse
from fashionpointapp.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from fashionpointapp.forms import PostForm
from fashionpointapp.models import UserProfile
from datetime import datetime
from fashionpointapp.forms import UserForm,UserProfileForm

def index(request):
 return render(request, 'fashionpointapp/index.html',)
def categories(request):
 return render(request, 'fashionpointapp/categories.html',)
def show_category(request, category_name_slug):
 context_dict = {}
 try:
  category = Category.objects.get(slug=category_name_slug)
  context_dict['category'] = category
 except Category.DoesNotExist:
  context_dict['category'] = None
 return render(request, 'fashionpointapp/category.html', context_dict)

def contact_us(request):
	return render(request, 'fashionpointapp/contact_us.html',)

def about_us(request):
	return render(request, 'fashionpointapp/about.html',)
def sitemap(request):
	return render(request, 'fashionpointapp/sitemap.html',)

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,
				'fashionpointapp/signup.html',
				{'user_form': user_form,
				'profile_form': profile_form,
				'registered': registered})
@login_required
def PostaPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES )
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.userPofile = UserProfile.objects.get(user=request.user)  # use your own profile here
            candidate.save()
            return index(request)
        else:
            print(form.errors)
    return render(request, 'fashionpointapp/PostaPost.html', {'form': form})
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'Fashionpointapp/login.html', {})
@login_required
def restricted(request):
	return render(request,'Fashionpointapp/restricted.html',{})
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
def visitor_cookie_handler(request):
	visits = int(get_server_side_cookie(request, 'visits', '1'))
	last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
	if (datetime.now() - last_visit_time).days > 0:
		visits = visits + 1
		request.session['last_visit'] = str(datetime.now())
	else:
		request.session['last_visit'] = last_visit_cookie
	request.session['visits'] = visits

def get_server_side_cookie(request, cookie, default_val=None):
	val = request.session.get(cookie)
	if not val:
		val = default_val
	return val

