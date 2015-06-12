import bottle

@bottle.route('/')
def home_page():
	return "Hellow world\n"

@bottle.route('/testpage')
def test_page():
	return "This is a testpage"

bottle.debug(True)
bottle.run(host='localhost',port=8080)