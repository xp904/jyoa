from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import path

from sys_user.models import SysUser
from common import make_pwd
from sys_user.views import RoleView, ESView, ESLogView


def to_index(request: HttpRequest):
    return render(request, 'index.html', locals())


def to_login(request: HttpRequest):
    if request.method == "POST":
        # 获取用户名和口令
        name = request.POST.get('username', '')
        pwd = request.POST.get('password', '')

        if any((not name, not pwd, len(name) == 0, len(pwd) == 0)):
            error = '用户名或口令不能为空!'

        else:
            ret = SysUser.objects.filter(name=name, auth_string=make_pwd(pwd))
            if ret.exists():
                login_user = ret.first()

                # 将登录的用户信息存在session中
                request.session['login_user'] = {
                    'id': login_user.id,
                    'name': login_user.name,
                    'role_name': login_user.role.name,
                    'role_code': login_user.role.code
                }

                return redirect('/')

            error = "用户名或口令错误!"

    return render(request, 'login.html', locals())


def to_regist(request: HttpRequest):
    return render(request, 'register.html')


def to_logout(req: HttpRequest):
    req.session.pop('login_user')
    return redirect('/login/')


urlpatterns = [
    path('regist/', to_regist),
    path('login/', to_login),
    path('logout/', to_logout),
    path('role/', RoleView.as_view()),
    path('init_es/', ESView.as_view()),
    path('upload_log/', ESLogView.as_view),
    path('', to_index),
]
