import hashlib

from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse

from Seller.models import *

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_username = request.COOKIES.get("username")
        session_username = request.session.get("username")
        if cookie_username and session_username and cookie_username == session_username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Seller/login/")
    return inner

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def register(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email:
            #首先检测email有没有
            user = LoginUser.objects.filter(email = email).first()
            if not user:
                new_user = LoginUser()
                new_user.email = email
                new_user.username = email
                new_user.password = setPassword(password)
                new_user.save()
            else:
                error_message = "邮箱已经被注册，请登录"
        else:
            error_message = "邮箱不可以为空"
    return render(request,"seller/register.html",locals())

import time,datetime
def login(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        code = request.POST.get("valid_code")
        if email:
            # 首先检测email有没有
            user = LoginUser.objects.filter(email=email).first()
            if user:
                db_password = user.password
                password = setPassword(password)
                if db_password == password:
                    #检测验证码
                    #获取验证码
                    # codes = Valid_Code.objects.filter(code_user=email).order_by("-code_time").first()
                    # #校验验证码是否存在，是否过期，是否被使用
                    # now = time.mktime(datetime.datetime.now().timetuple())
                    # db_time = time.mktime(codes.code_time.timetuple())
                    # t = (now - db_time)/60
                    # if codes and codes.code_state == 0 and t <= 5 and codes.code_content.upper() == code.upper():
                        response = HttpResponseRedirect("/Seller/index/")
                    #     response.set_cookie("username",user.username)
                    #     response.set_cookie("user_id", user.id)
                    #     request.session["username"] = user.username
                    #     return response
                    # else:
                    #     error_message = "验证码错误"
                else:
                    error_message = "密码错误"
            else:
                error_message = "用户名不存在"
        else:
            error_message = "邮箱不可以空"
    return render(request,"seller/login.html",locals())
def logout(request):
    response = HttpResponseRedirect("/login/")
    keys = request.COOKIES.keys()
    for key in keys:
        response.delete_cookie(key)
    del request.session["username"]
    return response

@loginValid
def index(request):
    return render(request,"seller/index.html",locals())

@loginValid
def goods_list(request,status,page=1):
    user_id = request.COOKIES.get("user_id")
    user = LoginUser.objects.get(id = int(user_id))
    page = int(page)
    if status == "1":
        goodses = Goods.objects.filter(goods_store = user,goods_status = 1)
    elif status == "0":
        goodses = Goods.objects.filter(goods_store = user,goods_status = 0)
    else:
        goodses = Goods.objects.all()
    all_goods = Paginator(goodses,10)
    goods_list = all_goods.page(page)
    return render(request,"seller/goods_list.html",locals())

@loginValid
def goods_status(request,state,id):
    id = int(id)
    goods = Goods.objects.get(id = id)
    if state == "up":
        goods.goods_status = 1
    elif state == "down":
        goods.goods_status = 0
    goods.save()
    url = request.META.get("HTTP_REFERER","/goods_list/1/1")
    return HttpResponseRedirect(url)

@loginValid
def personal_info(request):
    user_id = request.COOKIES.get("user_id")
    user = LoginUser.objects.get(id = int(user_id))
    if request.method == "POST":
        user.username = request.POST.get("username")
        user.gender = request.POST.get("gender")
        user.age = request.POST.get("age")
        user.phone_number = request.POST.get("phone_number")
        user.address = request.POST.get("address")
        user.photo = request.FILES.get("photo")
        user.save()
    return render(request,"seller/personal_info.html",locals())

@loginValid
def goods_add(request):
    goods_type_list = GoodsType.objects.all()
    if request.method == "POST":
        data = request.POST
        files = request.FILES

        goods = Goods()
        #常规保存
        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        goods.goods_pro_time = data.get("goods_pro_time") #出厂日期格式必须是yyyy-mm-dd格式
        goods.goods_status = 1

        #保存外键类型
        goods_type_id = int(data.get("goods_type"))
        goods.goods_type = GoodsType.objects.get(id = goods_type_id)
        #保存图片
        picture = files.get("picture")
        goods.picture = picture
        #保存对应的卖家
        user_id = request.COOKIES.get("user_id")
        goods.goods_store = LoginUser.objects.get(id = int(user_id))

        goods.save()

    return render(request,"seller/goods_add.html",locals())


def order_list(request,status):
    status = int(status)
    user_id = request.COOKIES.get("user_id")
    store = LoginUser.objects.get(id = user_id)
    store_order = store.orderinfo_set.filter(order_status = status).order_by("-id") #获取店铺对应的订单
    return render(request,"seller/order_list.html",locals())