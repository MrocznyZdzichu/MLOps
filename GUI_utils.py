def textBrowser_append(tb, msg):
    tb.append(msg)

def textBrowser_setMsg(tb, msg):
        tb.setText(msg)

def disable_pushButton(pb):
    pb.setDisabled(1)

def enable_pushButton(pb):
    pb.setEnabled(1)

def populate_comboBox(cb, values):
    cb.clear()
    cb.addItems(values)

def set_lineEdit_text(le, text):
    le.setText(text)
