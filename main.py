import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(
    page_icon="✨",
    page_title="Digital CV | Bhargavesh Dakka",
)


#CSS Stylings
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


Name = "BHARGAVESH DAKKA"
Description = """
A Data Science Enthusiatic looking for a role in a Esteemed Organization where I can utilize my academic skills to help organization in data-driver decision-making process while improving my skills.
"""
Email = "bhargaveshdakka@gmail.com"

Social_media = {
    "LinkedIn": "https://www.linkedin.com/in/bhargavesh-dakka",
    "GitHub"  : "https://github.com/bhargavesh-dakka",
    "Kaggle"  : "https://www.kaggle.com/bhargaveshdakka",
    "Hacker Rank" : "https://www.hackerrank.com/21695a3202"
}

Projects = {
    "Crop Analysis and Pediction":"https://tinyurl.com/crop-analysis-prediction",
    "Loan Prediction":"https://github.com/bhargavesh-dakka/LoanPrediction.git",
    "Breast Cancer Prediction":"https://github.com/bhargavesh-dakka/Breasr-Cancer-Prediction.git",
    "PIP Packages": "https://github.com/bhargavesh-dakka/PIP-Package.git",
    "Data Analysis Project":"https://github.com/bhargavesh-dakka/Uber-Data-Analysis.git",
    "Web Scraping Project":"https://github.com/bhargavesh-dakka/Women-Premier-Leauge-Scrape.git",
    "Image to Pencil Sketch" :"https://github.com/bhargavesh-dakka/Image-to-Pencil-Sketch.git"
}


with open("BhargaveshDakkaResume.pdf","rb") as pdf_file :
    resume = pdf_file.read()
profile_pic = Image.open("profile.jpg")

col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label="Download Resume",
        data=resume,
        file_name="BhargaveshDakkaResume.pdf",
        mime="application/octet-stream",
        use_container_width=True
    )
    st.write("📧","bhargaveshdakka@gmail.com")

st.divider()
st.write("#")
cols = st.columns(len(Social_media))
for index, (platform,link) in enumerate(Social_media.items()):
    with cols[index]:
        st.markdown(f"[{platform}]({link})")
st.write("#")
st.divider()

st.write("#")
st.subheader("Education")
st.table(pd.DataFrame({"Degree":pd.Series(["B.Tech(Data Science)",'Diploma CSE','SSC (X)']),
                       "College/Institute":pd.Series(["Madanapalle Institute of Technology and Science",'Sree Vidyanikethan Engineering College, A.Rangampet','ZPH School NP Kunta']),
                       "CGPA/Percentage":pd.Series(["8.51",'87.1','10.0'])
                       },index=None
                    )
        )

st.divider()
st.write("#")
st.header("Hard Skills")
st.write("""
- 🧑‍💻 Programming : Python, SQL, J2SE, Data Structures(Basics)
- 📊 Data Science : Numpy, Pandas, Matplotlib, Seaborn, Plotly, Scikit-Learn, Streamlit, OpenCV
- 📈 Data Visualizatoin : Power BI, Tableau, MS Excel, Looker Studio, Matplotlib, Seaboorn
- 🕸️ Web Scraping : BeautifulSoup, Requests, Selenium
- 🤖 Machine Learning : Supervised, Un-Supervised Machine learning
- 📊 Data Analysis : Exploratory Data Analysis, Data Cleaning, Data Preprocessing, Data Visualization
""")

st.divider()
st.write("#")
st.subheader("Projects & Accomplishments")
for projects,links in Projects.items():
    st.write(f"- 🏆 [{projects}]({links})")

st.divider()
st.write("#")
st.subheader("Certifications and Trainings")
st.write("""
- 📜 [Google Data Analytics](https://www.coursera.org/account/accomplishments/specialization/certificate/TC7UU95XB2ZF)
- 📜 [IBM Data Science](https://www.coursera.org/account/accomplishments/specialization/certificate/RSW23M32ZCKH)
- 📜 [Google IT Automation with Python](https://www.coursera.org/account/accomplishments/specialization/certificate/JEWD7G2KUV85)
- 📜 [Hacker Rank Python Certificate](https://www.hackerrank.com/certificates/30a4765dcf6a)
- 📜 [Hacker Rank SQL Certificate](https://www.hackerrank.com/certificates/96f40fcb7add)
""")