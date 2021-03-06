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
only_emotion =""
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
            for i in emotion_list:
                only_emotion=only_emotion+""+i


'''
#for bar graph
repeat = Counter(emotion_list)
fig, ax1 = plt.subplots()
ax1.bar(repeat.keys(), repeat.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

'''

custom_mask= np.array(Image.open('static/img/twitter_mask.jpg'))
wordcloud = WordCloud(
                      background_color='white',
                      contour_width=3,
                      contour_color='Black',
                      max_font_size=300,
                      min_font_size=25 )

wordcloud.generate(only_emotion)
'''
# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.margins(x=0, y=0)
plt.savefig('graph1.png')
plt.show()
'''

'''
# shaping my word cloud
twitter_mask = np.array(Image.open("static/img/twitter_mask.png"))
print(twitter_mask)  # Values of 255 are pure white, whereas values of 1 are black.
twitter_mask = twitter_mask.reshape((twitter_mask.shape[0], -1), order='F') #3d into 2d
#print(twitter_mask)


def transform_format(val):
    if val == 2:
        return 255
    else:
        return val


transformed_twitter_mask = np.ndarray((twitter_mask.shape[0], twitter_mask.shape[1]), np.int32)
for i in range(len(twitter_mask)):
    transformed_twitter_mask[i] = list(map(transform_format, twitter_mask[i]))
# Check the expected result of your mask
print(transformed_twitter_mask)


wc = WordCloud(background_color="white", max_words=100, mask=transformed_twitter_mask, contour_width=3, contour_color='blue')

# Generate a wordcloud
wc.generate(texxt)

# store to file
wc.to_file("static/img/twitter_mask.png")
'''
# show

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('graph2.png')
plt.show()
