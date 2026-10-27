from flask import Flask

app = Flask(__name__, static_folder="static", stactic_url_path="")


@app.route("/")
def inicial():
    return app.send_static_file("index.html")

if __name__ =="__main__":
    app.run(debug=True)