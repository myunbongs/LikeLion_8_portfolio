from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password


# Create your views here.

def signup_view (request) :
    if request.method == 'POST' : #요청이 post 형식이면 각 정보를 받아와서 user에 저장
        password=request.POST.get('password','defalut')
        password2=request.POST.get('password2','defalut')

        if  password==password2 :
            user = User.objects.create(username=request.POST['userid'], #ID
                            email=request.POST.get('email','defalut'),   #이메일
                            first_name=request.POST['username'],  #이름
                            password=password, #비번
                                            )
            
            auth.login(request,user)
            return redirect('/')
        else :
            return redirect('/')

    else : #요청이 get이면 signup.html을 띄움
        return render(request, 'signup.html')


def login_view(request) :
    if request.method=='POST' : #요청이  post일때
        userid = request.POST['userid'] 
        password = request.POST['password']

        #user = User.objects.get(username = userid, password = password)
        user= User.objects.get(username=userid) 
        if user is not None  :
            if  user.is_superuser:
                if check_password(password,user.password) :
                    auth.login(request,user)
                    return redirect('/')
            else :
                user=User.objects.get(password=password,username=userid)
                auth.login(request,user)
                return redirect('/')
        else :
         #비밀번호가 틀림
            return render(request, 'login.html')
    else : #요청이 get이면 login.html을 띄움
        return render(request,'login.html')



def logout_view(request) :
            auth.logout(request)
            return redirect('/')
