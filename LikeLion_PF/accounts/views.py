from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User 
from django.contrib import auth

# Create your views here.

def signup_view (request) :
    if request.method == 'POST' : #요청이 post 형식이면 각 정보를 받아와서 user에 저장
        user = User.objects.create_user(name=request.POST['name'],
                                        userid=request.POST['userid'],
                                        password=request.POST['password'],
                                        email=request.POST['email'])
        auth.login(request,user) #로그인
        return render (request,'home.html') 

    else : #요청이 get이면 signup.html을 띄움
        return render(request, 'signup.html')


def login_view(request) :
    if request.method=='POST' : #요청이  post일때
        userid = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request, userid = userid, password= password)
        # 받아온 userid와 password가 user에 존재하는지 대조
        if (user is not None) : #있다면
            auth.login(request,user) #로그인
            return redirect('/')
        else :
            #일치하는 정보가 없다고 팝업
            return render(request, 'login.html') #다시 로그인페이지로 
    else : #요청이 get이면 login.html을 띄움
        return render(request,'login.html')



def logout_view(request) :
    if request.method=='POST' : #요청이 post면
        auth.logout(request) #로그아웃
        return redirect('/') 
