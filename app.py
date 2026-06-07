from flask import Flask, render_template, request
from algorithms.hill_climbing import run_hill_climbing
from algorithms.simulated_annealing import run_simulated_annealing
from algorithms.genetic_algorithm import run_genetic_algorithm

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        total_hours = int(request.form["hours"])
        algorithm = request.form["algorithm"]

        if algorithm == "hill":
            result = run_hill_climbing(total_hours)

        elif algorithm == "sa":
            result = run_simulated_annealing(total_hours)

        elif algorithm == "ga":
            result = run_genetic_algorithm(total_hours)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)