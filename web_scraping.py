from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup
def scrape_news():
    url = "https://mits.ac.in/department/4"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    MitsCst = []
    for MitsCst in soup.find_all("h3", class_="MitsCst"):
        headlines.append(MitsCst.text)
    return MITSCST
@app.route("/")
def home():
 MITSCST = scrape_news()
 return render_template("index.html", headlines= MITSCST)