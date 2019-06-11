from django.shortcuts import render

# Create your views here.
from django.views import View
from django import http
import re



class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')

        if not all([username,password,password2,mobile,allow]):
            return http.HttpResponseBadRequest('缺少比传参数')

        if not re.match(r'^[a-zA-Z0-9_]{5,20}$', username):
            return http.HttpResponseBadRequest('请输入5-20个字符的用户名')

        if not re.match(r'[0-9A-Za-z]{8,20}$', password):
            return http.HttpResponseBadRequest('请输入8-20位的密码')
        if password != password2:
            return http.HttpResponseBadRequest('两次输入的密码不一致')
        if not re.match(r'^1[3-9]\d{9]$', mobile):
            return http.HttpResponseBadRequest('请输入正确的手机号码')
        if allow != 'on':
            return http.HttpResponseBadRequest('请勾选用户协议')
    
        