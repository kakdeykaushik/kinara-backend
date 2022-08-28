from shortner.decorators import exception_handler
from shortner.exceptions import Forbidden
from .models import Url
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from .serializers import UrlSerializer


# Create your views here.



# Reidrect to main url
@api_view(["GET"])
@exception_handler
def view_url(request, url):
    url_object = Url.objects.get(short_url=url, is_active=True)
    original_url = url_object.original_url
    
    url_object.clicks += 1
    url_object.save()

    return redirect(original_url)


# creates shortened url
@api_view(["POST"])
@exception_handler
def shortner(request):

    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    original_url = request.POST.get("url")
    new_url = Url(original_url=original_url, owner=token_object.user)
    new_url.save()
    
    serializer = UrlSerializer(new_url)
    return Response(serializer.data)



# gives url detail to owner only
@api_view(["GET"])
@exception_handler
def url_detail(request, url):

    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    user = token_object.user

    url_object = Url.objects.get(short_url=url)

    if user == url_object.owner:
        serializer = UrlSerializer(url_object)
        return Response(serializer.data)
    else:
        raise Forbidden("Not Allowed")




# disable url - owner only
@api_view(["GET"])
@exception_handler
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
        raise Forbidden("Not Allowed")



# enable url - owner only
@api_view(["GET"])
@exception_handler
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
        raise Forbidden("Not Allowed")





# delete url - owner only
@api_view(["DELETE"])
@exception_handler
def url_delete(request, url):

    token = request.headers["Authorization"].split()[-1]
    token_object = Token.objects.get(key=token)
    
    user = token_object.user

    url_object = Url.objects.get(short_url=url)


    if user == url_object.owner:
        url_object.delete()
        return Response({"message": f"{url} - deleted"})
    else:
        raise Forbidden("Not Allowed")
