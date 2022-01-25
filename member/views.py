from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from postapp.models import Post
from django.utils import timezone

def login_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            m = Member.objects.get(user_id=user_id, user_pw=user_pw)
        # 회원정보 조회 실패 시 예외 발생
        except Member.DoesNotExist as e:
            return render(request, 'member/login.html', 
                {'message':'아이디 비밀번호를 확인해주세요.'})
        else:
            request.session['user_id'] = m.user_id
            request.session['user_name'] = m.user_name
        return redirect('postapp:main')
    else:
        return render(request, 'member/login.html')


def logout_custom(request):
    # session 개별 삭제
    del request.session['user_id']
    del request.session['user_name']

    # session 전체 삭제
    request.session.flush()

    return redirect('member:login')

def signup_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')
        m = Member(
            user_id=user_id, 
            user_pw=user_pw, 
            user_name=user_name
            )
        m.date_joined = timezone.now()
        m.save()
        return redirect('member:login')
    else:
        return render(request, 'member/signup.html')