from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from .models import User
from django.contrib.auth import login, logout

# 회원가입
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
            return redirect('account:additional_info')
        else:
            return redirect('account:signup')

# 닉네임 설정  
def additional_info(request):
    if 'user' not in request.session:
        return redirect('account:signup')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        
        user_info = request.session['user']
        user_info['username'] = username

        user = User.objects.get(email=user_info['email'])
        user.username = username
        user.save()

        return redirect('account:login')
    else:
        form = SignUpForm()
    return render(request, 'additional_info.html', {'form' : form})
        
# 로그인
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            msg = "올바른 유저 이메일과 패스워드를 입력하세요."
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
            else:
                if user.check_password(raw_password):
                    msg = None
                    login(request, user)
                    return redirect('mypage:create_receivers')
                    # return render(request, "base.html") -> 로그아웃 버튼
    else:
        msg = None
        form = LoginForm()
    return render(request, "login.html", {"form": form, "msg": msg})

# 로그아웃
def logout_view(request):
    # 데이터 유효성 검사
    if request.user.is_authenticated:
        logout(request)
    return redirect('account:signup')