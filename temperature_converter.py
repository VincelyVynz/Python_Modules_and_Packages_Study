
def celsius_to_fahrenheit(celsius):
    """
     Convert Celsius to Fahrenheit.

     Args:
         celsius (float): Temperature in Celsius.

     Returns:
         float: Equivalent temperature in Fahrenheit.
     """
    fahrenheit = (9/5) * celsius + 32
    return f"{fahrenheit}°F."

def fahrenheit_to_celsius(fahrenheit):
    """
    Covert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
         float: Equivalent temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5/9
    return f"{celsius}°C."
