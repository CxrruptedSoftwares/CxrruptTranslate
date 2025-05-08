import sys
import os
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from utils.logger import Logger

def main():
    # Initialize logger
    logger = Logger()
    logger.info('Starting CxrruptTranslate application')

    try:
        # Create application
        app = QApplication(sys.argv)
        logger.debug('QApplication created')

        # Create and show main window
        window = MainWindow()
        window.show()
        logger.info('Main window displayed')

        # Start application
        exit_code = app.exec_()
        logger.info(f'Application exited with code: {exit_code}')
        return exit_code

    except Exception as e:
        logger.critical(f'Fatal error: {str(e)}')
        return 1

if __name__ == '__main__':
    sys.exit(main())
