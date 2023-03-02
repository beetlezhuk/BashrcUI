import os
import uuid
from PyQt5.QtWidgets import *
import BashrcOperations


class NewWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Value to PATH")
        self.setGeometry(600, 550, 300, 150)

        new_path_value = QLineEdit()
        add_value_btn = QPushButton()
        add_value_btn.setText("Add Value")
        add_value_btn.clicked.connect(lambda: BashrcOperations.add_value_to_path(new_path_value, self))

        layout = QVBoxLayout()
        layout.addWidget(new_path_value)
        layout.addWidget(add_value_btn)
        self.setLayout(layout)
