import binascii

import PyQt6
from PyQt6.QtGui import QIcon, QPainter, QColor, QPen, QBrush
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QTextBrowser, QGridLayout, QLabel, QLineEdit, QTextBrowser, \
    QLCDNumber
from PyQt6.QtCore import pyqtSlot, Qt, QSize


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.update()

    def paintEvent(self, a0) -> None:
        super(CentralWidget, self).paintEvent(a0)

        painter = QPainter(self)

        pen = QPen()
        pen.setColor(QColor("red"))
        pen.setWidth(25)
        pen.setStyle(Qt.PenStyle.DashDotDotLine)
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor("cyan"))
        brush.setStyle(Qt.BrushStyle.TexturePattern.DiagCrossPattern)
        painter.setBrush(brush)

        painter.drawEllipse(100, 50, 200, 300)
