# Extract POS from an English text using Flask and Spacy
This python app will return a list of words for parts of speech for an English language text.<p>
The text is pasted in a webpage and returned as 4 separate lists on the page: nouns, verbs, adjectives and adverbs.<p>
Words are returned in lemma form<p>
The app requires Flask, Pandas and Spacy (see the requirements file).<p> 
The app is set up to use the 'en_core_web_sm' model but this can be changed by editing the app.py file.<p>
The app is based on a project by Susan Li which used Spacy to extracted Named Entities from a text.<p>
https://towardsdatascience.com/building-a-flask-api-to-automatically-extract-named-entities-using-spacy-2fd3f54ebbc6

