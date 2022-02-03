from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def app_work():
    pass


@app.route('candidate/<x>')
def candidate_output(x):
    pass


@app.route('/list')
def list_of_candidates():
    pass


@app.route('/search?name=<x>')
def name_search(x):
    pass


@app.route('/skill/<x>')
def skill_search(x):
    pass


if __name__ == "__main__":
    app.run()
