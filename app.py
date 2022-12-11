from flask import Flask, render_template,request, url_for, redirect, session, flash, abort

app = Flask(__name__)
app.secret_key = 'super secret key'

# Páginas 

@app.route("/")
@app.route("/Home")
def index():
    return render_template('Home.html')

@app.route("/Other")
def otherP():
    return render_template('other.html')

@app.route("/Prs")
def prsP():
    return render_template('prs_info.html')

@app.route("/Port")
def portfolio():
    return render_template('portfolio.html')

# Rota para teste
@app.route("/Base")
def pr():
    return render_template('Base.html')


#Bloco para subir o site.
if __name__ == "__main__":
    app.run(debug=True)