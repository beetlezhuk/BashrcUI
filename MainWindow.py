from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import NewRecordWindow

import BashrcOperations


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(500, 500, 500, 400)
        self.setWindowTitle("Path Variables")
        side_layout = self.create_side_layout()
        side_widget = QWidget()
        side_widget.setLayout(side_layout)
        qh_box_layout = self.create_main_layout(side_widget)
        widget = QWidget()
        widget.setLayout(qh_box_layout)
        self.setCentralWidget(widget)

        self.show()

    def create_table(self):
        str_arr = BashrcOperations.read_path_vars()

        row: int = 0

        table = QTableWidget()
        table.setFixedWidth(self.width())
        table.setFixedHeight(self.height() - 50)
        table.setRowCount(len(str_arr))
        table.setColumnCount(2)
        table.setHorizontalHeaderItem(0, QTableWidgetItem("NAME"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))
        table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        for item in str_arr:
            print(item + "\n")
            table.setItem(row, 0, QTableWidgetItem("PATH"))
            table.setItem(row, 1, QTableWidgetItem(item))
            row += 1

        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        return table

    def create_add_btn(self):
        btn = QPushButton()
        btn.setText("Add")
        btn.clicked.connect(self.show_add_new_value_dialogue)

        return btn

    def show_add_new_value_dialogue(self):
        new_window = NewRecordWindow.NewWindow()
        new_window.exec_()


    def create_edit_btn(self):
        btn = QPushButton()
        btn.setText("Edit")
        return btn

    def create_remove_btn(self):
        btn = QPushButton()
        btn.setText("Remove")
        return btn

    def create_side_layout(self):
        qv_box_layout = QVBoxLayout()
        qv_box_layout.addStretch()

        qv_box_layout.addWidget(self.create_add_btn())
        qv_box_layout.addWidget(self.create_edit_btn())
        qv_box_layout.addWidget(self.create_remove_btn())
        return qv_box_layout

    def create_main_layout(self, widget: QWidget):
        qh_box_layout = QHBoxLayout()
        qh_box_layout.addWidget(self.create_table())
        qh_box_layout.addWidget(widget)
        return qh_box_layout
