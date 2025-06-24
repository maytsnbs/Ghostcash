from utils.telegram_bot import start_bot
from utils.scheduler import schedule_posts

if __name__ == "__main__":
    print("Starting GhostCash AI Bot...")
    schedule_posts()
    start_bot()
