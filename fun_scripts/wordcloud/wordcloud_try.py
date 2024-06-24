

import numpy as np
import pandas as pd
from os import path
from PIL import Image

from collections import Counter as c
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import requests
"""
text = "For visualization, matplotlib is a basic library that enables many other libraries to run and plot on its base including seaborn or wordcloud that you will use in this tutorial. "+"The pillow library is a package that enables image reading. Its tutorial can be found here. "+"Pillow is a wrapper for PIL - Python Imaging Library. You will need this library to read in image as the mask for the wordcloud."


import io
f = io.open("sampletext3_forwc.txt", mode="r", encoding="utf-8")
text = f.read();
text = re.sub(r'\[.*:','',text)
f.close();


# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud,cmap='gist_rainbow')
plt.axis("off")
plt.show()


#Increase size and clarity

wordcloud = WordCloud(width=800, height=400, background_color='brown').generate(text)
plt.figure( figsize=(20,10) )
plt.imshow(wordcloud)
# Counter
c(text.split()).most_common(17)
"""
## Read text from a website
protein_url = "https://rest.uniprot.org/uniprotkb/Q147X3.txt"

## bs
from bs4 import BeautifulSoup
html_text = requests.get(protein_url).text
soup = BeautifulSoup(html_text, 'html.parser')
lyrs = soup.findAll("div", class_="lcontent")
text = re.sub(r'<.*>','', html_text).replace("\n", " ").replace("Top","")
#wordcloud = WordCloud(width=800, height=400, background_color='brown').generate(text)
wordcloud = WordCloud(width=700, height=1250, background_color='yellow',
                      stopwords=["CHEBI", "ChEBI", "Evidence", "ECO", "RA",
                                 "PubMed", "CC", "Rhea"]).generate(text)
wordcloud.to_file(r"D:\CodingProjects\turtle_projects\fun_scripts\wordcloud.png")
#plt.figure( figsize=(20,10) )
#plt.plot(wordcloud)
"""
## srt fight club
f = io.open("fightclub_srt.txt", mode="r", encoding="utf-8")
text = f.read()
text = re.sub(r'\<.*>','',text).replace("\n", "")
f.close()

with open(r"D:\CodingProjects\func_desc.txt",'r') as f:
    t=f.read()
wordcloud = WordCloud(width=800, height=400, background_color='green',
                      stopwords=["none","description","available","not",
                                 "known","concise"]).generate(t)
plt.figure(figsize=(20,10))
plt.show(wordcloud)
"""