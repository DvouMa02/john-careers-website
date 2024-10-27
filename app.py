from flask import Flask, render_template, jsonify

#https://htmldog.com/guides/javascript/
#http://www.htmldog.com/badge1.gif
#https://getbootstrap.com/
#https://css-tricks.com/snippets/html/mailto-links/
#https://mailtolink.me/
#1h 55 min

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Budapest, Hungary',
    'salary': '€3,000,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Prague, Czechia',
    'salary': '€1,000,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Brno, Czechia',
    'salary': '€2,000,000'
  },
  {
    'id': 4,
    'title': 'Data Master',
    'location': 'Ostrava, Czechia'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)