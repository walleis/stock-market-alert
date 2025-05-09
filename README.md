# Stock News Alert

## Overview

This Python script monitors the stock price of a specified company using the Alpha Vantage API. It compares the closing price of the stock from yesterday to the day before yesterday. If the percentage difference in closing prices is greater than a defined threshold (default is 5%), the script fetches the top 3 recent news headlines related to a specified company from the News API and sends an SMS notification to a specified phone number via the Twilio API, including the stock price change and the news headlines.

## Features

* **Stock Price Monitoring:** Fetches daily stock price data for a specified company from the Alpha Vantage API.
* **Significant Price Change Detection:** Calculates the percentage difference in the closing price between the last two trading days and triggers an alert if the change exceeds a configurable threshold (default: 5%).
* **Relevant News Retrieval:** If a significant price change is detected, the script fetches the top 3 recent news articles related to specified company from the News API.
* **SMS Notification with Stock and News:** Sends an SMS message via the Twilio API containing:
    * An emoji indicating whether the stock price went up (🔺) or down (🔻).
    * The percentage difference in the closing price.
    * The headline and a brief description of the top 3 recent news articles about specified company.
* **Configurable Stock and Threshold:** The stock ticker symbol, company name for news search, and the percentage change threshold can be easily modified in the script.

## How to Use

1.  **Prerequisites:**
    * **Python 3:** Ensure you have Python 3 installed on your system.
    * **`requests` Library:** Install the `requests` library for making HTTP requests:
      ```bash
      pip install requests
      ```
    * **`twilio` Library:** Install the `twilio` library for sending SMS messages:
      ```bash
      pip install twilio
      ```
    * **Alpha Vantage API Key:** Sign up for a free API key at [Alpha Vantage](https://www.alphavantage.co/).
    * **News API Key:** Sign up for a free API key at [News API](https://newsapi.org/).
    * **Twilio Account:** Sign up for a Twilio account at [Twilio](https://www.twilio.com/). You will receive an Account SID and an Auth Token. You will also need a Twilio phone number.

2.  **Configuration:**
    * **Open `main.py` (or the name you saved the script as) and modify the following variables:**
        * `ALPHAVANTAGE_API_KEY`: Replace `"YOUR_ALPHAVANTAGE_API_KEY"` with your actual Alpha Vantage API key.
        * `NEWSAPI_API_KEY`: Replace `"YOUR_NEWSAPI_API_KEY"` with your actual News API key.
        * `TWILIO_ACCOUNT_SID`: Replace `"YOUR_TWILIO_ACCOUNT_SID"` with your Twilio Account SID.
        * `TWILIO_AUTH_TOKEN`: Replace `"YOUR_TWILIO_AUTH_TOKEN"` with your Twilio Auth Token.
        * `from_`: Replace `"TWILIO NUMBER` with your Twilio phone number.
        * `to`: Replace `"YOUR PHONE NUMBER"` with the recipient's phone number (including the country code).
        * `STOCK_NAME`: Replace `"TSLA"` with the desired stock ticker symbol (e.g., "AAPL", "GOOGL").
        * `COMPANY_NAME`: Update `"Tesla Inc"` with the full name of the company corresponding to the `STOCK_NAME` for more relevant news (e.g., "Apple Inc", "Alphabet Inc").

3.  **Run the script:** Execute the Python script:
    ```bash
    python main.py
    ```

    The script will fetch the stock data, compare the closing prices, and if the percentage difference is greater than the defined threshold, it will fetch the latest news and send an SMS notification. You will see the status of the SMS message printed in the console.

## Project Structure

The project consists of a single Python file (e.g., `main.py`) which contains all the logic for fetching stock data, news, and sending SMS notifications.

## Code Overview

* **Import Libraries:** Imports the `requests` library for making HTTP requests to the Alpha Vantage and News APIs, and the `twilio.rest.Client` for interacting with the Twilio API.
* **API Keys and Auth Tokens:** Defines variables to store the API keys and Twilio credentials. **Remember to replace the placeholder values with your actual credentials.**
* **API Endpoints:** Defines the URLs for the Alpha Vantage stock data API and the News API.
* **Parameters for API Calls:**
    * `stock_params`: A dictionary containing parameters for the Alpha Vantage API call, including the function to retrieve daily time series data, the stock symbol (`STOCK_NAME`), and the API key.
    * `news_params`: A dictionary containing parameters for the News API call, including the API key and the keyword to search for in the news article titles (`COMPANY_NAME`).
* **Fetch Stock Data:** Uses `requests.get()` to retrieve stock data from Alpha Vantage and parses the JSON response to extract the daily time series data. It then retrieves the closing prices for yesterday and the day before yesterday.
* **Calculate Price Difference:** Calculates the absolute difference and the percentage difference between the two closing prices.
* **Determine Price Direction:** Sets the `up_down` variable to "🔺" if the price went up and "🔻" if it went down.
* **Check for Significant Change:** An `if` condition checks if the absolute percentage difference in closing prices is greater than 5 (this value can be adjusted).
* **Fetch News Articles (if significant change):** If the price change is significant, the script makes a GET request to the News API to fetch recent articles related to the `COMPANY_NAME`. It then extracts the top 3 articles.
* **Format News Articles:** Formats the headlines and descriptions of the top 3 articles into a list of strings to be included in the SMS message.
* **Send SMS Notification (if significant change):** Iterates through the formatted news articles and sends each as a separate SMS message via the Twilio API, including the stock information and the news headline and brief. The status of each SMS message is printed to the console.
