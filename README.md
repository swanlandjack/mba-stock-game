Based on the code files you provided (`app.py`, `requirements.txt`, and `game.html`), here is a tailored `README.md` file. It accurately reflects the "AI Jedi Terminal" theme and the specific Flask + Yahoo Finance architecture found in your code.

You can copy and paste the following markdown directly into your repository:

-----

#  📈

A stock market prediction game with a html interface*. This web application challenges users to predict whether a specific stock closed **UP** or **DOWN** yesterday compared to the day before, verifying guesses against live market data.

## 🚀 Features

  * **Live Market Data:** Fetches real-time historical data using the `yfinance` library.
  * **Bloomberg-Style UI:** A "dark mode" CSS grid layout resembling a professional trading terminal.
  * **Instant Verification:** Calculates the percentage change between the last two closing prices to determine the win/loss outcome.
  * **Cloud Ready:** Configured with `gunicorn` and environment variable handling for easy deployment (e.g., Render, Heroku).

## 🛠️ Tech Stack

  * **Backend:** Python, Flask
  * **Data API:** [yfinance](https://pypi.org/project/yfinance/) (Yahoo Finance)
  * **Frontend:** HTML5, CSS3 (Grid Layout), Vanilla JavaScript
  * **Server:** Gunicorn (Production WSGI)

## 📂 Project Structure

```text
├── app.py              # Main Flask application and API logic
├── requirements.txt    # Python dependencies
└── templates/
    └── game.html       # The frontend terminal interface
```

## 🏁 Getting Started

Follow these instructions to run the game locally.

### Prerequisites

  * Python 3.x installed
  * Git installed

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/swanlandjack/mba-stock-game.git
    cd mba-stock-game
    ```

2.  **Create a Virtual Environment** (Optional but recommended)

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Running the App

1.  **Start the Flask Server**

    ```bash
    python app.py
    ```

2.  **Play the Game**
    Open your web browser and navigate to:
    `http://127.0.0.1:5001` (or the port displayed in your terminal).

## 🎮 How to Play

1.  **Enter Ticker:** Type a valid stock symbol (e.g., `AAPL`, `TSLA`, `NVDA`) into the input field.
2.  **Make a Prediction:** Click **▲ PRICE WENT UP** or **▼ PRICE WENT DOWN**.
3.  **View Results:** The system compares the latest closing price to the previous day's close.
      * **Green:** You guessed correctly (Profit\!)
      * **Red:** You guessed incorrectly (Loss).

## ☁️ Deployment

This app is ready for cloud deployment. The `app.py` file is configured to listen on the `PORT` environment variable, which is standard for hosting platforms like Render or Heroku.

**Procfile (for Heroku/Render):**

```text
web: gunicorn app:app
```

## 📄 License

[MIT License](https://www.google.com/search?q=LICENSE)

-----

### Next Step

Would you like me to also write the **Procfile** mentioned in the "Deployment" section above so you can easily deploy this to a free cloud host like Render?
