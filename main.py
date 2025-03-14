import streamlit as st
# calculator
def calculator(num1,num2,operator):
  
    if operator == "-":
      result = num1 - num2
    elif operator == "+":
        result = num1 + num2
    elif operator == "*":
        result = num1*num2       
    elif operator == "/":
        if operator != 0:
            result = num1/num2
        else:
            result = "Error:choose another number:" 
    else:
        result = "invalid number:"          

    print("Total Answer:",result)

    return result

st.set_page_config(page_title="Simple Calculator",layout="wide" ,page_icon="🧮")
st.title("Growth Mindset Challenge✅")
st.write("#### Simple Calculator🔢")

num1 = st.number_input("Enter first number:",value=0)
num2 = st.number_input("Enter second number:",value=0)

operator = st.selectbox("Select operator:",["-","+","/","*"])

if st.button("Calculate"):
    result = calculator(num1,num2,operator)
    st.write(f"Result:{result}")