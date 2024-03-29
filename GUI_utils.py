from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


def textBrowser_append(tb, msg):
    tb.append(msg)

def textBrowser_setMsg(tb, msg):
        tb.setText(msg)

def disable_pushButton(pb):
    pb.setDisabled(1)

def enable_pushButton(pb):
    pb.setEnabled(1)

def read_comboBox(cb):
    return cb.currentText()

def clear_comboBox(cb):
    cb.clear()

def populate_comboBox(cb, values, empty_first=False):
    cb.clear()
    if empty_first == True:
        cb.addItem('')
    cb.addItems(values)

def read_lineEdit(le):
    return le.text()

def set_lineEdit_text(le, text):
    le.setText(text)

def clear_lineEdit(le):
    le.clear()

def populate_listWidget(lw, items_list):
    for added_item in items_list:
        item = QListWidgetItem(added_item)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Unchecked)
        lw.addItem(item)

def clear_listWidget(lw):
    lw.clear()

def get_lw_items(lw):
    result = []
    for i in range(lw.count()):
            item = lw.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                result.append(item.text())
    return result

def populate_tableWidget(tw, data2D, headers=None):
    row_count = len(data2D)
    col_count = len(data2D[0])
    tw.setRowCount(row_count)
    tw.setColumnCount(col_count)

    for row in range(0, row_count):
        for col in range(0, col_count):
            value = data2D[row][col]
            item = QTableWidgetItem(str(value))
            tw.setItem(row, col, item)

    if headers != None:
        tw.setHorizontalHeaderLabels(headers)
    tw.resizeColumnsToContents()

def clear_tableWidget(tw):
    tw.clearContents()
    tw.setRowCount(0)
    tw.setColumnCount(0)

def change_stackedWidget_page(sw, page_index):
    sw.setCurrentIndex(page_index)
