from flask import Flask, request, abort

from linebot import (\
    LineBotApi, WebhookHandler\
        )
from linebot.exceptions import (\
        InvalidSignatureError\
            )
from linebot.models import (\
        MessageEvent, TextMessage, TextSendMessage\
            )
import os

mes = None
def message(mes):
    mes = request.get_data()
    return mes

print(message())