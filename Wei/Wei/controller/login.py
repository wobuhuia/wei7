from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password

from WeiModel.models import ImsUsers
from . import forms

#登陆方法
def login(request):
	if request.POST:

		#接收表单数据
		username = request.POST['username']
		password = request.POST['password']

		#查询用户
		res = ImsUsers.objects.filter(username=username)

		#判断用户是否存在
		if res :
			for var in res:
				pwd = var.password
				uid = var.uid

			#验证密码正确性
			if check_password(password, pwd):
				request.session['uid'] = uid
				return HttpResponseRedirect('index')
			else:
				error = '密码错误'
		else:
			error = '用户不存在'
		return HttpResponse('<h3>'+error+'</h3>')
	else:
		loginForm = forms.Forms
		return render(request, 'login/login.html', {'loginForm':loginForm})