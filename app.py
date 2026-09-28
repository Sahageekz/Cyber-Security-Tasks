from flask import Flask, render_template, request

app = Flask(__name__)

PASSWORD = "527"

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        password = request.form.get("password")

        if password == PASSWORD:
            message = "LOGIN_SUCCESS"
        else:
            message = "Invalid password"

    return render_template("login.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
