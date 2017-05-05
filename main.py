# -*- coding:utf-8 -*-
import web

urls = (
"/","index"
)

class index:
	def GET(self):
		render=web.template.render("templates")
		return render.index("CBC")
		
if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
	
	
		