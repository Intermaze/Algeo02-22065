import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tubes Algeo 02 FK ITB</h1><p>Katanya ITB ada faktultas kedokteran ygy</p>"

app.run()