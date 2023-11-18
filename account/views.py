from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import User

def signup(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form' : form}
        return render(request, 'signup.html', context)
    
    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # 바로 저장 X
            request.session['user'] = {
                'email' : user.email,
                'phone' : user.phone,
            }
            user.save()
            return redirect('additional_info')
        else:
            return redirect('signup')
        
def additional_info(request):
    if 'user' not in request.session:
        return redirect('signup')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        
        user_info = request.session['user']
        user_info['username'] = username

        user = User.objects.get(email=user_info['email'])
        user.username = username
        user.save()

        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'additional_info.html', {'form' : form})
        

def login(request):
    if request.method == 'POST':
        pass
    else:
        pass