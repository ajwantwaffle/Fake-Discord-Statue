import time
import json
from pypresence import Presence

# ---------- Load config.json ----------
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# ---------- Discord Connexion  ----------
RPC = Presence(config["app_id"])
RPC.connect()

start_time = int(time.time())

# ---------- Dynamic Text ----------
texts = []
if config.get("dynamictxt", False):
    texts = [
        config.get("txt1"),
        config.get("txt2"),
        config.get("txt3"),
    ]
    texts = [t for t in texts if t]
else:
    texts = [config.get("details", "")]

text_index = 0

try:
    while True:
        details_text = texts[text_index % len(texts)]
        text_index += 1

        payload = {
            "details": details_text,
            "start": start_time,
            "large_image": config.get("large_image"),
            "large_text": config.get("large_text"),
        }

        RPC.update(**payload)
        time.sleep(config.get("update_interval", 15))

except KeyboardInterrupt:
    RPC.clear()
    print("Rich Presence stopped")