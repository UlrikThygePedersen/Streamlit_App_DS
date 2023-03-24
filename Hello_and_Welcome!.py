import streamlit as st

# Page config
st.set_page_config(
    page_title="Data Science Salary",
    page_icon="👨‍🔬",
)

st.write("# Welcome to the Data Science Salary Calculator")

st.sidebar.success("Select a dataset above.")

st.markdown(
    """
    This app is a collection is salary information from various sources, all in the field of Data Science!
    ### Currently there are datasets and models from the following sources:
    - [Danish Data Science Association](https://ddsa.dk/)
    - [Reddit Data Science Subreddit](https://www.reddit.com/r/datascience/comments/11xq4oo/data_scientist_salary_in_eu_2023_thread/?utm_source=share&utm_medium=ios_app&utm_name=iossmf&utm_content=1&utm_term=15)
    - [Danish Industrial Association](https://www.danskindustri.dk/)
"""
)
