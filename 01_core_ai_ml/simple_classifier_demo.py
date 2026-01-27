from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Win a free iPhone",
    "Meeting at 3pm",
    "Limited time offer",
    "Let's have lunch"
]

labels = ["spam", "not_spam", "spam", "not_spam"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

test_email = ["Free coupons waiting"]
X_test = vectorizer.transform(test_email)

prediction = model.predict(X_test)
print(prediction)
