from ssl import HAS_TLSv1_1
from flask import Flask, request, render_template, redirect,url_for
from form import contactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dedde'



    
@app.route('/submit' ,methods=['GET','POST'])
def home():
    form = contactForm()
    if form.validate_on_submit():
            return redirect('/success')
    return render_template('index.html', form=form)


@app.route('/success')
def success():
    return 'Thank you for submitting '



if __name__ == "__main__":
    app.run(debug=True)