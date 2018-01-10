from django.conf.urls import include,url
from .controller import index,login,register,user,weijk

urlpatterns = [

	#首页
	url( r'^index$', index.index ),

	#登陆
    url( r'^login$', login.login ),

    #注册
    url( r'^register$', register.register ),

    #验证码
    url( r'^captcha$', include('captcha.urls')),

    #用户模块
    #url( r'^user/showOne$', user.showOne),

    #微信
    url( r'^weijkList$', weijk.list),
    url( r'^weijkAdd$', weijk.add),
    url( r'^weijkQun/(.*)$', weijk.qun),
]
