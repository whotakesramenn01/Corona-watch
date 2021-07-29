import requests
import json
from flask import Flask, render_template

app = Flask(__name__)
#Api data getting
response = requests.get('https://corona.lmao.ninja/v2/countries/')

#Checking
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

#API sorting
response_dict = response.json()
rawData = json.dumps(response.json())
data = json.loads(rawData)

profiles = []
for x in data:
    profiles.append(x)

#Routing to table
@app.route("/")
def index():
    return render_template("theChotWatch.html",data=profiles)
if __name__ == "__main__":
        app.run()