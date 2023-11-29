from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, login

User = get_user_model()


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        country = request.POST.get('country')
        town = request.POST.get('town')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=username, country=country, town=town,
                                            phone=phone, password=password)
        login(request, new_user)
        return redirect('index')
    return render(request, 'accounts/signup.html')
