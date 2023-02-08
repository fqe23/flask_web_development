from my_app import app

@app.route("/")
@app.route("/hello2")
def hello2():
    return "Hola Circular dos" 

