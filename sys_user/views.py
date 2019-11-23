from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views import View
from pymysql.cursors import DictCursor

from sys_user.models import SysRole

from django.db import connection

# Create your views here.

from common import es_

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


class ESView(View):
    def get(self, request):
        # 同步ES（初始化）
        es_.create_index()

        cursor = connection.cursor()
        cursor.execute('select id,name,ord_sn,parent_id from t_category')
        for row in cursor.fetchall():
            doc = {
                'id': row[0],
                'name': row[1],
                'ord_sn': row[2],
                'parent_id': row[3]
            }

            es_.add_doc(doc, 'category')

        return JsonResponse({
            'status': 0,
            'msg': '同步ElasticSearch搜索引擎成功'
        })


class ESLogView(View):
    def post(self, request):

        data = request.POST
        print(data)

        return JsonResponse({
            'status': 0,
            'msg': '上传日志成功'
        })