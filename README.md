# Salary Prediction  ML Web App(Deployed) 
Streamlit ML Web App for predicting employee annual salary using Linear Regression model trained on comprehensive HR dataset. Predicts salary based on years of experience, job performance, gender, and department. Deployed with production-ready Streamlit interface.

✨ Features

Interactive UI: User-friendly Streamlit app with dropdowns and sliders

Real-time Predictions: Instant salary predictions using trained Linear Regression model

Model Performance: R² Score ~0.85+ on test data

Production Ready: Cached model loading for optimal performance

Dataset: 689 employee records with 15+ features

📊 Live Demo

🔗 Deployed App: [Render Cloud/Share](https://salary-predictor-ml-web-app.onrender.com/)
🌐 GitHub Repo: [akmishra-001/Salary-Prediction](https://github.com/akmishra-001/Salary-Prediction-Deployed-Project-March-2026.git)

🛠 Tech Stack

🤖 ML Framework: scikit-learn (Linear Regression)
🌐 Web App: Streamlit
📊 Data Processing: pandas, numpy
📦 Model Persistence: joblib (.pkl)
📈 Visualization: matplotlib/seaborn
🚀 Quick Start (Local)

Prerequisites
Python 3.8+

Git

Clone & Setup
bash
git clone https://github.com/akmishra-001/Salary-Prediction-Deployed-Project-March-2026.git
cd Salary-Prediction-Deployed-Project-March-2026
Install Dependencies
bash
pip install -r requirements.txt
Note: Add these missing files first!
text
 LinearModel.pkl (trained model)
 requirements.txt
✅ Available: App-2.py, Analysis_Modeling_LR.ipynb, Employees-3.csv,  LinearModel.pkl (trained model)
 requirements.txt

Run App
bash
streamlit run App-2.py
App opens at: https://salary-predictor-ml-web-app.onrender.com/

📁 Project Structure

text
├── App-2.py              # Main Streamlit app
├── Analysis_Modeling_LR.ipynb  # Complete ML pipeline
├── Employees-3.csv       # Training dataset (689 records)
├── LinearModel.pkl       # 🆕 ADD: Trained model (generate from notebook)
├── requirements.txt      # 🆕 ADD: Dependencies list
└── README.md            # This file!
🔬 Model Details

Linear Regression Model trained on key features:

Years of Experience

Job Rate (Performance)

Gender (One-hot encoded)

Department (21 categories, one-hot encoded)

Performance Metrics:

text
R² Score: ~0.85
Features: 22 total (after encoding)
Dataset: 689 samples
Target: Annual Salary ($9K - $41K range)
🎯 How to Generate Missing Files
1. Create LinearModel.pkl
bash
# Run the notebook to train & save model
jupyter notebook Analysis_Modeling_LR.ipynb
# Last cells save: joblib.dump(model, 'LinearModel.pkl')
2. Create requirements.txt
text
streamlit==1.28.0
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
joblib==1.3.2

📈 Sample Predictions

Experience	Job Rate	Gender	Department	Predicted Salary
7 years	3.0	Male	Quality Control	~$25,000 
5 years	1.0	Male	Quality Control	~$38,000 
8 years	2.0	Female	Mfg Projects	~$30,000 
🔍 Dataset Insights

📊 Total Records: 689 employees
🌍 Countries: Egypt, Saudi Arabia, UAE, Syria
🏢 Departments: 21 unique (Quality Control most common)
💰 Salary Range: $9,648 - $41,400 annually
👥 Gender: Mixed (Male/Female)
📈 Experience: 5-10 years dominant
🏗 Deployment Options
Render Cloud (Free)
Push to GitHub

Auto-deploys on push!

Heroku / Railway
text
Procfile: web: streamlit run App-2.py --server.port=$PORT --server.address=0.0.0.0
🤝 Contributing
Fork the repo

Create feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push (git push origin feature/amazing-feature)

Open Pull Request

📄 License
MIT License - Free to use, modify, deploy! 🚀

👨‍💻 Author
Abhishek Mishra
