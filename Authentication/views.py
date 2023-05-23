from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
# Create your views here.
class UserRegister(View):
    def get(self, request):
        return render(request, 'Authentication/register.html')

    def post(self, request):
        data = json.loads(request.boby)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should not contain symbols'})
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username already exist'})
        return JsonResponse({'username_value': True})

def login(request):
    return render(request, 'Authentication/login.html')


def register1(request):
    username = request.POST.get('username')
    full_name = request.POST.get('full-name')
    email = request.POST.get('email')
    password=request.POST.get('password')
    phone_number=request.POST.get('phone-no')

    if request.method == 'POST':
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password<7):
                    messages.error(request, 'Password too short')
                    return render(request, 'Authentication/register.html')
                user = User.objects.create_user(username=username, email=email, phone_number=phone_number, firstname = full_name)
                user.set_password(password)
                user.save()
                messages.success(request, 'Acount successfully created ')
        return render(request, 'Authentication/register.html')
    return render(request, 'Authentication/register.html')

