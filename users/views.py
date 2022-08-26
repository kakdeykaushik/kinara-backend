from rest_framework.decorators import api_view
from users.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.


@api_view(["POST"])
def register(request):
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            raise Exception("User alreaddy exists!")

        new_user = User(username=username, password=password)
        new_user.save()

        token = Token.objects.create(user=new_user)
        return Response({"token": token.key})

    except Exception as e:
        print(str(e))
        raise e





@api_view(["POST"])
def login(request):
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.get(username=username, password=password)

        token = Token.objects.get(user=user)
        return Response({"token": token.key})    

    except Exception as e:
        print(str(e))
        raise e
