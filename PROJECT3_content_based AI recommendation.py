import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 AI Personalization & Recommendation Engine")
st.write("Enter your key skills to match with optimal domain roles.")

# Dataset Setup
data = {
    'Role': [
        'DevOps Engineer', 'Cloud Architect', 'Data Scientist', 
        'Frontend Developer', 'AI/ML Engineer', 'Systems Administrator'
    ],
    'Required_Skills': [
        'python cloud automation linux docker kubernetes CI/CD',
        'cloud AWS azure infrastructure networking security automation',
        'python machine learning data analysis pandas statistics SQL',
        'javascript react HTML CSS web design UI/UX frontend',
        'python deep learning neural networks tensors optimization machine learning',
        'linux networking automation python sysadmin bash security'
    ]
}
df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['Required_Skills'])

# Web Interface User Input Fields
col1, col2, col3 = st.columns(3)
with col1:
    skill1 = st.text_input("Skill / Interest 1", "Python")
with col2:
    skill2 = st.text_input("Skill / Interest 2", "Machine Learning")
with col3:
    skill3 = st.text_input("Skill / Interest 3", "Data")

if st.button("Generate Recommendations"):
    user_inputs = [skill1, skill2, skill3]
    user_profile_str = " ".join(user_inputs)
    
    # Step 1: Vectorization
    user_vector = vectorizer.transform([user_profile_str])
    
    # Step 2: Cosine Similarity Match
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    
    # Step 3: Sorting & Ranking
    df['Match_Score'] = similarity_scores
    results = df.sort_values(by='Match_Score', ascending=False).head(3)
    
    st.subheader("Results:")
    for idx, row in results.iterrows():
        score_pct = round(row['Match_Score'] * 100, 2)
        st.write(f"**Role:** {row['Role']} — **Match:** {score_pct}%")
        st.caption(f"Required Keywords: {row['Required_Skills']}")
        st.divider()
        
