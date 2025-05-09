from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTextEdit, QComboBox, 
                             QPushButton, QLabel, QLineEdit, QGroupBox,
                             QCheckBox, QSpinBox, QFrame)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QLinearGradient, QGradient
from utils.translator import Translator
from utils.osc_client import OSCClient
from utils.logger import Logger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logger = Logger()
        self.logger.info('Initializing main window')
        
        self.translator = Translator()
        self.osc_client = OSCClient()
        
        self.auto_translate_timer = QTimer()
        self.auto_translate_timer.timeout.connect(self.auto_translate)
        self.last_text = ""
        
        self.init_ui()
        self.setup_theme()
        self.logger.info('Main window initialized')

    def init_ui(self):
        self.setWindowTitle('CxrruptTranslate')
        self.setMinimumSize(1200, 800)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        # Title
        title_label = QLabel("CxrruptTranslate")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        # OSC Settings
        osc_group = QGroupBox("OSC Settings")
        osc_layout = QHBoxLayout()
        osc_layout.setSpacing(15)
        
        ip_label = QLabel("IP:")
        self.ip_input = QLineEdit("127.0.0.1")
        port_label = QLabel("Port:")
        self.port_input = QLineEdit("9000")
        apply_osc_btn = QPushButton("Apply OSC Settings")
        apply_osc_btn.clicked.connect(self.apply_osc_settings)
        
        osc_layout.addWidget(ip_label)
        osc_layout.addWidget(self.ip_input)
        osc_layout.addWidget(port_label)
        osc_layout.addWidget(self.port_input)
        osc_layout.addWidget(apply_osc_btn)
        osc_group.setLayout(osc_layout)
        layout.addWidget(osc_group)

        # Translation Settings
        settings_group = QGroupBox("Translation Settings")
        settings_layout = QHBoxLayout()
        settings_layout.setSpacing(15)

        # Source language selection
        source_label = QLabel('Source Language:')
        self.source_lang = QComboBox()
        self.source_lang.addItems(self.translator.get_available_languages())
        self.source_lang.setCurrentText('Auto Detect')
        
        # Target language selection
        target_label = QLabel('Target Language:')
        self.target_lang = QComboBox()
        self.target_lang.addItems(self.translator.get_available_languages())
        self.target_lang.setCurrentText('English')

        # Auto-translate settings
        self.auto_translate_cb = QCheckBox("Auto Translate")
        self.auto_translate_cb.stateChanged.connect(self.toggle_auto_translate)
        
        delay_label = QLabel("Delay (ms):")
        self.delay_spin = QSpinBox()
        self.delay_spin.setRange(100, 5000)
        self.delay_spin.setValue(500)
        self.delay_spin.setSingleStep(100)
        self.delay_spin.valueChanged.connect(self.update_auto_translate_delay)

        settings_layout.addWidget(source_label)
        settings_layout.addWidget(self.source_lang)
        settings_layout.addWidget(target_label)
        settings_layout.addWidget(self.target_lang)
        settings_layout.addWidget(self.auto_translate_cb)
        settings_layout.addWidget(delay_label)
        settings_layout.addWidget(self.delay_spin)
        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)

        # Input text area
        input_group = QGroupBox("Input Text")
        input_layout = QVBoxLayout()
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText('Enter text to translate...')
        self.input_text.textChanged.connect(self.on_text_changed)
        input_layout.addWidget(self.input_text)
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)

        # Output text area
        output_group = QGroupBox("Translated Text")
        output_layout = QVBoxLayout()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText('Translation will appear here...')
        output_layout.addWidget(self.output_text)
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        
        self.translate_btn = QPushButton('Translate')
        self.copy_btn = QPushButton('Send to VRChat')
        self.clear_btn = QPushButton('Clear All')
        
        self.translate_btn.clicked.connect(self.translate_text)
        self.copy_btn.clicked.connect(self.copy_to_vrchat)
        self.clear_btn.clicked.connect(self.clear_all)
        
        button_layout.addWidget(self.translate_btn)
        button_layout.addWidget(self.copy_btn)
        button_layout.addWidget(self.clear_btn)
        layout.addLayout(button_layout)

    def setup_theme(self):
        # Set purple and black theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(20, 20, 20))
        palette.setColor(QPalette.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ToolTipBase, QColor(20, 20, 20))
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)

        self.setPalette(palette)

        # Set stylesheet for additional styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1E1E1E;
            }
            QTextEdit, QLineEdit {
                background-color: #2D2D2D;
                color: white;
                border: 2px solid #6B46C1;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                selection-background-color: #6B46C1;
            }
            QTextEdit:focus, QLineEdit:focus {
                border: 2px solid #805AD5;
            }
            QPushButton {
                background-color: #6B46C1;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 14px;
                min-width: 140px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #805AD5;
            }
            QPushButton:pressed {
                background-color: #553C9A;
            }
            QComboBox {
                background-color: #2D2D2D;
                color: white;
                border: 2px solid #6B46C1;
                border-radius: 8px;
                padding: 8px;
                min-width: 180px;
                font-size: 14px;
            }
            QComboBox:hover {
                border: 2px solid #805AD5;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border: none;
            }
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
            }
            QGroupBox {
                color: #6B46C1;
                border: 2px solid #6B46C1;
                border-radius: 8px;
                margin-top: 1.5em;
                padding: 15px;
                font-size: 14px;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px 0 10px;
                color: #6B46C1;
            }
            QCheckBox {
                color: white;
                font-size: 14px;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #6B46C1;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                background-color: #6B46C1;
            }
            QSpinBox {
                background-color: #2D2D2D;
                color: white;
                border: 2px solid #6B46C1;
                border-radius: 8px;
                padding: 8px;
                min-width: 100px;
                font-size: 14px;
            }
            QSpinBox:hover {
                border: 2px solid #805AD5;
            }
        """)

    def translate_text(self):
        try:
            source_text = self.input_text.toPlainText()
            if not source_text:
                self.logger.warning('Attempted translation with empty input')
                return
                
            source_lang = self.source_lang.currentText()
            target_lang = self.target_lang.currentText()
            
            self.logger.info(f'Translating from {source_lang} to {target_lang}')
            translated_text = self.translator.translate(source_text, source_lang, target_lang)
            self.output_text.setPlainText(translated_text)
            self.logger.debug('Translation completed successfully')
            
        except Exception as e:
            self.logger.error(f'Translation error: {str(e)}')
            self.output_text.setPlainText("Translation error occurred. Please try again.")

    def copy_to_vrchat(self):
        try:
            translated_text = self.output_text.toPlainText()
            if translated_text:
                self.logger.info('Sending text to VRChat')
                self.osc_client.send_message(translated_text)
                self.logger.debug('Text sent successfully to VRChat')
        except Exception as e:
            self.logger.error(f'Failed to send text to VRChat: {str(e)}')

    def apply_osc_settings(self):
        try:
            ip = self.ip_input.text()
            port = int(self.port_input.text())
            self.osc_client = OSCClient(ip, port)
            self.logger.info(f'OSC settings updated: {ip}:{port}')
        except ValueError as e:
            self.logger.error(f'Invalid port number: {str(e)}')
        except Exception as e:
            self.logger.error(f'Failed to apply OSC settings: {str(e)}')

    def toggle_auto_translate(self, state):
        if state == Qt.Checked:
            self.auto_translate_timer.start(self.delay_spin.value())
        else:
            self.auto_translate_timer.stop()

    def update_auto_translate_delay(self, value):
        if self.auto_translate_cb.isChecked():
            self.auto_translate_timer.setInterval(value)

    def on_text_changed(self):
        if self.auto_translate_cb.isChecked():
            self.auto_translate_timer.start(self.delay_spin.value())

    def auto_translate(self):
        current_text = self.input_text.toPlainText()
        if current_text != self.last_text:
            self.last_text = current_text
            self.translate_text()
            self.copy_to_vrchat()

    def clear_all(self):
        self.input_text.clear()
        self.output_text.clear()
        self.last_text = "" 