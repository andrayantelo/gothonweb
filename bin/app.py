import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greetings = "FOO"
        return render.foo(greeting = greetings)
        
if __name__ == "__main__":
    app.run()
