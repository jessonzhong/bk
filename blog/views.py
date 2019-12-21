from django.shortcuts import render, HttpResponse
from blog import models, forms
from django.http import JsonResponse
from django.contrib import auth
from django.db.models import Count
from geetest import GeetestLib
import logging, os, json
from bk import settings
from django.db.models import F

# Create your views here.

# 生成一个logger实例，专门用来记录日志
logger = logging.getLogger(__name__)


# 注册函数
def register(request):
    if request.method == "POST":
        print(request.POST)
        print("=" * 100)
        ret = {"status": 0, "msg": ""}
        form_obj = forms.RegForm(request.POST)
        print(request.POST)

        # 校验部分
        if form_obj.is_valid():

            # 校验通过，去数据库创建一个新的用户
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_img)
            ret["msg"] = "/index/"
            return JsonResponse
        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            print(ret)
            print("=" * 100)
            return JsonResponse
        # 生成一个form对象
        form_obj = forms.RegForm()
        print(form_obj.fields)
        return render(request, "register.html", {"form_obj": form_obj})

# 校验用户名是否已经被注册函数
def check_username_exist(request):
    pass



