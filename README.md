# Streamlit App Setup and Run Instructions

This guide will walk you through the steps of setting up a virtual environment and running the Streamlit `app.py` in your local machine.

## via `virtualenv`
### 1. Install Virtualenv (if not already installed)

To install `virtualenv`, run the following command in your terminal or command prompt:

```bash
pip install virtualenv
```

### 2. Create a new Virtual Environment

once `virtualenv` is installed, create a new environment by running:

```bash
pip virtualenv myenv
```

### 3. Activate the virtual environment

```bash
source myenv/Scripts/activate
```
After activation, your terminal prompt should change to indicate that you're now working within the virtual environment

### 4. Install Dependencies

With the virtual environment activated, install the required dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all the necessary libraries listed in the requirements.txt file for the Streamlit app to run.

### 5. Manually Install the SpaCy model used for preprocessing.

```bash
python -m spacy download en_core_web_sm
```
### 6. Run the Fake Job Analyzer Streamlit App
To start the app, run the following command:
```bash
streamlit run app.py
```

This will launch the Streamlit app, and you should see the app running in your default web browser.

## via `Docker`

### 1. Build the Docker Image 
```bash
docker build -t <image_name> . 
```

### 2. Run the Container 
```bash
docker run -p 8501:8501 <image_name>
```
Then visit http://localhost:8501 in your browser.


---
# Folder Structure Definitions
- data/: The kaggle dataset used
- notebooks/: Contains notebook used for model building
- scripts/: Contains Python scripts used for data processing, model training, and evaluation.
- app.py: The Streamlit app for the Fake Job Analyzer.



#### Sample Fake Job Listing: 
1.
```
No interview required - guaranteed acceptance!
        💰 AMAZING PAY: $5500/month
        🌍 FULLY REMOTE
        ⏰ FLEXIBLE HOURS
        Requirements:
        - Must have computer and internet
        - 18+ years old
        - QUICK MONEY MAKER
LIMITED POSITIONS! ACT NOW!
```

2.
```
Immediate start with no interview required! Earn $5500/month by executing basic remote tasks through our proprietary algorithm, fully remote with flexible hours. Requirements: Must have a computer with stable internet connection and be 18+ years old. Quick income opportunity via our seamless backend integration. Limited positions available – Apply now using the /quickstart API!
```

3.
```
Immediate Hiring – No Interview Required!
Earn $9500/month working from home as a Call Center Representative.
Fully Remote – Flexible Hours, Start Now!
Requirements:

Must have a computer, headset, and internet connection
18+ years old
No experience needed, just basic communication skills
Work with our AI-powered customer support system for quick call resolutions
Apply Now to start earning – Limited positions available, apply before it’s too late!
Guaranteed approval – click to activate your account!
```