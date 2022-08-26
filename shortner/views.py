import random

from shortner.decorators import exception_handler
from shortner.exceptions import http_403_forbidden
from .models import Url
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from .serializers import UrlSerializer


# Create your views here.

CORPUS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


# Reidrect to main url
@exception_handler
@api_view(["GET"])
def view_url(request, url):
    url_object = Url.objects.get(short_url=url, is_active=True)
    original_url = url_object.original_url
    
    url_object.clicks += 1
    url_object.save()

    return redirect(original_url)


# creates shortened url
@exception_handler
@api_view(["POST"])
def shortner(request):
    
    while True:
        mini_url = ""
        for _ in range(7):
            mini_url += random.choice(CORPUS)

        if not Url.objects.filter(short_url=mini_url).exists():
          break


    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    original_url = request.POST.get("url")
    new_url = Url(short_url=mini_url, original_url=original_url, owner=token_object.user)
    new_url.save()
    
    serializer = UrlSerializer(new_url)
    return Response(serializer.data)



# gives url detail to owner only
@exception_handler
@api_view(["GET"])
def url_detail(request, url):

    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    user = token_object.user

    url_object = Url.objects.get(short_url=url, is_active=True)

    if user == url_object.owner:
        serializer = UrlSerializer(url_object)
        return Response(serializer.data)
    else:
        raise http_403_forbidden()




# disable url - owner only
@exception_handler
@api_view(["GET"])
def url_disable(request, url):

    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    user = token_object.user

    url_object = Url.objects.get(short_url=url)


    if user == url_object.owner:
        url_object.is_active = False
        url_object.save()
        serializer = UrlSerializer(url_object)
        return Response(serializer.data)
    else:
        raise http_403_forbidden()



# enable url - owner only
@exception_handler
@api_view(["GET"])
def url_enable(request, url):

    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    user = token_object.user

    url_object = Url.objects.get(short_url=url)


    if user == url_object.owner:
        url_object.is_active = True
        url_object.save()
        serializer = UrlSerializer(url_object)
        return Response(serializer.data)
    else:
        raise http_403_forbidden()





# delete url - owner only
@exception_handler
@api_view(["GET"])
def url_delete(request, url):

    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    user = token_object.user

    url_object = Url.objects.get(short_url=url)


    if user == url_object.owner:
        url_object.delete()
        return Response({"message": f"{url} - deleted"})
    else:
        raise http_403_forbidden()
