"""
Matrix Handler for E.L.I.S.A.
Phase 2: Decentralized Presence
"""

from nio import AsyncClient, LoginResponse
import asyncio

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

# Usage example:
# handler = MatrixHandler("https://matrix.org", "YourUsername", "YourPassword")
# asyncio.run(handler.login())
