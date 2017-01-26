from app import app, db
from flask import request, render_template
import json
from app.models import HTML
import requests
import lxml.html

#This is going to be the splash page
@app.route("/scrape",methods=["GET","POST"])
def scrape():
    page = requests.get("https://xkcd.com/").text
    html = lxml.html.fromstring(page)
    links = html.xpath("//a/@href")
    new_page = HTML(page,json.dumps(links))
    db.session.add(new_page)
    db.session.commit()
    return "scraped"

@app.route("/", methods=["GET","POST"])
def index():
    pages = [elem.page[:10] for elem in HTML.query.all()]
    total_links = sum([len(elem.links.split(",")) for elem in HTML.query.all()])
    return render_template("index.html", pages=pages, total_links=total_links)

