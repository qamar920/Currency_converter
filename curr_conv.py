import requests
import streamlit as st

def exchange_rate(base_curr):    
    url = f"https://api.exchangerate-api.com/v4/latest/{base_curr}"
    response = requests.get(url)
    data = response.json()
    exchange_rates = data['rates']
    if response.status_code == 200:
        return exchange_rates
    else:
        print("Error! couldn't fetch the data.")
        return None

def currency_converter(reporting_curr, amount, base_curr):
    
    """
    This is build to produce a total sales in reporting currency.
    """
    exch_rate = exchange_rate(base_curr)[reporting_curr]
    result = amount/exch_rate
    return result
    
#conv_sales("USD", 1, "PKR")
def main():
    st.title('Currency Converter by QZ')

    col0, col1, col2 = st.columns(3)
    with col1:
        amount = st.number_input('Enter amount to convert', min_value=0.01, step=0.01, value=1.00)
    col3, col4, col5 = st.columns(3)
    with col3:
        from_currency = st.selectbox('From ', exchange_rate('USD').keys())
    with col5:
        to_currency = st.selectbox('To ', exchange_rate('USD').keys())

    if st.button('Convert'):
        converted_amount = currency_converter(from_currency, amount, to_currency)
        st.success(f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')

if __name__ == "__main__":
    main()

