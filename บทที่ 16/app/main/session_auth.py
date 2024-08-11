from gotrue import SyncSupportedStorage
from flask import session, g
from supabase import Client, ClientOptions
import os


url_supabase: str = os.getenv("SUPABASE_URL_DATA")
key_supabase: str = os.getenv("SUPABASE_KEY_DATA")


class FlaskSessionStorage(SyncSupportedStorage):
    def __init__(self):
        self.storage = session

    def get_item(self, key: str) -> str | None:
        if key in self.storage:
            return self.storage[key]

    def set_item(self, key: str, value: str) -> None:
        self.storage[key] = value

    def remove_item(self, key: str) -> None:
        if key in self.storage:
            self.storage.pop(key, None)


def get_supabase() -> Client:
    if "supabase" not in g:
        g.supabase = Client(
            url_supabase,
            key_supabase,
            options=ClientOptions(storage=FlaskSessionStorage(), flow_type="pkce"),
        )
    return g.supabase
