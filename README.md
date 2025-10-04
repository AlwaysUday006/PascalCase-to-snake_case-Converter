# 🐍 PascalCase / camelCase → snake_case Converter

This project implements a **Python utility** that converts **PascalCase** or **camelCase** strings into **snake_case** format.  
It also demonstrates how the same project can be converted into a **simple interactive webpage using Streamlit**.

---

## 📖 About
This script automatically converts PascalCase or camelCase into snake_case —  
a naming style commonly used in Python for readability and consistency.

**Examples:**
- **PascalCase** → `ThisIsPascalCase`
- **camelCase** → `thisIsCamelCase`
- **snake_case** → `this_is_snake_case`

**How it works:**
1. Each character is checked one by one.  
2. If a character is **uppercase**, it is preceded by an underscore (`_`) and converted to lowercase.  
3. Other characters remain unchanged.  
4. Leading underscores are removed if present (from the first uppercase letter).

---

## 🚀 Features
- Converts **PascalCase → snake_case**  
- Converts **camelCase → snake_case**  
- Handles uppercase letters intelligently by inserting underscores  
- Strips leading underscores  
- **Simple and beginner-friendly** Python implementation  
- Optional **Streamlit app** for interactive web-based conversion  

---

## 🛠️ How It Works
1. Enter a string in PascalCase or camelCase.  
2. The program processes each character according to the conversion rules.  
3. Outputs the converted string in snake_case.  
4. Optionally, run the Streamlit app to try it on a simple web interface.

---

## 📂 Project Structure
- `case.py` – Core logic for PascalCase/camelCase to snake_case conversion  
- `app.py` – Streamlit web app for interactive conversion  
- `README.md` – Project documentation and instructions  

---

## 🎯 Steps Followed
1. Learned string manipulation and conditional logic in Python.  
2. Implemented the conversion function in `case.py`.  
3. Tested conversion with different PascalCase and camelCase strings.  
4. Created `app.py` for a simple Streamlit web interface.  
5. Documented the project for easy understanding and sharing.

---

## 🌐 Try It on Streamlit
You can try this project instantly here:  
👉 [**PascalCase / camelCase Converter Web App**](https://alwaysuday006-pascalcase-to-snake-case-converter-app-zyccqn.streamlit.app/) 🚀

### ▶️ Run Locally
```bash
# Install dependencies
pip install streamlit

# Run the Streamlit app
streamlit run app.py
