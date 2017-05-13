#-*- coding:utf-8 -*-
import web
from web import form
import model

render = web.template.render("templates")
	
urls = (
	"/(.*)","index"
	#,"(d+)","change"
	)
	
app = web.application(urls,globals())

class index:
	def GET(self,name):
		form = [(u'', u'', u'', u'', u'', u'', u'')]
		name = name + u" 请选择功能"
		#return model.ntno("tname")
		#return form.render()
		return render.postindex(name,form)
	def POST(self,name):
		form = [(u'', u'', u'', u'', u'', u'', u'')]
		i=web.input()
		#return i["menu"]
		# 提交结果为空
		if i["tno"] == u'':
			name = name + u" 请选择功能"
			return render.postindex(name,form)
		tno = (i["tno"],)
		if (i["menu"]!= u"insert") and  (tno not in model.tno()):
			name = name + u"请输入正确的教师号！"
			form = [(u'', u'', u'', u'', u'', u'', u'')]
			return render.postindex(name,form)
	
		if (i["menu"] == u"insert") and (tno in model.tno()):
			name = name + u"该教师号已经存在"	
			return render.postindex(name,form)

		#	else:
		#		name = name + u" 学号不能为空"
		#		return render.postindex(name,form)
		# 判断输入tno是否都为数字
		#for it in i["tno"]:
		#	if (it<u'0')or(it > u'9'):
		#		name= name + u" 请输入正确的教师号！!"
		#		return render.postindex(form,name)
		#k=(i["tno"],)
		#if k not in model.tno():			
		#	if (i["menu"]==u'select')or(i["menu"]==u'delete'):
		#		name= name + u" 请输入正确的教师号！!"
		#		return render.postindex(form,name)
		#	else:
		#		pass
		#else:
		#	if i["menu"]==u'update':
		#		name= name + u" 不能修改教师号！!"
		#		return render.postindex(form,name)
		#	else:
		#		pass
		menu=i["menu"]
		name = name +" "+menu+" success"
		form = model.result(i)
		if form ==[]:
			form = [(u'', u'', u'', u'', u'', u'', u'')]
		return render.postindex(name,form)

if __name__ == "__main__":
    app.run()