from flask import Flask
from flask import jsonify
import datetime
import holidays

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("")
    return "Hello World! This is a landing page to a sample project showing continuous delivery."


@app.route("/next_business_day/<from_date>")
def next_business_day(from_date):
    from_date = datetime.datetime.strptime(from_date, "%m-%d-%Y")
    ONE_DAY = datetime.timedelta(days=1)
    HOLIDAYS_US = holidays.US()

    next_day = from_date + ONE_DAY
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
        next_day += ONE_DAY
    val = {"Next business day": next_day}
    return jsonify(val)


@app.route("/name/<value>")
def name(value):
    print(f"This was placed in the url: new-{value}")
    val = {"Supplied Name": value}
    return jsonify(val)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
