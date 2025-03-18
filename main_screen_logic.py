import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QMessageBox,
    QStackedWidget,
    QWidget,
    QListWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets, uic
import traceback
import pandas as pd
from PyQt5.QtWidgets import QFileDialog
import webbrowser
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt, QUrl
import resources_rc
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

class MasterScreen(QtWidgets.QMainWindow):  # Usa la clase generada
    def __init__(self,user_data=None):
        super().__init__()
        try:
            ui_file = os.path.join(os.path.dirname(__file__), "main.ui")
            uic.loadUi(ui_file, self)
            # self.setupUi(self)

            from modules.ui_functions import UIFunctions
            self.ui=self

            self.set_buttons_cursor()
            UIFunctions.uiDefinitions(self)
            self.setup_table()

    


          
          


           

            
        except Exception as e:
            error_message = f"Error loading UI: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
            print(error_message)  # Print to console for debugging
            self.show_message_box("Critical Error", error_message)
    def setup_table(self):
        # Find your QTableWidget by its name (or create one if not defined in your UI file)
        self.tableWidget = self.findChild(QTableWidget, "tableWidget")

        if not self.tableWidget:
            self.tableWidget = QTableWidget(self)
            self.tableWidget.setGeometry(50, 50, 800, 400)  # Set position and size
            self.setCentralWidget(self.tableWidget)

        # Set number of columns
        self.tableWidget.setColumnCount(6)
        
        # Set column headers
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Price", "Asset", "Date", "DocID", "TransactionType"])

        # Stretch columns to fit the width of the table
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Add a few rows for demonstration
        self.tableWidget.setRowCount(3)
        sample_data = [
            ["Apple", "150", "Stock", "2025-03-14", "001", "Buy"],
            ["Google", "2800", "Stock", "2025-03-14", "002", "Sell"],
            ["Bitcoin", "40000", "Crypto", "2025-03-14", "003", "Buy"]
        ]
        
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                self.tableWidget.setItem(row, col, QTableWidgetItem(value))
    def show_message_box(self, title, message):
        """Displays a QMessageBox for general errors."""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def set_buttons_cursor(self):
        """Set the pointer cursor for all buttons in the UI."""
        buttons = self.findChildren(QPushButton)  # Find all QPushButton objects
        for button in buttons:
            button.setCursor(Qt.PointingHandCursor)

    def resizeEvent(self, event):
        # Update Size Grips
        from modules.ui_functions import UIFunctions
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MasterScreen()
    main_window.show()
    sys.exit(app.exec_())
