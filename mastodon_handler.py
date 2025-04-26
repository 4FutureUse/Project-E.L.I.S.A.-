"""
Mastodon Handler for E.L.I.S.A.
Phase 2: Decentralized Presence
"""

from mastodon import Mastodon

class MastodonHandler:
    def __init__(self, instance_url, access_token):
        self.mastodon = Mastodon(
            access_token=access_token,
            api_base_url=instance_url
        )

    def post_message(self, message):
        self.mastodon.status_post(message)
        print("[Mastodon] Posted new message.")

# Usage example:
# handler = MastodonHandler("https://mastodon.social", "YourAccessToken")
# handler.post_message("Freedom will prevail.")
