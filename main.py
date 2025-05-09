import requests
from twilio.rest import Client


# Company name.
STOCK_NAME = "INSERT STOCK NAME"
COMPANY_NAME = "INSERT COMPANY NAME"

# Api Calls and Keys.
STOCK_ENDPOINT = "https://www.alphavantage.co/query" # API endpoint for Alpha Vantage
ALPHAVANTAGE_API_KEY = "INSERT ALPHA AVANTAGE API KEY" # Api Key for Alpha Vantage

NEWS_ENDPOINT = "https://newsapi.org/v2/everything" # API endpoint for News API
NEWSAPI_API_KEY = "INSERT NEW API KEY" # API Key for News API

TWILIO_ACCOUNT_SID = "INSERT TWILIO SID" # Twilio account ID
TWILIO_AUTH_TOKEN = "INSERT TWILIO AUTH TOKEN" # Twilio auth token


# Parameters for the Alpha Vantage API call.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME, # Stock data parameter about the company
    "apikey": ALPHAVANTAGE_API_KEY,
}

# Parameters for the News API call.
news_params = {
    "apiKey": NEWSAPI_API_KEY,
    "qInTitle": COMPANY_NAME, # News parameter about the company
}


# Stock market data.
response = requests.get(url=STOCK_ENDPOINT, params=stock_params) # API call
response.raise_for_status() # Displays request code
stock_data = response.json()["Time Series (Daily)"] # Daily stock data
data_list = [value for (key, value) in stock_data.items()] # List of values from the data

yesterday_data = data_list[0] # Data about yesterday
yesterday_closing_price = yesterday_data["4. close"] # Data about closing price from yesterday

before_yesterday_data = data_list[1] # Data about before yesterday
before_yesterday_closing_price = before_yesterday_data["4. close"] # Data about closing price from before yesterday

closing_price_difference = abs(float(yesterday_closing_price) - float(before_yesterday_closing_price)) # Difference between the
                                                                                                       # closing prices from yesterday and before yesterday with absolute float values

closing_price_difference_percentage = round((closing_price_difference / float(before_yesterday_closing_price)) * 100) # Difference between the
                                                                                                                      # closing prices from yesterday and before yesterday with percentage values


# Check the differences on the closing prices to show the emoji according to the price evaluation.
up_down = None
if closing_price_difference > 0:
    up_down = "🔺" # If it gets higher a triangle pointing up will be shown in the message
else:
    up_down = "🔻" # If it gets lower a triangle pointing down will be shown in the message


# If the closing price difference is above 5% an SMS will be sent.
if abs(closing_price_difference_percentage) > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params) # News API call
    articles = news_response.json()["articles"] # Articles from the company
    three_articles = articles[:3] # Get only the three recent articles
    formatted_articles = [f"{STOCK_NAME}: {up_down}{closing_price_difference_percentage}%\nHeadline: {articles["title"]}.\nBrief:{articles["description"]}" for articles in three_articles] # Formatted news


    for articles in formatted_articles:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)  # Making the API call in Twilio to send the SMS
        message = client.messages.create(
         body=articles,  # SMS Message
         from_="INSERT TWILIO PHONE NUMBER",  # Phone Number from Twilio
         to="INSERT YOUR PHONE NUMBER",  # Your phone number
        )
        print(message.status)
