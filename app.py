from email import message
from math import remainder
from unicodedata import name
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

Registrants = {}

#data 
Fighters = [
    "tony ferguson",
    "conor macgregor",
    "dustin  porier",
    "micheal chandler"]

@app.route("/")
def index():
    # redner index.html and send Fighter to index.html as template {}
    return render_template("index.html", Fighters = Fighters)


@app.route("/favorite", methods=["GET","POST"])
def favorite():
    
    #grub  value of 'name' from index.html and store in variable user_name
    user_name = request.form.get('name')
    
    #grub  value of 'fighter' from index.html and store in variable picked_fighter
    picked_fighter = request.form.get('fighter')
    
    #grub  value of 'ffighter-list' from index.html and store in variable select
    select = request.form.get('fighter-list')


    ###varidation here###

    # if user_name dose not have a value or select value is none 
    if not user_name or select=="none":
        # render error page, have default error message as EROR and send it to error.html
        return render_template('error.html', message = "ERROR")
    # otherwise return success
    return render_template('success.html')




if __name__ == "__main__":
    app.run(debug=True)