import time
from pypresence import Presence

client_id = '1391933469571153971'
RPC = Presence(client_id)
RPC.connect()

start_time = time.time() - (1)

try:
    RPC.update(
        large_image="logoGTAVI.png",
        large_text="GTA VI",
        details="Playing online",
        start=int(start_time),
    )
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    RPC.clear()
    print("Rich Presence stopped.")
