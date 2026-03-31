import streamlit as st
import joblib
import pandas as pd


st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="💼",
    layout="centered"
)


@st.cache_resource
def load_model():
    return joblib.load("LinearModel.pkl")


model = load_model()

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f8fbff 0%, #eef4ff 100%);
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 850px;
    }
    .title-box {
        background: linear-gradient(135deg, #1f4e79, #3b82f6);
        padding: 28px 24px;
        border-radius: 18px;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.10);
        margin-bottom: 20px;
    }
    .title-box h1 {
        margin: 0;
        font-size: 2.2rem;
    }
    .title-box p {
        margin-top: 8px;
        font-size: 1rem;
        opacity: 0.95;
    }
    .input-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.07);
        border: 1px solid #e5e7eb;
        margin-top: 12px;
    }
    .result-card {
        background: linear-gradient(135deg, #ecfdf5, #d1fae5);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #10b981;
        box-shadow: 0 8px 20px rgba(16,185,129,0.12);
        margin-top: 18px;
    }
    .result-text {
        font-size: 1.8rem;
        font-weight: 700;
        color: #065f46;
    }
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        font-size: 1rem;
        font-weight: 600;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #1e40af);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="title-box">
        <h1>Salary Prediction Web App</h1>
        <p>Predict annual salary using employee details such as experience, performance, gender, and department.</p>
    </div>
""", unsafe_allow_html=True)

department_options = {
    "Creative": "Department_Creative",
    "Environmental Compliance": "Department_Environmental Compliance",
    "Environmental Health/Safety": "Department_Environmental Health/Safety",
    "Facilities/Engineering": "Department_Facilities/Engineering",
    "Green Building": "Department_Green Building",
    "Human Resources": "Department_Human Resources",
    "IT": "Department_IT",
    "Major Mfg Projects": "Department_Major Mfg Projects",
    "Manufacturing": "Department_Manufacturing",
    "Manufacturing Admin": "Department_Manufacturing Admin",
    "Marketing": "Department_Marketing",
    "Product Development": "Department_Product Development",
    "Professional Training Group": "Department_Professional Training Group",
    "Quality Assurance": "Department_Quality Assurance",
    "Quality Control": "Department_Quality Control",
    "Research Center": "Department_Research Center",
    "Research/Development": "Department_Research/Development",
    "Sales": "Department_Sales",
    "Training": "Department_Training"
}

columns_list = [
    'Years', 'Job Rate', 'Gender_Male', 'Department_Creative',
    'Department_Environmental Compliance',
    'Department_Environmental Health/Safety',
    'Department_Facilities/Engineering', 'Department_Green Building',
    'Department_Human Resources', 'Department_IT',
    'Department_Major Mfg Projects', 'Department_Manufacturing',
    'Department_Manufacturing Admin', 'Department_Marketing',
    'Department_Product Development', 'Department_Professional Training Group',
    'Department_Quality Assurance', 'Department_Quality Control',
    'Department_Research Center', 'Department_Research/Development',
    'Department_Sales', 'Department_Training'
]

job_rate_mapping = {
    "1 - Very Low": 1.0,
    "2 - Low": 2.0,
    "3 - Average": 3.0,
    "4.5 - Good": 4.5,
    "5 - Excellent": 5.0
}

st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    years = st.text_input(
        "Years of Experience",
        placeholder="Enter years of experience"
    )

with col2:
    job_rate_display = st.selectbox(
        "Standard Job Rate",
        ["Select Job Rate", "1 - Very Low", "2 - Low", "3 - Average", "4.5 - Good", "5 - Excellent"],
        index=0
    )

col3, col4 = st.columns(2)

with col3:
    gender = st.selectbox(
        "Gender",
        ["Select Gender", "Male", "Female"],
        index=0
    )

with col4:
    department_label = st.selectbox(
        "Department",
        ["Select Department"] + list(department_options.keys()),
        index=0
    )

predict = st.button("Predict Annual Salary")

st.markdown('</div>', unsafe_allow_html=True)

if predict:
    if years.strip() == "":
        st.warning("Please enter Years of Experience.")
    elif job_rate_display == "Select Job Rate":
        st.warning("Please select Standard Job Rate.")
    elif gender == "Select Gender":
        st.warning("Please select Gender.")
    elif department_label == "Select Department":
        st.warning("Please select Department.")
    else:
        try:
            years = int(years)
            job_rate = job_rate_mapping[job_rate_display]

            input_data = pd.DataFrame(0, index=[0], columns=columns_list)

            input_data.at[0, "Years"] = years
            input_data.at[0, "Job Rate"] = job_rate

            if gender == "Male":
                input_data.at[0, "Gender_Male"] = 1

            selected_department_column = department_options[department_label]
            if selected_department_column in input_data.columns:
                input_data.at[0, selected_department_column] = 1

            prediction = model.predict(input_data)[0]

            st.balloons()
            st.markdown(f"""
                <div class="result-card">
                    <div style="font-size: 1rem; color: #065f46; margin-bottom: 8px;">
                        Predicted Annual Salary
                    </div>
                    <div class="result-text">${prediction:,.2f}</div>
                </div>
            """, unsafe_allow_html=True)

            with st.expander("View input summary"):
                st.write({
                    "Years": years,
                    "Job Rate": job_rate_display,
                    "Gender": gender,
                    "Department": department_label
                })

        except ValueError:
            st.error("Please enter a valid whole number for Years of Experience.")
else:
    st.info("Fill in the employee details and click on 'Predict Annual Salary."
            )