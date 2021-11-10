import os

_token = os.environ.get('AIOGRAM_TOKEN') # Console: export AIOGRAM_TOKEN=123456789:BotToken

TOKEN = _token if _token else "1234567890:ThERE_LEttERS_IN_YOUR_-TOkEn-Y"  # Place there your token (if no .env)
PARSE_MODE = "HTML"
