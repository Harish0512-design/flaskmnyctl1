from flask import Flask,render_template
import moneycontrol.allcmpnydetails as acd
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/')
def firstview():
    result = acd.all_cmpny_details_1()
    return render_template('stock_overview1.html',context=result)

@app.route('/2')
def secondview():
    result = acd.all_cmpny_details_2()
    return render_template('stock_overview2.html',context=result)

@app.route('/3')
def thirdview():
    result = acd.all_cmpny_details_3()
    return render_template('stock_overview3.html',context=result)


if __name__ == '__main__':
    app.run()
