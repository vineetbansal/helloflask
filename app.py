from flask import Flask, request, redirect, session, url_for, render_template, abort
from flask.json import jsonify
import os

import slurm
import slurm2


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit")
def submit():
    i = int(request.args.get("i", 1))
    j = int(request.args.get("j", 1))
    t = int(request.args.get("t", 20))
    return jsonify(job_id=slurm.submit(i, j, t))


@app.route("/state/<job_id>")
def state(job_id):
    return jsonify(state=slurm.state(job_id))


@app.route("/result/<job_id>")
def result(job_id):
    return jsonify(result=slurm.result(job_id))


@app.route("/kepler/submit")
def submit2():
    i = int(request.args.get("i", 1))
    j = int(request.args.get("j", 1))
    return jsonify(job_id=slurm2.submit(i, j))


@app.route("/kepler/state/<job_id>")
def state2(job_id):
    return jsonify(state=slurm2.state(job_id))


@app.route("/kepler/result/<job_id>")
def result2(job_id):
    return jsonify(result=slurm2.result(job_id))


@app.route("/hello")
def hello():
    return render_template("hello.html")


if __name__ == '__main__':

    import sys
    host, port = sys.argv[1:]
    app.run(threaded=True, host=host, port=int(port))

