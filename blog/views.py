from django.shortcuts import render, HttpResponse, redirect
from blog import models, forms
from django.http import JsonResponse
from django.contrib import auth
from django.db.models import Count
import logging, os, json
from bk import settings
from django.db.models import F
from geetest import GeetestLib

pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"
mobile_geetest_id = "7c25da6fe21944cfe507d2f9876775a9"
mobile_geetest_key = "f5883f4ee3bd4fa8caec67941de1b903"

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
    ret = {"status": 0, "msg": ""}
    username = request.GET.get("username")
    print(username)
    is_exist = models.UserInfo.objects.filter(username=username)
    if is_exist:
        ret["status"] = 1
        ret["msg"] = "用户名已被注册"
    return JsonResponse


# 登录函数
def login(request):
    if request.method == "POST":
        # 初始化一个给ajax返回的函数
        ret = {"status": 0, "msg": ""}

        # 从提交过来的数据中获取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        # 获取极验滑动验证码相关参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]

        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 如果用户账户密码追赠却，给用户做登录
                auth.login(request, user)  # 将登录用户赋值给request.user
                ret["msg"] = "/index/"
            else:
                # 账户密码错误
                ret["status"] = 1
                ret["msg"] = "账户或密码错误"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"
        return JsonResponse
    return render(request, "login2.html")


# 注销登录函数
def logout(request):
    auth.logout(request)
    return redirect("/index/")


# 主页面函数
def index(request):
    # 查询所有文章列表
    article_list = models.Article.objects.all()
    return render(request, "index.html", {"article_list": article_list})


# 获取验证码-图片函数
def get_valid_img(request):
    # 自己生成一个图片
    from PIL import Image, ImageDraw, ImageFont
    import random

    # 获取随机颜色的函数
    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 生成一个图片对象
    img_obj = Image.new('RGB', (220, 35), get_random_color())
    # 在生成的图片对象中写字符并生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体得到一个字体对象
    font_obj = ImageFont.truetype("static/font/kumo.ttf", 28)
    # 开始生成随机字符串并写到图片上
    tmp_list = []
    for i in range(5):
        u = chr(random.randint(65, 90))  # 生成大写字母
        l = chr(random.randint(97, 122))  # 生成小写字母
        n = chr(random.randint(0, 9))  # 生成数字，要转换成字符串类型
        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20+40*i, 0), tmp, fill=get_random_color(), font=font_obj)
    print("".join(tmp_list))
    print("生成的验证码".center(100, "="))
    # 保存到session
    request.session["valid_code"] = "".join(tmp_list)

    # 不需要保存图片，在内存加载即可
    from io import BytesIO
    io_obj = BytesIO()
    # 将生成的图片保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象中取上一步保存的图片数据
    data = io_obj.getvalue()
    return HttpResponse


# 处理获取到的验证码-图片函数
def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)
