from flask import Flask, render_template

#https://htmldog.com/guides/javascript/
#http://www.htmldog.com/badge1.gif
#https://getbootstrap.com/
#59 minuta

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)