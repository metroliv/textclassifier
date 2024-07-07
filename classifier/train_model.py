import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib  # Import joblib directly
from dataset import transactions

# Download necessary NLTK data
nltk.download('punkt')

# Load dataset
texts, labels = zip(*transactions)

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train the classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Save the model and vectorizer
joblib.dump(clf, 'classifier_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
