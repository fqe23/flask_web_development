from flask import Flask,url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return "<p> Hola FQE con recarga de pagina </p>"

@app.route("/hola")
def hola():
    return "<p>Hola desde Hola</p>"
if __name__=="__main__":
    app.run()

@app.route("/saludar")
@app.route("/saludar/<hi>")
@app.route("/saludar/<hi>/<lang>")
def saludar(hi="JESUS", lang="es"):
    return "<p>Hola desde saludar:</p>"+hi+" "+lang
if __name__=="__main__":
    app.run()

@app.route('/primer_html')
@app.route('/primer_html/<name>')
def primer_html(name="FABIAN"):
    return '''
        <html>
            <body bgcolor="green" text="white">
                <img src='/static/img/flask.png'>
                <h1>Hola FLASK</h1>
                <p>Hola %s</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <li>Item 3</li>
                </ul>
            </body>
        </html>
    '''%name

@app.route('/static_file')
def static_file():
     #return "<img src='/static/img/flask.png'>"
     return "<img src='"+url_for("static", filename="img/flask.png")+"'>"
  
@app.route('/primer_template')
@app.route('/primer_template/<name>')
def primer_template(name='Cientifico de datos'):
    return render_template('view.html', vname=name)


if __name__=="__main__":
    app.run()