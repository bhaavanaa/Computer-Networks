# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thankyou.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_thankyou_2(object):
    def setupUi(self, thankyou_2):
        thankyou_2.setObjectName("thankyou_2")
        thankyou_2.resize(636, 545)
        self.thankyou = QtWidgets.QLabel(thankyou_2)
        self.thankyou.setGeometry(QtCore.QRect(-4, -4, 641, 561))
        self.thankyou.setStyleSheet("     \n"
"background-image: url(:/newPrefix/thanks.jpg);")
        self.thankyou.setText("")
        self.thankyou.setObjectName("thankyou")

        self.retranslateUi(thankyou_2)
        QtCore.QMetaObject.connectSlotsByName(thankyou_2)

    def retranslateUi(self, thankyou_2):
        _translate = QtCore.QCoreApplication.translate
        thankyou_2.setWindowTitle(_translate("thankyou_2", "thankyou"))
import thanks_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thankyou_2 = QtWidgets.QDialog()
    ui = Ui_thankyou_2()
    ui.setupUi(thankyou_2)
    thankyou_2.show()
    sys.exit(app.exec_())
