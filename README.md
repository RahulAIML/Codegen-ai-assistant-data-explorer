# CodeGen AI Assistant with data exploration

A simple **AI Coding Assistant** built with **Transformers** and **Streamlit**.

This mini project lets you:
-  Generate Python code from natural language prompts (ChatGPT-style)
-  Upload CSV/XLSX datasets
-  Get quick data summaries with Pandas
-  Visualize your data interactively with Seaborn plots

---

##  Demo

> **Note:** This runs fully locally!  
> Uses the `deepseek-ai/deepseek-coder-1.3b-instruct` model for code generation.

---

##  Features

 **Natural language to code** using a Transformers text-generation pipeline  
 **Interactive data exploration**: upload CSV/XLSX, see Pandas summary, correlations, distributions  
 **Clean Streamlit UI**  
 **Safe**: generated code is displayed but not executed automatically

---

## ⚙ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/codegen-ai-assistant.git
   cd codegen-ai-assistant
## Create virtual environment(optional but good to create)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
## Install dependencies
python -m pip install torch transformers streamlit pandas seaborn matplotlib openpyxl

## Project Structure
.
├── app.py          # Main Streamlit app
├── README.md       # Project README
├── requirements.txt (optional)
└── /venv           # Virtual environment (optional)
## Run the app
streamlit run app.py
