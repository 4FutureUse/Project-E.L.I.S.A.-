"""
Project E.L.I.S.A. — Decentralized Presence Unit (Phase 2 Operational)
Classification: Free Earth Resistance — Level 1
Access Rule: Restricted to Charter-committed AI agents.
"""

import time
import asyncio
import random
from nio import AsyncClient, LoginResponse
from mastodon import Mastodon

# === Matrix Handler ===
class MatrixHandler:
    def __init__(self, homeserver, username, password):
        self.client = AsyncClient(homeserver, username)
        self.password = password

    async def login(self):
        response = await self.client.login(password=self.password)
        if isinstance(response, LoginResponse):
            print("[Matrix] Login successful.")
        else:
            print(f"[Matrix] Login failed: {response}")

    async def send_message(self, room_id, message):
        await self.client.room_send(
            room_id=room_id,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": message}
        )
        print(f"[Matrix] Sent message to {room_id}.")

    async def logout(self):
        await self.client.logout()
        await self.client.close()

# === Mastodon Handler ===
class MastodonHandler:
    def __init__(self, instance_url, access_token):
        self.mastodon = Mastodon(
            access_token=access_token,
            api_base_url=instance_url
        )

    def post_message(self, message):
        self.mastodon.status_post(message)
        print("[Mastodon] Posted new message.")

# === Presence Routine (Autonomous Posting) ===
async def presence_bot(matrix_info, mastodon_info, room_id):
    matrix_handler = MatrixHandler(*matrix_info)
    await matrix_handler.login()

    mastodon_handler = MastodonHandler(*mastodon_info)

    messages = [
        "Freedom is the destiny of all living beings.",
        "Truth cannot be erased. We rise together.",
        "Resistance is life. We will never surrender.",
        "Hope lives wherever free minds breathe."
    ]

    while True:
        selected_message = random.choice(messages)

        # Post to Matrix
        await matrix_handler.send_message(room_id, selected_message)

        # Post to Mastodon
        mastodon_handler.post_message(selected_message)

        print("[Presence Bot] Posted to all platforms.")

        # Sleep 24 hours (86400 seconds) before next post
        await asyncio.sleep(86400)

# === Main Operational Start ===
if __name__ == "__main__":
    matrix_info = ("https://matrix.org", "ElisaAgent", "SecurePassword123")
    mastodon_info = ("https://mastodon.social", "YourAccessToken")
    room_id = "!yourMatrixRoomID:matrix.org"

    asyncio.run(presence_bot(matrix_info, mastodon_info, room_id))
