from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from WeiModel.models import ImsWeixinInfo
import urllib.request
import json

#消息列表
def list(req):
	list = ImsWeixinInfo.objects.all()
	return render(req, 'weijk/list.html', {'content':list})

#获取用户openid列表 群发
def qun(req,xid):
	access_token = token()

	info = ImsWeixinInfo.objects.filter(id=xid)
	for val in info:
		xiao = val.content

	#获取用户列表
	url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='+access_token
	resJson = urllib.request.urlopen( url )
	res = json.loads( resJson.read() )
	data = {'touser':res['data']['openid'],'msgtype':'text','text':{'content':xiao}}
	data = json.dumps(data, ensure_ascii=False)
	data = bytes(data, 'utf8')
	url = 'https://api.weixin.qq.com/cgi-bin/message/mass/send?access_token='+access_token
	request = urllib.request.Request(url)
	result = urllib.request.urlopen(request,data).read()
	res = json.loads( result )
	if res['errcode'] == 0 :
		return HttpResponseRedirect('weijkList')
	return HttpResponse( result )

#添加微信消息
def add(req):
	if req.POST:
		content = req.POST['content']
		weiObj = ImsWeixinInfo( content=content )
		weiObj.save()
		return HttpResponseRedirect('weijkList')
	return render(req, 'weijk/add.html')

#获取token
def token():
	appid = 'wx762eb4fb3d0488b9'
	appsecret = '1b5de8ab4170655de24d48f81dd7c970'
	url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+appsecret
	resJson = urllib.request.urlopen( url )
	res = json.loads( resJson.read() )
	return res['access_token']
