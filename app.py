
from scripts.predict import predict_job
import pickle
import streamlit as st


def main():
    st.set_page_config(layout="wide")
    st.title("Legit or Scam? Job Posting Analyzer")

    # Input field for job posting
    job_posting = st.text_area("Enter Job Posting", "Type job posting here...", height=215)

    # Submit button
    if st.button("Submit"):
        if job_posting:
            prediction, probability = predict_job(job_posting)
            if prediction == 1:
                st.subheader(f"Prediction: Fake Job")
                st.write(f"Probability of being fake: {probability:.2f}")
            else:
                st.subheader(f"Prediction: Real Job")
                st.write(f"Probability of being real: {1 - probability:.2f}")
        else:
            st.write("Please enter a job posting.")

if __name__ == "__main__":
    main()