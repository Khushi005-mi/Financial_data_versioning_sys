import logging
import logging.config
from pythonjsonlogger import jsonlogger
from app.config.settings.py import settings


LOG_LEVEL = settings.LOG_LEVEL
LOG_NAME = settings.LOG_NAME
ENV = settings.ENV
APP_NAME = settings.APP_NAME
# Step 4 — Create custom formatter
class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_data, record, message_dict):
        super().addd_fields(log_data, record , message_dict)
        log_data["env"] = ENV
        log_data["app"] = APP_NAME
        log_data["level"] = record.levelname
        log_data["module"] = record.module 
# This injects metadata into every log automatically.
# Step 5 — Define logging configuration dictionary
def get_logging_config():
    return {
        "version" : 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json":{
            "()" : CustomJsonFormatter,
            "fmt" : "%(asctime)s %(levelname)s %(name)s %(message)s"

        },
        "console":{
                "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            },
        {
         "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stdout"
            "level": LOG_LEVEL
         },
         "file": {"class": "logging.FileHandler",
                    "formatter": "json",
                    "filename": f"logs/{LOG_NAME}.log",
                    "level": LOG_LEVEL},
        },
        "root":
        {
            "handlers": ["console", "file"],
            "level": LOG_LEVEL
         }
    }
# Step 6 — Initialize logging
def setup_logging():
    logging_config = get_logging_config()
    logging.config.dictConfig(logging_config)
# Step 7 — Create logs directory automatically
import os   
if not os.path.exists("logs"):
    os.makedirs("logs")
# Step 8 — Enable logging in FastAPI entrypoint
from app.core.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)
logger.info("Application starting...")
    