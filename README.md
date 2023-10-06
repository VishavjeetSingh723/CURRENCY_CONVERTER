#Currency Converter - A Web App using Streamlit


## AUTHOR

### Student's Name -  Vishavjeet Singh
### Student ID     -  24895346
### E-mail         -  singhvishavjeet723@gmail.com


## Project Overview

In this project, our aim is to develop a web app in Python using Streamlit that performs currency conversion using data fetched from the [Frankfurter API](https://www.frankfurter.app/). The app allows users to select two currencies, an amount to be converted, and a date in the past (optional) to retrieve conversion rates and calculate the inverse conversion rate.

This project is divided into the following multiple python files-

- `app.py`        : Main Streamlit application script for managing user inputs and displaying results.
- `api.py`        : Python script for making API calls to the Frankfurter API.
- `frankfurter.py`: Python script containing functions for interacting with the Frankfurter API.
- `currency.py`   : Python script containing functions for formatting conversion results.
- `README.md`     : Documentation file providing details about the project, functions, and instructions 
                    for running the web app.



## Functions-


### `frankfurter.py`

- `get_currency_codes()`: Fetches the list of available currency codes from Frankfurter API. Returns a dictionary of currency codes and their names.

- `get_latest_rate(base_currency, target_currency)`: Fetches the latest conversion rate for the specified currency codes. Returns the conversion rate.

- `get_historical_rate(date, base_currency, target_currency)`: Fetches the historical conversion rate for the specified date and currency codes. Returns the conversion rate.


### `currency.py`

- `format_conversion_result(date, base_currency, target_currency, rate, amount)`: Formats the conversion result as per the specified format. Returns a formatted text string.


### `app.py`

- Main Streamlit application script that integrates API calls and user interface components.


## Usage -

To run the Currency Converter web app:

1. Ensure you have Python and the required libraries installed.

2. Open a terminal and navigate to the project directory.

3. Run the following command:
     streamlit run app.py

     
4. The Streamlit web app will open in your default web browser( it runs better in chrome). You can select currencies, enter an amount, and retrieve conversion rates.

## Example-

![Currency Converter App Screenshot]

## Dependencies

- Python 3.11
- Streamlit
- Requests (for making HTTP requests)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file attached with this project to find out more details.


# Thanks for reading
## Vishavjeet Singh
---


