# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spbgltu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_spbgltu(object):
    def setupUi(self, spbgltu):
        spbgltu.setObjectName("spbgltu")
        spbgltu.resize(939, 52)
        self.label = QtWidgets.QLabel(spbgltu)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(spbgltu)
        QtCore.QMetaObject.connectSlotsByName(spbgltu)

    def retranslateUi(self, spbgltu):
        _translate = QtCore.QCoreApplication.translate
        spbgltu.setWindowTitle(_translate("spbgltu", "СПБГЛТУ"))
        self.label.setText(_translate("spbgltu", "СПБГЛТУ, Кафедра информационных систем, 09.03.02 \"Информационные системы и технологии\", 2020г. Заведующий кафедрой: Заяц Анатолий Моисеевич"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    spbgltu = QtWidgets.QDialog()
    ui = Ui_spbgltu()
    ui.setupUi(spbgltu)
    spbgltu.show()
    sys.exit(app.exec_())
