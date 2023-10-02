def format_conversion_result(date, base_currency, target_currency, rate, amount):
    """
    Formats the conversion result as per the specified format.
    
    Args:
        date (str): The date of the conversion.
        base_currency (str): The base currency code.
        target_currency (str): The target currency code.
        rate (float): The conversion rate.
        amount (float): The original amount.
        
    Returns:
        str: The formatted conversion result text.
    """
    converted_amount = amount * rate
    inverse_rate = 1 / rate
    
    result_text = (
        f"The conversion rate on {date} from {base_currency} to {target_currency} was {rate}. "
        f"So {amount} in {base_currency} corresponds to {converted_amount} in {target_currency}. "
        f"The inverse rate was {inverse_rate}."
    )
    
    return result_text
