import os
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

# 讀取剛剛存進 GitHub Secrets 的資訊
token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

# 取得台灣時間 (UTC+8)
tw_tz = timezone(timedelta(hours=8))
now_tw = datetime.now(tw_tz).strftime("%Y-%m-%d %H:%M:%S")

# 組合通知訊息內容
message = (
    "🎉 主動通知測試成功！\n"
    "這是我的 Telegram 作業。\n"
    f"發送時間：{now_tw}"
)

# 透過官方 API 發送訊息
url = f"https://api.telegram.org/bot{token}/sendMessage"
data = urllib.parse.urlencode({"chat_id": chat_id, "text": message}).encode("utf-8")
req = urllib.request.Request(url, data=data)

with urllib.request.urlopen(req) as response:
    print("發送結果：", response.read().decode("utf-8"))
