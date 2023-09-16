import logging
from PyDictionary import PyDictionary
from typing import Union, Dict, List
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackContext
    ConversationHandler
    
    
)  
        
telegram.ext.ConversationHandler()



import requests
from bs4 import BeautifulSoup
import telegram
import asyncio
import pyupbit
import ccxt
from binance.client import Client
from binance.exceptions import BinanceAPIException
import time

accessToken = "6108076558:AAF0QQL6iDqRoBwcZ2xFDR7zSunHwrwqvyk"
binance_api_key = "XYOZtgUINjmhfU62dScAVPzsDgTDAfoVY1VKfYC33qLW7UkEumAVcNyZCvDgbXpi"
binance_api_secret = "QsRnDqS4AHr5lKk3pISTnT4NgKmhQFEEeWTm03IeVdI9vSGRW2u2F2AgoKHI9A18"

client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 어떤 유저인지 받아옵니다
    user = update.effective_user
    # 해당 유저에게 mention 하는 메시지를 보냅니다.
    await update.message.reply_html(
        f"Hi {user.mention_html()}",
    )


async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    user = update.effective_user
    text = "체인을 선택하세요:"
    buttons = [
        [
            InlineKeyboardButton("체인 1", callback_data="chain_1"),
            InlineKeyboardButton("체인 2", callback_data="chain_2"),
        ],
        [
            InlineKeyboardButton("체인 3", callback_data="chain_3"),
            InlineKeyboardButton("체인 4", callback_data="chain_4"),
        ],
    ]
    
    # InlineKeyboardMarkup으로 버튼 생성
    reply_markup = InlineKeyboardMarkup(buttons)

    # 사용자에게 키보드와 함께 메시지를 보냅니다.
    await update.message.reply_text(text, reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data

    # 선택된 체인에 따라 다른 작업을 수행할 수 있습니다.
    if data == "chain_1":
        await query.answer("체인 1을 선택하셨습니다.")
        # 여기에서 체인 1에 대한 작업을 수행합니다.
    elif data == "chain_2":
        await query.answer("체인 2를 선택하셨습니다.")
        # 여기에서 체인 2에 대한 작업을 수행합니다.
    # 다른 체인 옵션들에 대해서도 동일한 방식으로 처리합니다.

    

    
conv_handler = ConversationHandler(
    
)
    
  


    
#result = client.withdraw(coin = "XRP", amount = 30, address="raQwCVAJVqjrVm1Nj5SFRcX8i22BhdC9WA", network="XRP")
    #else:


# 메인함수
def main() -> None:
    # 봇 설정 값 입력
    """Run the bot."""
    application = (
        Application.builder()
        .token(accessToken)
        .build()
    )

    # Command 타입 중에 start 명령어르 받으면 start 함수 호출
    
    
    application.add_handler(CommandHandler("start", start))
    
    application.add_handler(CommandHandler("withdraw", withdraw))    
    
    application.run_polling()
    

# 코드 실행
if __name__ == "__main__":
    main()
