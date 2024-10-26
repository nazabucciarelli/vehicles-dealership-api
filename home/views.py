from django.contrib.auth import (
    authenticate,
    login,
    logout)
from django.shortcuts import redirect, render
from django.views import View
from django.views import View
from users.forms import UserRegistrationForm
from django.http import JsonResponse
from users.models import Province, City

class LoginView(View):
    def get(self, request):
        return render(
            request,
            'login.html'
        )

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user:
                print(user)
                login(request, user)
                return redirect('vehicle_list')
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirigir a la página de inicio o a donde desees
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def load_provinces(request):
    country_id = request.GET.get('country_id')
    provinces = list(Province.objects.filter(country_id=country_id).values('id', 'name'))
    return JsonResponse({'provinces': provinces})

def load_cities(request):
    province_id = request.GET.get('province_id')
    cities = list(City.objects.filter(province_id=province_id).values('id', 'name'))
    return JsonResponse({'cities': cities})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class AdminPanelView(View):
    def get(self, request):
        return render(
            request,
            "admin_panel.html"
        )
