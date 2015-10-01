from system.core.controller import *

class Uwheres(Controller):
	def __init__(self, action):
		super(Uwheres, self).__init__(action)
		self.load_model('Uwhere')

	def index(self):
		if 'name' in session:
			session.pop('name')
		else:
			pass
		return self.load_view('index.html')

	def profile(self, id):
		return self.load_view('profile.html')

	def login_page(self):
		return self.load_view('login.html')

	def register_page(self):
		return self.load_view('register.html')

	def register(self):
		session['name'] = request.form['name']
		user_info = {
			'name': request.form['name'],
			'email': request.form['email'],
			'phone': request.form['phone'],
			'password': request.form['password'],
			'cpassword': request.form['cpassword']
		}
		reg_user = self.models['Uwhere'].register_user(user_info)
		if reg_user['errors'] == True:
			session['id'] = reg_user['user']['id']
			id = str(session['id'])
			return redirect('/uwhere/' + id)
		else:
			for message in reg_user['errors']:
				flash(message, 'regis_errors')
			return redirect('/registerpage')

	def logging(self):
		user_info = {
			'email': request.form['loginemail'],
			'password': request.form['loginpassword']
		}
		login = self.models['Uwhere'].login_user(user_info)
		if login['status'] == True:
			session['id'] = login['user']['id']
			session['name'] = login['user']['name']
			session['email'] = login['user']['email']
			id = str(session['id'])
			return redirect('/uwhere/' + id)
		else:
			for message in login['errors']:
				flash(message, 'regis_errors')
			return redirect('/loginpage')

	def logout(self):
		return redirect('/')