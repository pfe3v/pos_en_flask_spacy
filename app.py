#Flask and spacy integration to 
#Based on work by Susan Li
#https://towardsdatascience.com/building-a-flask-api-to-automatically-extract-named-entities-using-spacy-2fd3f54ebbc6

from flask import Flask,render_template,url_for,request
import re
import pandas as pd
import spacy
#from spacy import displacy
import en_core_web_sm
nlp = spacy.load('en_core_web_sm')
posElements=['NOUN','VERB','ADJ','ADV']


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']
        doc = nlp(rawtext)
        d = []
    for token in doc: #looping through each word in the line
            if str(token.pos_) in posElements: #checking if token matches requirements
                d.append((token.pos_, token.lemma_))   

    uniqList = list(set(d)) #creates an unordered index
    sortUniqList=(sorted(uniqList, key=lambda txt:(txt[1],txt[0]))) #sorts the index
    df = pd.DataFrame(sortUniqList, columns=('pos', 'output'))       
    
    verb = df.loc[df['pos'] == 'VERB']['output']
    noun = df.loc[df['pos'] == 'NOUN']['output']
    adjective = df.loc[df['pos'] == 'ADJ']['output']
    adverb = df.loc[df['pos'] == 'ADV']['output']

    return render_template("index.html",results=noun,results2=verb,results3=adjective,results4=adverb)

if __name__ == '__main__':
    app.run(debug=True)

