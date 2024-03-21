temperature = 75  # This is the temperature in degrees Fahrenheit
forecast = "sunny"  # This is the weather forecast

if temperature < 80 and forecast != "rainy":
    print("Go outside!")    # This line will only print if the temperature is less than 80 and the forecast is not rainy
else:
    print("Stay inside!")