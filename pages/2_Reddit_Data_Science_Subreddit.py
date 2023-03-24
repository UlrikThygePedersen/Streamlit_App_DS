# Import require libraries
import xgboost as xgb
import streamlit as st
import pandas as pd

# Loading up the Regression model we created
# model = xgb.XGBRegressor()
# model.load_model("xgb_model.json")


# Caching the model for faster loading
@st.cache_data
# Define the function predict, which is called in the Streamlit interface
def predict(location, country, education, education_level, years_of_experience):
    # Encode Streamlit interface inputs to match model features
    if job_title == "Machine Learning Engineer/Specialist":
        job_title = 2
    elif job_title == "Data Analyst":
        job_title = 0
    elif job_title == "Data Scientist":
        job_title = 1

    # Call model.predict on the Streamlit inputs
    prediction = model.predict(
        pd.DataFrame(
            data={
                "location": location,
                "country": country,
                "education": education,
                "education_level": education_level,
                "years_of_experience": years_of_experience,
            },
            index=[0],
        )
    )
    # Return the final model prediction
    return prediction


# Set page configuration to navigate to it
st.set_page_config(page_title="Reddit Data Science Subreddit", page_icon="👨‍🔬")
st.sidebar.header("Reddit Data Science Subreddit")

# Set Streamlit title, image and header for the Streamlit app interface
st.title("Reddit Data Science Subreddit Predictor")
st.image("""https://miro.medium.com/v2/resize:fit:1400/1*cG6U1qstYDijh9bPL42e-Q.jpeg""")
st.header("Enter the candidate information:")

job_title = st.selectbox(
    "What job title best reflects your daily work?",
    [
        "Machine Learning Engineer/Specialist",
        "Data Scientist",
        "Data Analyst",
    ],
)

most_used_tool = st.multiselect(
    "What tools do you use in your daily work?",
    [
        "High-level programming languages (e.g., Python, R, MATLAB, SAS, Julia, JavaScript)",
        "Mid-level programming languages (e.g., C, C++, C#, Java, Go)",
        "Query languages (e.g., SQL, BigQuery)",
        "Advanced visualisation tools (e.g., PowerBI, D3.js, Tableau, Qlik)",
        "AutoML / Low-code / No-code tools (e.g., PyCaret, TPOT, Google AutoML, Azure ML)",
    ],
)

people_employed = st.selectbox(
    "People Employed At Your Workplace?",
    [
        "0 (self-employed)",
        "1-9",
        "10-24",
        "25-99",
        "100-249",
        "250+",
    ],
)

sector = st.selectbox(
    "In which sector do you work?",
    [
        "Consulting",
        "Education/Research",
        "Financial Services",
        "Law",
        "Life Sciences",
        "Public Sector",
        "Tech",
    ],
)

region = st.selectbox(
    "In which Danish region is your office located?",
    [
        "Hovedstaden",
        "Sjælland",
        "Syddanmark",
        "Midtjylland",
        "Nordjylland",
    ],
)

edu_background = st.selectbox(
    "What educational background do you have?",
    [
        "Business/Economics",
        "Computer Science",
        "Data Science",
        "Mathematics/Statistics",
        "Natural Sciences",
        "Self-taught",
    ],
)

edu_level = st.selectbox(
    "What is your highest level of education?",
    [
        "Secondary School",
        "Academy Profession Degree",
        "Undergraduate",
        "Masters",
        "PhD",
    ],
)

years_experience = st.number_input(
    "How many years of relevant full-time work experience do you have?",
    min_value=0.1,
    max_value=12.0,
    value=1.0,
)

# If the button 'Predict Salary' is pressed on the Streamlit app interface,
# the features are sent to the model, a prediction is made and if succesfull,
# the price is returned and displayed
if st.button("Predict Salary"):
    price = predict(location, country, education, education_level, years_of_experience)
    st.success(f"The predicted salary for the candidate is {price[0]:.2f} DKK")
