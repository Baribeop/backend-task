from flask import Flask, request, render_template, jsonify



app = Flask("__name__")


@app.route("/details", methods=["GET"])

def user_detail():
    return jsonify
    ({

        "slackUsername" : "Leele Barry Baribeop",
        "backend" : True,
        "age" : 35,
        "bio": "I am a Tutor turned Web developer looking for opportunity to build scalable web app "

    })
if __name__ == "__main__":
    app.run(debug = False)
    