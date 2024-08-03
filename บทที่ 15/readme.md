# บทที่ 15 การทำ OAuth ด้วย Google Login เบื้องต้น

## ลบ __pycache__
```
rmdir /s /q __pycache__
```

## คำสั่งรัน
```
python run.py
```

## สร้าง virtualenv
```
python -m venv _env
```

## Install requrement
```
pip install -r requirements.txt
```

## .env
```.env
SQLALCHEMY_DATABASE_URI = "postgresql://postgres.x................"
AWS_ACCESS_KEY = ...........
AWS_SECRET_KEY = ..........
BUCKET_NAME = .......
```

## Run Dokcer , Podman
```
podman build -t name_images
podman run -it --rm -p 5000:5000 name_images
```

# Docs
- https://developers.google.com/identity/oauth2/web/guides/get-google-api-clientid
- https://supabase.com/docs/reference/python/auth-setsession
- https://supabase.com/docs/guides/auth/social-login/auth-google?queryGroups=platform&platform=web
- flask_storage.py
- https://codepen.io/mupkoo/pen/YgddgB
- https://tailwindflex.com/@shakti/google-login-signup-button
```
from gotrue import SyncSupportedStorage
from flask import session
from supabase import Client, ClientOptions
from flask import g
import os


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


url_supabase: str = os.environ.get("SUPABASE_URL_DATA")
key_supabase: str = os.environ.get("SUPABASE_KEY_DATA")


def get_supabase() -> Client:
    if "supabase" not in g:
        g.supabase = Client(
            url_supabase,
            key_supabase,
            options=ClientOptions(storage=FlaskSessionStorage(), flow_type="pkce"),
        )
    return g.supabase
```
- routes.py
```diff
...
import os
from supabase import Client
from werkzeug.local import LocalProxy
+ from .session_auth import get_supabase

api = Blueprint("main", __name__)
bcrypt = Bcrypt()
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_KEY"),
)

+ supabase_client: Client = LocalProxy(get_supabase)
...
@api.route("/test")
def test():
    data = supabase_client.auth.sign_in_with_oauth(
        {
            "provider": "google",
            "scopes": ["openid", "email", "profile"],
        }
    )
    print(data)
    return redirect(data.url, code=302)


@api.route("/test-api")
def test_api():
    code = request.args.get("code")
    next = request.args.get("next", "/")

    if code:
        res = supabase_client.auth.exchange_code_for_session({"auth_code": code})
        print(res)

    return redirect(next)
...
```