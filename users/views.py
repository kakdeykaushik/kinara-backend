from rest_framework.decorators import api_view
from users.decorators import exception_handler
from users.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .exceptions import http_409_conflict
# Create your views here.


@exception_handler
@api_view(["POST"])
def register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if User.objects.filter(username=username).exists():
        raise http_409_conflict("User already exists!")

    new_user = User(username=username, password=password)
    new_user.save()

    token = Token.objects.create(user=new_user)
    return Response({"token": token.key})





@exception_handler
@api_view(["POST"])
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = User.objects.get(username=username, password=password)

    token = Token.objects.get(user=user)
    return Response({"token": token.key})    
