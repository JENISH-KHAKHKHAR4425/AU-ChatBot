from flask import Flask, render_template, request, redirect, session, jsonify
import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
from chatbot import get_response

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-deploy"

# Firebase Admin
cred = credentials.Certificate("atmiya-university---chatbot-firebase-adminsdk-fbsvc-664d935bd8.json")
firebase_admin.initialize_app(cred)

# ---------------- HOME ----------------
@app.route("/")
def home():
    if "uid" in session:
        return redirect("/index")
    return redirect("/login")

# ---------------- LOGIN ----------------
@app.route("/login")
def login():
    if "uid" in session:
        return redirect("/index")
    return render_template("login.html")

# ---------------- SIGNUP ----------------
@app.route("/signup")
def signup():
    if "uid" in session:
        return redirect("/index")
    return render_template("signup.html")

# ---------------- FIREBASE TOKEN VERIFY ----------------
@app.route("/firebase-login", methods=["POST"])
def firebase_login():
    data = request.get_json()
    id_token = data.get("idToken")

    if not id_token:
        return jsonify({"error": "Token missing"}), 400

    try:
        decoded_token = firebase_auth.verify_id_token(id_token)

        session["uid"] = decoded_token["uid"]
        session["email"] = decoded_token.get("email", "")
        session["name"] = decoded_token.get("name", "User")

        return jsonify({"status": "success", "name": session["name"]})

    except Exception as e:
        print("Firebase error:", e)
        return jsonify({"error": "Invalid token"}), 401

# ---------------- INDEX ----------------
@app.route("/index")
def index():
    if "uid" not in session:
        return redirect("/login")
    return render_template("index.html", name=session.get("name"))

# ---------------- CHAT ----------------
@app.route("/chat", methods=["POST"])
def chat():
    if "uid" not in session:
        return jsonify({"response": "Please login first"}), 401

    msg = request.form.get("message", "")
    return jsonify({"response": get_response(msg)})

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
