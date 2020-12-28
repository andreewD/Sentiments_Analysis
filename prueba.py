from textblob import TextBlob
analysis = TextBlob("This table is black")
print(analysis.sentiment)

print(analysis.tags)
print(analysis.translate(to='es'))

print(dir(analysis))