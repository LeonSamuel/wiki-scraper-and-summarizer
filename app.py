#Author: Leon Samuel
#Class: Databases 
#Description: A site that will display a summary of the Wikipedia article the user posts. 
#    The user is able to set the length of the summary, otherwise it will return a 1 setence summary.

from flask import Flask, render_template, request, redirect, url_for, redirect, jsonify, make_response
import json
from requests import put, get, post
import web_scraper
app = Flask(__name__)

@app.route('/')
@app.route('/home' , methods=['POST', 'GET']) #both routes will go to the same function below
def home():        
    return render_template('home.html')

@app.route('/shorten', methods=['POST', 'GET'])
def shorten():
    #will grab the users link and num of lines for summary from home page
    wikilink = request.form.get('wikilink') #stores the link that the user provided
    num_of_requested_lines = request.form.get('numoflines')
    if num_of_requested_lines == "":
        num_of_requested_lines = 1
    
    wikidata = web_scraper_call(wikilink)
    summary_text = summarizer_call(wikidata, num_of_requested_lines)

    #renders page with text obtained from services
    return render_template('shorten.html', wikidata=summary_text)
    

def web_scraper_call(wikilink):    
    #uses service on flip server that will return the summary paragraph of the wikipedia page selected
    jsonwiki = get("http://flip3.engr.oregonstate.edu:8183/"+wikilink).json()
    print(jsonwiki) #for testing what is stored

    #storing value from json formated jsonwiki
    for key, value in jsonwiki.items():
        wikidata = value #only need the value from the only pairing in the file
        return wikidata

def summarizer_call(wikidata, num_of_requested_lines):
    #uses service on flip server that to return a summary of the text passed
    api_url = "http://flip1.engr.oregonstate.edu:4444/api"
    api_params = {"type": "text", "input": wikidata, "length": num_of_requested_lines}
    summary = get(url=api_url, params=api_params).json()
    
    #storing value stored in json format
    for key, value in summary.items():
        if key == 'summary':
            summary_text = value #only need the value from the only pairing in the file
            return summary_text
        
if __name__ == '__main__':
    app.run(debug=True)
