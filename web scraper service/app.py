# Author: Leon Samuel
# Date: May 05, 2021
# Description:
"""
Using wikipedia's api to scrape the summary of the article and return json format back.
Program is accessed using: '/https://en.wikipedia.org/wiki/<string:userlink>'
Commented out section note: txt file and json file are created in local directory for formatting return as well as future applicability. 
Note: This will only work with pages with textual summaries, and not with pages that only contain tables.
When running on server - start program inside of virtual machine before deploying
"""

from flask import Flask, request
from flask_restful import Resource, Api
from requests import put, get
import wikipedia
import json 
import os
import urllib

app = Flask(__name__)
api = Api(app)

#class that runs when accessed with port and wikipedia article
class Scrape(Resource):
    def get(self, usertopic):
        print(usertopic)
    
        #obtaining a string of the summary 
        usertopic = urllib.parse.unquote(urllib.parse.unquote(usertopic)) #removes encoded utc-8 formating so symbols are proccessed correctly 
        data = wikipedia.summary('"'+usertopic+'"') #format for summary search is topic in quotation marks
        print(data) 

        return {'data' : data }

# if left as 'Scrap, "/"' then going to the port will run the app, however, I added a varible with a path that will automatically strip the wikipedia link that was passed 
api.add_resource(Scrape, '/https://en.wikipedia.org/wiki/<path:usertopic>/') 


# Listener 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8183))
    app.run(port=port, debug=True)


#https://github.com/osu-cs340-ecampus/flask-starter-app