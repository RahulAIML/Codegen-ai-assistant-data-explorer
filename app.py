# CodeGen/app.py

import torch
import pandas as pd
from transformers import pipeline
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seed(42)

def load_pipeline():
    return pipeline("text-generation", model="deepseek-ai/deepseek-coder-1.3b-instruct")

pipe = load_pipeline()

st.set_page_config(page_title="CodeGen", layout="wide")
st.title("CodeGen: Your AI Coding Assistant")
st.write(
    """
    Enter instructions like you'd do with ChatGPT.
    Generate Python code, upload a dataset, see summaries, and explore data with Seaborn plots!
    """
)

uploaded_file = st.file_uploader("Upload your CSV or XLSX data", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, encoding='utf-8')
        else:
            df = pd.read_excel(uploaded_file)
    except UnicodeDecodeError:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

    st.write("Preview of your data:")
    st.dataframe(df.head())

    if st.button("Show Data Summary"):
        st.write(df.describe())

    if st.button("Want to See the Distribution Plots?"):
        st.subheader("Seaborn Plots")

        numeric_df = df.select_dtypes(include=['number'])

        if numeric_df.empty:
            st.warning("No numeric columns to plot.")
        else:
            # Pairplot
            st.write("### Pairplot")
            pairplot_fig = sns.pairplot(numeric_df)
            # Use a smaller size for the pairplot
            pairplot_fig.fig.set_size_inches(6, 6)
            st.pyplot(pairplot_fig)

            # Correlation Heatmap
            st.write("### Correlation Heatmap")
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax2)
            st.pyplot(fig2)

            # Distribution Plots
            st.write("### Distribution Plots")
            for col in numeric_df.columns:
                fig, ax = plt.subplots(figsize=(5, 3))
                sns.histplot(numeric_df[col], kde=True, ax=ax)
                ax.set_title(f'Distribution of {col}')
                st.pyplot(fig)

st.subheader("Chat with CodeGen AI")

default_prompt = "Write your instruction here"

prompt = st.text_area("Your instruction:", value=default_prompt, height=150)

if st.button("Generate Code"):
    with st.spinner("Generating..."):
        generated = pipe(
            prompt,
            max_length=512,
            temperature=0.3
        )[0]['generated_text']

    st.subheader("Generated Code:")
    st.code(generated, language="python")
    st.info("For safety, generated code is not auto-executed. Copy & run it yourself!")

st.markdown("---")
st.write("Built with ❤️ by Buddhadeb Bhattacharya")
