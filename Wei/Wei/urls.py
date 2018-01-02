from django.conf.urls import include,url
from .controller import index,login,register

urlpatterns = [

	#首页
	url( r'^index$', index.index ),

	#登陆
    url( r'^login$', login.login ),

    #注册
    url( r'^register$', register.register ),

    #验证码
    url( r'^captcha$', include('captcha.urls')),
]
