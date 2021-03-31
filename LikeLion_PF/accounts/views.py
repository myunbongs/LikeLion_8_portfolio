from django.shortcuts import render
from django.shortcuts import redirect
from .models import Account
from django.contrib.auth.hashers import check_password


# Create your views here.

def signup_view (request) :
    if request.method == 'POST' : #요청이 post 형식이면 각 정보를 받아와서 user에 저장
        password=request.POST.get('password','defalut')
        password2=request.POST.get('password2','defalut')

        if  password==password2 :
            user = Account.objects.create(userid=request.POST['userid'], #ID
                            email=request.POST.get('email','defalut'),   #이메일
                            username=request.POST['username'],  #이름
                            password=password, #비번
                                            )
            
            request.session['user'] = user.userid 
            return render(request,'../../portfolio/templates/portfolio/list.html')
        else :
            return redirect('/')

    else : #요청이 get이면 signup.html을 띄움
        return render(request, 'signup.html')


def login_view(request) :
    if request.method=='POST' : #요청이  post일때
        userid = request.POST['userid'] 
        password = request.POST['password']

        user = Account.objects.get(userid=userid) # 없으면 404에러 띄우기
        
        if password==user.password:
                request.session['user'] = user.userid 
                request.session.modified = True
                return render(request,'../../portfolio/templates/portfolio/list.html')
        else :
            
            return render(request, 'login.html') #다시 로그인페이지로 
    else : #요청이 get이면 login.html을 띄움
        return render(request,'login.html')



def logout_view(request) :
            request.session.clear()
            return redirect('/')
