from os.path import basename
from random import choice, randint
from flask import Flask, render_template, jsonify, session, url_for, request,redirect, flash
from forex_python.converter import CurrencyRates,CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "springboard"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCE PT_REDIRECTS'] = True
app.debug = True
c = CurrencyRates()
c_codes = CurrencyCodes()

@app.route('/')
def home_page():    
    return render_template("home.html")

@app.route('/?')
def reset():
    return redirect('/')
 
@app.route('/checkinputs', methods=['POST','GET'])
def check_inputs():
    global start
    global start_currency
    global to
    global to_currency
    global amount
    amount = request.args['amount']
    start = request.args.get('start').upper()
    to = request.args.get('to').upper()
    to_currency = c_codes.get_currency_name(to)
    to_symbol = c_codes.get_symbol(start)
    start_symbol = c_codes.get_currency_name(to)
    print('symbol test',start_symbol,to_symbol,type(amount))
    start_currency = c_codes.get_currency_name(start)
    if(start == "" or to_symbol == None):
        flash(f"invalid input {start}")
    if(to == "" or start_symbol == None):
        flash(f"invalid input {to}")    
    if amount == False:
        flash(("please enter amount to convert"))
    elif amount == None:
        flash("invalid amount to convert")
    elif isinstance(int(amount), int) ==False:
        flash("please enter a number in digits")
    if start_currency and to_currency and amount:#!= False or None:
        int_amount = int(amount)
        result_code = round(c.convert(start,to,int_amount), 2)
        result_symbol = c_codes.get_symbol(to)
        return render_template("start_conversion.html", converted_symbol = result_symbol, converted_amount =  result_code) 
    return render_template('index.html')
#@app.route('/flashes', methods=['POST','GET'])
#def flashes():

     
