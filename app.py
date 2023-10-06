import streamlit as st
import api
import currency
import datetime
import frankfurter

def main():
    st.title("Currency Converter")

    # User input for amount
    amount = st.number_input("Enter the amount to be converted", value=1.0)

    # User selects the base and target currencies
    base_currency = st.selectbox("Select the base currency", api.get_currency_codes())
    target_currency = st.selectbox("Select the target currency", api.get_currency_codes())

    # Fetch latest conversion rate when the button is clicked
    if st.button("Get Latest Conversion Rate"):
        latest_rate = api.get_latest_rate(base_currency, target_currency)
        conversion_date = datetime.date.today().strftime('%Y-%m-%d')
        converted_amount = amount * latest_rate
        inverse_rate = 1 / latest_rate
        result_text = f"The conversion rate on {conversion_date} from {base_currency} to {target_currency} was {latest_rate}. So {amount} in {base_currency} corresponds to {converted_amount} in {target_currency}. The inverse rate was {inverse_rate}."
        st.write(result_text)

    # User selects a date in the past
    past_date = st.date_input("Select a date in the past")

    # Fetch historical conversion rate when a date is selected
    if st.button("Get Historical Conversion Rate"):
        historical_rate = api.get_historical_rate(past_date, base_currency, target_currency)
        formatted_date = past_date.strftime('%Y-%m-%d')
        converted_amount = amount * historical_rate
        inverse_rate = 1 / historical_rate
        result_text = f"The conversion rate on {formatted_date} from {base_currency} to {target_currency} was {historical_rate}. So {amount} in {base_currency} corresponds to {converted_amount} in {target_currency}. The inverse rate was {inverse_rate}."
        st.write(result_text)

if __name__ == "__main__":
    main()
    
