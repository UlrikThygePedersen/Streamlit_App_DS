# Data Science Salaries Prediction App

This repository contains a [Streamlit](https://streamlit.io/) web application that uses a machine learning model to predict data science salaries based on certain features. The app was built using Python and the scikit-learn library for machine learning.

## Installation
To run this app on your local machine, you will need to have Python 3 installed. You can install the required dependencies by running the following command in your terminal:

```python
pip install -r requirements.txt
```

## Usage
To run the app, navigate to the repository directory in your terminal and run the following command:

```python
streamlit run data_science_app.py
```

This will open a new tab in your web browser with the app running. You can then interact with the app by selecting various options and entering data for the features.

## Features
The app allows you to input various features that may affect data science salaries, including:

* Job Title
* Industry
* Company Size
* Years of Experience
* Education Level

The machine learning model used in this app is a GradientBoostRegressor, which was trained on a dataset of data science salaries and various features.

## Dataset
The dataset used to train the machine learning model was obtained from the [Danish Data Science Association](https://ddsa.dk/). The dataset contains information about data science salaries and various features, such as job title, industry, and years of experience. The dataset was cleaned and preprocessed before being used to train the model.