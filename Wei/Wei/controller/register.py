from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.urls import reverse

from . import forms
from WeiModel.models import ImsUsers, ImsUsersProfile
import time
import socket

def register(req):
	if req.method == 'POST':

		#获取计算机名
		hostname = socket.gethostname()

		#获取本机ip
		ip = socket.gethostbyname( hostname )

		#获取当前时间戳
		date = int( time.time() )

		#生成机密串
		password = make_password( req.POST['password'] )
		username = req.POST['username']
		nickname = req.POST['nickname']
		realname = req.POST['realname']
		qq = req.POST['qq']

		UserObj = ImsUsers.objects.create(
		 		username = username,
		 		password = password,
		 		salt = 0,
		 		owner_uid = 0,
		 		groupid = 1,
		 		founder_groupid = 0,
		 		type = 1,
		 		status = 2,
		 		joindate = date,
		 		joinip = ip,
		 		lastvisit = date,
		 		lastip = ip,
		 		starttime = date,
		 		endtime = 0,
		 		register_type = 0
		 	)

		if UserObj :
			res = ImsUsers.objects.filter(username=username)
			for var in res:
				uid = var.uid

			UsersProfile = ImsUsersProfile.objects.create(
				uid = uid,
				createtime = date,
				edittime = 0,
				realname = realname,
				nickname = nickname,
				qq = qq,
				vip = 0,
				gender = 0,
				birthyear = 0,
				birthmonth = 0,
				birthday = 0,
				is_send_mobile_status = 0,
				send_expire_status = 0,
				)
			if UsersProfile :
				return HttpResponseRedirect('login')
		return HttpResponse('<h3>注册失败</h3>')
	else:
		registerForm = forms.Forms
		return render(req, 'register/register.html', {'registerForm':registerForm})
