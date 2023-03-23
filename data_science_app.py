# Import require libraries
import xgboost as xgb
import streamlit as st
import pandas as pd

# Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model("xgb_model.json")


# Caching the model for faster loading
@st.cache_data
def predict(
    job_title,
    most_used_tool,
    people_employed,
    sector,
    region,
    edu_background,
    edu_level,
    years_experience,
):
    if job_title == "Machine Learning Engineer/Specialist":
        job_title = 2
    elif job_title == "Data Analyst":
        job_title = 0
    elif job_title == "Data Scientist":
        job_title = 1

    if (
        "High-level programming languages (e.g., Python, R, MATLAB, SAS, Julia, JavaScript)"
        in most_used_tool
    ):
        tool_Hig = 1
    else:
        tool_Hig = 0
    if "Mid-level programming languages (e.g., C, C++, C#, Java, Go)" in most_used_tool:
        tool_Mid = 1
    else:
        tool_Mid = 0
    if "Query languages (e.g., SQL, BigQuery)" in most_used_tool:
        tool_Que = 1
    else:
        tool_Que = 0
    if (
        "Advanced visualisation tools (e.g., PowerBI, D3.js, Tableau, Qlik)"
        in most_used_tool
    ):
        tool_Adv = 1
    else:
        tool_Adv = 0
    if (
        "AutoML / Low-code / No-code tools (e.g., PyCaret, TPOT, Google AutoML, Azure ML)"
        in most_used_tool
    ):
        tool_Aut = 1
    else:
        tool_Aut = 0

    if people_employed == "0 (self-employed)":
        people_employed = 0
    elif people_employed == "1-9":
        people_employed = 1
    elif people_employed == "10-24":
        people_employed = 2
    elif people_employed == "25-99":
        people_employed = 3
    elif people_employed == "100-249":
        people_employed = 4
    elif people_employed == "250+":
        people_employed = 5

    if sector == "Consulting":
        sector = 0
    elif sector == "Education/Research":
        sector = 1
    elif sector == "Financial Services":
        sector = 2
    elif sector == "Law":
        sector = 3
    elif sector == "Life Sciences":
        sector = 4
    elif sector == "Public Sector":
        sector = 5
    elif sector == "Tech":
        sector = 6

    if region == "Hovedstaden":
        region = 0
    elif region == "Sjælland":
        region = 3
    elif region == "Syddanmark":
        region = 4
    elif region == "Midtjylland":
        region = 1
    elif region == "Nordjylland":
        region = 2

    if edu_background == "Business/Economics":
        edu_background = 0
    elif edu_background == "Computer Science":
        edu_background = 1
    elif edu_background == "Data Science":
        edu_background = 2
    elif edu_background == "Mathematics/Statistics":
        edu_background = 3
    elif edu_background == "Natural Sciences":
        edu_background = 4
    elif edu_background == "Sefl-taught":
        edu_background = 5

    if edu_level == "Secondary School":
        edu_level = 3
    elif edu_level == "Academy Profession Degree":
        edu_level = 0
    elif edu_level == "Undergraduate":
        edu_level = 4
    elif edu_level == "Masters":
        edu_level = 1
    elif edu_level == "PhD":
        edu_level = 2

    prediction = model.predict(
        pd.DataFrame(
            data={
                "job_title": job_title,
                "people_employed": people_employed,
                "sector": sector,
                "region": region,
                "edu_background": edu_background,
                "edu_level": edu_level,
                "years_experience": years_experience,
                "tool_Adv": tool_Adv,
                "tool_Hig": tool_Hig,
                "tool_Que": tool_Que,
                "tool_Mid": tool_Mid,
                "tool_Aut": tool_Aut,
            },
            index=[0],
        )
    )
    return prediction


st.title("Danish Data Science Salary Predictor")
st.image(
    """https://builtin.com/cdn-cgi/image/f=auto,quality=80,width=752,height=435/https://builtin.com/sites/www.builtin.com/files/styles/byline_image/public/2021-12/machine-learning-examples-applications.png"""
)
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

if st.button("Predict Salary"):
    price = predict(
        job_title,
        most_used_tool,
        people_employed,
        sector,
        region,
        edu_background,
        edu_level,
        years_experience,
    )
    st.success(f"The predicted salary for the candidate is {price[0]:.2f} DKK")
