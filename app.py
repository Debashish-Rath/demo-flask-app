from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:green'>Hello There! This is Debashish here, I modified it for second time in my Local VS Code</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
