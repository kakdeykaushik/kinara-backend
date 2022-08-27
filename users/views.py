from rest_framework.decorators import api_view
from users.decorators import exception_handler
from users.models import User
from rest_framework.response import Response
from .exceptions import Conflict
# Create your views here.


@api_view(["POST"])
@exception_handler
def register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if User.objects.filter(username=username).exists():
        raise Conflict("User already exists!")

    new_user = User(username=username, password=password)
    new_user.save()
    token = new_user.get_token()
    return Response({"token": token.key})





@api_view(["POST"])
@exception_handler
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = User.objects.get(username=username, password=password)
    
    token = user.get_token()

    return Response({"token": token.key})    
