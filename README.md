# Streamlit App Setup and Run Instructions

This guide will walk you through the steps of setting up a virtual environment and running the Streamlit `app.py` in your local machine.

## 1. Install Virtualenv (if not already installed)

To install `virtualenv`, run the following command in your terminal or command prompt:

```bash
pip install virtualenv
```

## 2. Create a new Virtual Environment

once `virtualenv` is installed, create a new environment by running:

```bash
pip virtualenv myenv
```

## 3. Activate the virtual environment

```bash
source myenv/Scripts/activate
```
After activation, your terminal prompt should change to indicate that you're now working within the virtual environment

## 4. Install Dependencies

With the virtual environment activated, install the required dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all the necessary libraries listed in the requirements.txt file for the Streamlit app to run.

## 5. Manually Install the SpaCy model used for preprocessing.

```bash
python -m spacy download en_core_web_sm
```
## 6. Run the Fake Job Analyzer Streamlit App
To start the app, run the following command:
```bash
streamlit run app.py
```

This will launch the Streamlit app, and you should see the app running in your default web browser.




# Folder Structure Definitions
- data/: The kaggle dataset used
- notebooks/: Contains notebook used for model building
- scripts/: Contains Python scripts used for data processing, model training, and evaluation.
- app.py: The Streamlit app for the Fake Job Analyzer.