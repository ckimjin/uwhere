from system.core.controller import *
from twilio.rest import TwilioRestClient
import time

account_sid = "AC09a3bc97a1c7e22e2001635496cab1b1" 
auth_token  = "44e38c6f8df76752b0bd5bdee41dc2a4" 
client = TwilioRestClient(account_sid, auth_token)

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
		friends = self.models['Uwhere'].friends_list()
		return self.load_view('profile.html', friends = friends)

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

	def sendMessage(self):
		# friendsList = [int(request.form['number'])]
		# message = request.form['message']
		id = str(session['id'])
		friendsList =[request.form['numbers']]
		outgoing = "+17346220925"
		message = request.form['message']
		for friend in friendsList:
			client.messages.create(body = message, to = friend, from_ = outgoing)
		return redirect ('/uwhere/' + id)
		# sendMessage(outgoing, friendsList, message)