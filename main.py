import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image


# reading text file
text = open("my_tweets.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

emotion_list = []
only_emotion = ""
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
            for i in emotion_list:
                only_emotion=only_emotion+""+i
print(only_emotion)

custom_mask = np.array(Image.open('static/img/twitter_mask.png'))
wordcloud = WordCloud(
                      background_color='white',
                      mask=custom_mask,
                      contour_color='Blue',
                      contour_width=3,
                      max_font_size=200,
                      min_font_size=2,
                      repeat=True, scale=4 )

wordcloud.generate(only_emotion)

# show

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('graph2.png')
plt.show()


plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.margins(x=0, y=0)
plt.savefig('graph1.png')
plt.show()