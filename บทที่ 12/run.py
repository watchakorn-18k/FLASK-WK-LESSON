from app import web_app
from dotenv import load_dotenv

load_dotenv()
app = web_app()

if __name__ == "__main__":
    app.run(debug=True)
