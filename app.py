import streamlit as st

# Function to convert PascalCase or camelCase to snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')


# --- Streamlit App ---
st.set_page_config(page_title="Snake Case Converter", page_icon="🐍")

st.title("🐍 PascalCase / camelCase → snake_case Converter")

st.write(
    "This app converts **PascalCase** or **camelCase** strings into "
    "**snake_case** format."
)

# User input
user_input = st.text_input("Enter a PascalCase or camelCase string:")

# Convert when user provides input
if user_input:
    result = convert_to_snake_case(user_input)
    st.success(f"✅ Converted String: `{result}`")

# Add some examples
st.subheader("📌 Examples")
examples = ["IAmAPascalCasedString", "camelCaseExample", "HelloWorld", "streamLitApp"]
for example in examples:
    st.code(f"{example} → {convert_to_snake_case(example)}")
