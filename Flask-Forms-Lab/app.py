from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Majd","Ayman","Adam", "Raja", "Omar", "Hussin"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user_name = request.form ['username']
		password1 = request.form ['password']
		if username == user_name and password == password1:
				return redirect(url_for('home'))
		else:
				print ("try again -- uncorrect")
				return render_template("login.html")
	

@app.route('/home')  # '/' for the default page
def home():
	return render_template('home.html', facebook_friends=facebook_friends)


@app.route('/friends/<string:name>', methods=['GET', 'POST'])
def friends(name):
	if name in facebook_friends:
		exist = True
		return render_template('friend_exists.html', exist= exist)
	else:
		exist= False
	return render_template('friend_exists.html', n=name, exist= exist)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)