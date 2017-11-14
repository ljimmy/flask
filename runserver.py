"""启动"""
import os
from app import create_app

if __name__ == "__main__":
    create_app(os.getenv('APP_ENV') or 'development').run()
