from flask import Flask, render_template
from opentok import OpenTok

API_KEY = "!!!"
API_SECRET = "???"

app = Flask(__name__)
opentok = OpenTok(API_KEY, API_SECRET)
session = opentok.create_session()

@app.route("/")
def test():
    key = API_KEY
    session_id = session.session_id
    token = opentok.generate_token(session_id)
    return render_template("index.html", API_KEY=key, session_id=session_id, token=token)

if __name__ == '__main__':
    app.run()