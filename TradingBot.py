import ccxt
import pandas as pd
import pandas_ta as ta
import time
import datetime
import json
import os

# --- ĐỌC CẤU HÌNH TỪ FILE ---
def load_config():
    config_path = 'config.json'
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Validate required fields
    required_fields = ['symbol', 'leverage', 'margin_mode', 'api_key', 'secret']
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field in config: {field}")
    
    return config

# --- KẾT NỐI SÀN GIAO DỊCH ---
config = load_config()
symbol = config['symbol']

# Kết nối trực tiếp đến Binance USDM
exchange = ccxt.binanceusdm({
    'apiKey': config['api_key'],
    'secret': config['secret'],
    'options': {
        'adjustForTimeDifference': True,
    }
})
exchange.options['adjustForTimeDifference'] = True
# Thiết lập đòn bẩy và chế độ margin
try:
    exchange.set_leverage(config['leverage'], symbol)
    exchange.set_margin_mode(config['margin_mode'], symbol)

except Exception as e:
    print(f"Error setting leverage/margin mode: {e}")

trade_long = None
trade_short = None

while True:
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=config['time'], limit=100)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        price = df['close'].iloc[-1]

        
        rsi0 = ta.rsi(df['close'], length=config['rsi'])
        rsi1 = rsi0.iloc[-3]
        rsi2 = rsi0.iloc[-2]
        

        if rsi1 < config['rsi_lower_band'] and rsi2 > config['rsi_lower_band'] and trade_long != 'LONG':
            exchange.create_order(symbol, 'market', 'buy', config['vol'], params={'positionSide': "LONG"})  
            print(f"{datetime.datetime.now()} - Long signal detected at price: {price}")
            trade_long = 'LONG'
            trade_short = None

            
        if rsi1 > config['rsi_upper_band'] and rsi2 < config['rsi_upper_band'] and trade_short != 'SHORT':
            exchange.create_order(symbol, 'market', 'sell', config['vol'], params={'positionSide': "SHORT"})
            print(f"{datetime.datetime.now()} - Short signal detected at price: {price}")
            trade_short = 'SHORT'
            trade_long = None


        time.sleep(5)  # Chờ 5 giây trước khi lặp lại
    except Exception as e:
        print(f"Lỗi: {e}")
        time.sleep(5)
        continue


