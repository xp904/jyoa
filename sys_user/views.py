from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views import View
from sys_user.models import SysRole

# Create your views here.

class RoleView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = SysRole.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.id,
                'name': role.name,
                'code': role.code
            })

        roles = SysRole.objects.all()
        return render(request, 'sys_mgr/role_list.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('role_id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        code = request.POST.get('code')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = SysRole.objects.get(pk=id)
            role.name = name
            role.code = code  # 建议不修改code
            role.save()
        else:
           SysRole.objects.create(name=name, code=code)

        return redirect('/role/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = SysRole.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })
