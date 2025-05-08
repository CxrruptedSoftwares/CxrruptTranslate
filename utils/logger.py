import logging
import os
from datetime import datetime

class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            self.setup_logger()
            Logger._initialized = True

    def setup_logger(self):
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Configure logging
        self.logger = logging.getLogger('CxrruptTranslate')
        self.logger.setLevel(logging.DEBUG)

        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Create and configure file handler
        log_file = os.path.join('logs', 'latest.log')
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)

        # Add handlers to logger
        self.logger.addHandler(file_handler)

        # Log initial message
        self.logger.info('Logger initialized')

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def rotate_logs(self):
        """Rotate logs if latest.log is too large"""
        log_file = os.path.join('logs', 'latest.log')
        if os.path.exists(log_file) and os.path.getsize(log_file) > 5 * 1024 * 1024:  # 5MB
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            archive_name = f'log_{timestamp}.log'
            os.rename(log_file, os.path.join('logs', archive_name))
            self.setup_logger()
            self.info('Log rotated') 