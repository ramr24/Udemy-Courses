# main.py for flask-calculator

import os

from flask import Flask, render_template, request, redirect, url_for, session

from model import SavedTotal

app = Flask(__name__)
app.secret_key = b'\\\x8a\x90O\x8e\rH\x02\xf9Nb\xcf\xc8\xf6\xe5\x8f\xdf\xb80\x83~\xbf\xdbAs'

@app.route("/add", methods=["GET", "POST"])
def add():
    # session['total']
    if 'total' not in session:
        session['total'] = 0
    
    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number
    
    return render_template("add.html", session=session)

@app.route('/save', methods=['POST'])
def save():
    total = session.get('total', 0)
    code = base64.b32encode(os.urandom(8)).decode().strip("=")

    saved_total = SavedTotal(value=total, code=code)
    saved_total.save()

    return render_template("save.html", code=code)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
