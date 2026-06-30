from flask import Flask, render_template
from services.log_reader import read_logs

app = Flask(__name__)

@app.route("/")
def home():

    collector_logs = read_logs("collector")
    analyzer_logs = read_logs("analyzer")
    decision_logs = read_logs("decision")
    notifier_logs = read_logs("notifier")

    return render_template(
        "index.html",
        collector_logs=collector_logs,
        analyzer_logs=analyzer_logs,
        decision_logs=decision_logs,
        notifier_logs=notifier_logs
    )

if __name__ == "__main__":
    app.run(debug=True)