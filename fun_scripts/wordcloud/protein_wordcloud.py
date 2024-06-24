# import
import requests
import re
from wordcloud import WordCloud

# read text from a website
protein_url = "https://rest.uniprot.org/uniprotkb/Q147X3.txt"
wordcloud_dir= r"D:\CodingProjects\turtle_projects\fun_scripts\wordcloud"

## read url
html_text = requests.get(protein_url).text
print(html_text)
# format text in one line
text = re.sub(r'<.*>','', html_text).replace("\n", " ")
wordcloud = WordCloud(width=700, height=1250, 
                      background_color='beige').generate(text)
wordcloud.to_file(rf'{wordcloud_dir}\wordcloud.png')

# remove unnecessary/repetitive words
wordcloud = WordCloud(width=700, height=1250, background_color='yellow',
                      stopwords=["CHEBI", "ChEBI", "Evidence", "ECO", "RA",
                                 "PubMed", "CC", "Rhea"]).generate(text)
wordcloud.to_file(rf'{wordcloud_dir}\wordcloud_clean.png')