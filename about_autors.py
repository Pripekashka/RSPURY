# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_autors.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_autors(object):
    def setupUi(self, about_autors):
        about_autors.setObjectName("about_autors")
        about_autors.resize(809, 106)
        self.label = QtWidgets.QLabel(about_autors)
        self.label.setGeometry(QtCore.QRect(10, 0, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(about_autors)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(about_autors)
        QtCore.QMetaObject.connectSlotsByName(about_autors)

    def retranslateUi(self, about_autors):
        _translate = QtCore.QCoreApplication.translate
        about_autors.setWindowTitle(_translate("about_autors", "Об авторе"))
        self.label.setText(_translate("about_autors", "Создатель: Кононов Михаил Дмитриевич, специально для дипломного проекта \"Планирование учебного расписания университета\" г. Санкт-Петербург СПБГЛТУ 2020г."))
        self.label_2.setText(_translate("about_autors", "По вопросам технической поддержки ПО обращаться по адресу: kononov4598@mail.ru"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_autors = QtWidgets.QDialog()
    ui = Ui_about_autors()
    ui.setupUi(about_autors)
    about_autors.show()
    sys.exit(app.exec_())
