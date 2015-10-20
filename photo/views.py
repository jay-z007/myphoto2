from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from myphoto.settings import MEDIA_URL
from photo.models import *
from photo.forms import UploadPhotoForm
from django.views.generic import View
from django.core.mail import send_mail
from photo.forms import UploadPhotoForm
from django.views.generic import View
from django.utils import timezone
from django.core.urlresolvers import reverse


def slide(request, album_id):
    album = Album.objects.get(id = album_id)
    cover = album.cover_photo
    photo_list = Photo.objects.filter(albums = album_id)
    return render_to_response("photo/slide.html", dict(photo_list = photo_list, cover = cover, media_url = MEDIA_URL))


def photo_booth_strips(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/photo/login/?next=%s' % request.path)

    albums = Album.objects.filter(users__id = request.session['user_id'])[:4]
    # if request.user.is_authenticated():
    #     albums = albums.object_list

    paginator = Paginator(albums, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.photo_set.all()[:6]
    return render_to_response("photo/photo_booth_strips.html", dict(albums=albums, user=request.user,
                                                        media_url=MEDIA_URL))

@csrf_exempt
def search(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/photo/login/?next=%s' % request.path)

    photos = Photo.objects.filter(user_id = request.session['user_id']).filter(tags__tag = request.POST.get('tags'))
    
    return render_to_response("photo/search.html", dict(photos=photos, user=request.user,
                                                       media_url=MEDIA_URL))


def success(request, album_id):
    context = RequestContext(request)
    return render_to_response("photo/success.html",{'email':album_id}, context)


def index(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/photo/login/?next=%s' % request.path)

    albums = Album.objects.filter(users__id = request.session['user_id'])
    # if request.user.is_authenticated():
    #     albums = albums.object_list
    tags = Tag.objects.all()
    paginator = Paginator(albums, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.photo_set.all()[:6]

    return render_to_response("photo/index.html", dict(albums=albums, user=request.user, tags=tags,
                                                       media_url=MEDIA_URL))


def albums(request):
    albums = Album.objects.all()
    if not request.user.is_authenticated():
        albums = albums.object_list

    paginator = Paginator(albums, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    # for album in albums.object_list:
    #     album.images = album.photo_set.all()[:4]

    return render_to_response("photo/albums.html", dict(albums=albums, user=request.user,
                                                        media_url=MEDIA_URL))

@csrf_protect
def register_form(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user = MyUser.objects.create_user(email=request.POST['email'], date_of_birth=request.POST['date_of_birth'], first_name=request.POST['first_name'],
                      last_name=request.POST['last_name'], gender=request.POST['gender'], password=request.POST['password']
                      )
        user.save()
        registered = True
        return render_to_response('photo/login.html',{'message': "Registration successful. Enter your credentials"},context)
    else:
    # Render the template depending on the context.
        return render_to_response('photo/register.html',context)


@csrf_exempt
def user_update(request):
    u_id = request.session['user_id']
    user = MyUser.objects.get(id=u_id)
    time = user.time_registered
    if request.method == 'POST' :
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.time_registered = timezone.now()
        user.gender = request.POST['gender']
        user.date_of_birth = request.POST['date_of_birth']
        user.save()

    return render_to_response("photo/update_user.html", dict(user = user))


@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        send_mail('New Password', 'Your New Password is "india@123"', 'faizaancharania@gmail.com', ['jayybhatt007@gmail.com'], fail_silently=False)
        return render_to_response("photo/login.html")
    return render_to_response("photo/forgot_password.html")


@csrf_protect
def login_form(request):

    # Like before, obtain the context for the user's request.

    context = RequestContext(request)
    if request.user.is_active :
    # If the request is a HTTP POST, try to pull out the relevant information.
        return HttpResponseRedirect('/photo/', dict(message="You are already logged in"),context)
    else:
        if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.

            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
            # If we have a User object, the details are correct.
            # If None (Python's way of representing the absence of a value), no user
            # with matching credentials was found.
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # We'll send the user back to the homepage.
                    login(request, user)
                    request.session['user_id'] = user.id
                    return HttpResponseRedirect('/photo/', {})
                else:
                    # An inactive account was used - no logging in!
                    return HttpResponse("Your Phileikones account is disabled.")
            else:
                # Bad login details were provided. So we can't log the user in.
                #return HttpResponse("Invalid login details supplied.")
                return render_to_response('photo/login.html',{'message': "Invalid Login Details"},context)
        # The request is not a HTTP POST, so display the login form.
        # This scenario would most likely be a HTTP GET.
        else:
            # No context variables to pass to the template system, hence the
            # blank dictionary object...
            return render_to_response('photo/login.html', {}, context)

def dev(request):
    return render_to_response('photo/develop.html')

def abt(request):
    return render_to_response('photo/abt.html')



def home(request):
    return render_to_response('photo/home.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/photo/home/')

def album_details(request, album_id):
    albums = Album.objects.get(id = album_id)
    count = albums.photo_set.count()
    cover = albums.cover_photo
    photo_list = Photo.objects.filter(albums = album_id)
    title = albums.album_name
    return render_to_response("photo/album_details.html", dict(title=title,count= count, id = album_id ,photo_list = photo_list, cover = cover, media_url = MEDIA_URL))


@csrf_exempt
def upload_photo(request):
    if request.method == "POST":
        image = request.FILES['image']
        photo = Photo(image = image, title = request.POST['title'])
        tags = request.POST.getlist('Tags')
        photo.save()
        for text in tags:
            tag = Tag.objects.get(tag = text)
            photo.tags.add(tag)

        albums = request.POST.getlist('Albums')
        for album_name in albums:
            album = Album.objects.filter(album_name = album_name)
            for a in album :
                photo.albums.add(a)

        photo.user = request.user

        photo.save()
        photo.save_dimen()
        if photo:
            albums = Album.objects.all()
            return HttpResponseRedirect('/photo/albums/',dict(albums = albums))
        else:
            return render_to_response("photo/add_photo.html", dict(form = "form"))
    else:
        all_albums = Album.objects.all()
        all_tags = Tag.objects.all()
        return render_to_response("photo/add_photo.html", dict(all_albums = all_albums, all_tags = all_tags))

@csrf_exempt
def create_album(request):
    if request.method == 'POST':
        album = Album()
        album.cover_photo = request.FILES['image']
        album.album_name = request.POST.get('album_name')
        album.description = request.POST.get('description')
        album.save()
        all_users = request.POST.getlist('Users')
        for user in all_users:
            album.users.add(user)
        user = MyUser.objects.get(id = request.session['user_id'])
        album.users.add(user)
        album.save()

        if album:
            return HttpResponseRedirect(reverse('album_details', args=(album.id,)))
        else:
            return render_to_response("photo/create_album.html")
    else:
        all_users = MyUser.objects.all().exclude(id = request.session['user_id'])
        return render_to_response("photo/create_album.html", dict(all_users = all_users))


def photo_detail(request,photo_id):
    photo = Photo.objects.get(id = photo_id)
    all_tags = photo.tags.all()
    albums = photo.albums.all()
    return render_to_response("photo/image_detail.html", dict(photo = photo, albums= albums, all_tags = all_tags))
