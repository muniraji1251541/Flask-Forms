from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,IntegerField,SubmitField

AI=Flask(__name__)

AI.config['SECRET_KEY']='CsrfToken'

@AI.route('/htmlform',methods=['GET','POST'])
def html_form():
	if request.method=='POST':
		data=request.form
		#return data
		return data['name']
	return render_template('html_form.html')

class Webform(Form):
	name=StringField()
	age=IntegerField()
	submit=SubmitField()

@AI.route('/webform',methods=['GET','POST'])
def web_form():
	form=Webform()
	if request.method=='POST':
		fd=Webform(request.form)
		if fd.validate():
			return fd.data
	return render_template('web_form.html',form=form)


if __name__=='__main__':
	AI.run(debug=True)