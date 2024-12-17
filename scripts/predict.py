import pickle
from scripts.preprocessing import preprocess_pipe


def load_model():
    with open('./model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Function to make predictions
def predict_job(text):
    model = load_model()
    tfidf_text = preprocess_pipe(text)
    prediction = model.predict(tfidf_text)
    probability = model.predict_proba(tfidf_text)
    fake_probability = probability[0][1]  # Probability of 'Fake' class
    return prediction[0], fake_probability

