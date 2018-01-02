from django.shortcuts import render
from django.http import HttpResponse

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
			
		return HttpResponse(data)
	else:
		loginForm = forms.Forms
		return render(request, 'login/login.html', {'loginForm':loginForm})