from django import forms

class Forms(forms.Form):

	#用户名
	username = forms.CharField()
	username.widget.attrs['class'] = 'form-control'
	username.widget.attrs['placeholder'] = '用户名'
	
	#密码
	password = forms.CharField(widget = forms.PasswordInput())
	password.widget.attrs['class'] = 'form-control'
	password.widget.attrs['placeholder'] = '密码'

	#确认密码
	passwordAgain = forms.CharField(widget = forms.PasswordInput())
	passwordAgain.widget.attrs['class'] = 'form-control'
	passwordAgain.widget.attrs['placeholder'] = '确认密码'

	#称呢
	nickname = forms.CharField()
	nickname.widget.attrs['class'] = 'form-control'
	nickname.widget.attrs['placeholder'] = '称呢'

	#真实姓名
	realname = forms.CharField()
	realname.widget.attrs['class'] = 'form-control'
	realname.widget.attrs['placeholder'] = '真实姓名'

	#QQ号
	qq = forms.CharField(required=False)
	qq.widget.attrs['class'] = 'form-control'
	qq.widget.attrs['placeholder'] = 'QQ号'

	#验证码
	#captcha = forms.CaptchaField()