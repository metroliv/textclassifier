import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from dataset import transactions  # Adjust according to your dataset structure and module name

# Download NLTK data if not already downloaded
nltk.download('punkt')

# Load dataset
texts, labels = zip(*transactions.transactions)  # Ensure 'transactions.transactions' correctly loads data

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# Train the classifier
clf = MultinomialNB()
clf.fit(X, labels)

# Save the model and vectorizer
joblib.dump(clf, 'classifier_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

def classify_text(text):
    # Load model and vectorizer
    clf = joblib.load('classifier_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    
    # Transform text to TF-IDF features
    X = vectorizer.transform([text])
    
    # Predict the category
    prediction = clf.predict(X)[0]
    return prediction
