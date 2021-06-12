# Author: Leon Samuel
# Date: May 05, 2021
# Description:
"""
Using wikipedia's api to scrape the summary of the article into txt file and json file in local directory 
Note: this will only work with pages with textual summaries, and not with pages that only contain tables.
"""

# importing needed modules to run program
import wikipedia
import json


#userlink = "https://en.wikipedia.org/wiki/Stoicism"

def web_scraper(userlink):

    #removing url from user input so that we only grab the specific topic
    usertopic = userlink.split("/")[-1]

    #obtaining a string of the summary 
    data = ("data " + (wikipedia.summary('"'+usertopic+'"'))) #format for summary search is topic in quotation marks


    #sanitizing string before uploading to text file - wasn't able to get a clean file wihtout acsii characters 
    data = data.replace("\n", " ")
    data = data.replace('\"', "\'") #having problems with text having escape characters before double quotes, onyl replacing them with single quotes seems to work.
    data = data.replace('.', ". ") #no space after periods at end of paragraphs


    with open('scraped_data.txt', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


    scraped_txt_file = 'scraped_data.txt'

    # dictionary where the lines from text will be stored
    dic = {}

    # creating dictionary
    with open(scraped_txt_file, encoding='utf8') as fh:
        for line in fh:
            # reads each line, and uses first word as key of key:value pair
            key, summary = line.strip().split(None, 1)
            dic[key] = summary.strip()
        fh.close()

    # creating json file
    with open("scraped_data.json", "w", encoding='utf-8') as out_file:
        #out_file = out_file.decode('string_escape')
        #out_file.data.replace("\\", "")
        json.dump(dic, out_file, ensure_ascii=False, indent = 4, sort_keys = False)
        out_file.close()

    
    #return data


#