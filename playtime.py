'''
All flask applications must import Flask from flask
app isn't a keyword, it's a variable - it could be called anything
it creates an instance of the class Flask (which is the entire framework really)
its is passed the name argument so that it can locate the files relative to the root
it's probably best not to think too deeply about this for now, and just accept it

'''
from flask import Flask
from flask import request
from datetime import datetime
from flask.ext.script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import session
from flask import url_for
from flask import redirect
from flask import flash


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = '2jsh7dgss8ejrg56dhsl37rtrtre7'


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash("Looks like you've changed your name!")
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
	#user_agent = request.headers.get('User-Agent')
	#today = datetime.today()
	return render_template('user.html', name=name)

@app.route('/admin/<user>')
def admin(user):
	return 'this is where the admin shite goes'

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	Submit = SubmitField('Submit')


#Error handling
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500



#the follow line is a conditional that says - only run the server if this app is called directly - not if it's imported
if __name__ == '__main__':
	#app.run(debug=True)
	manager.run()
