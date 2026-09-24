from PyQt5 import QtWidgets, QtGui, QtCore
from model import rgb_to_xyz, xyz_to_rgb, rgb_to_hsv, hsv_to_rgb, xyz_to_hsv, hsv_to_xyz

class ColorController:
    def __init__(self, ui):
        self.ui = ui
        self.current_source = 'rgb'

    def setup_connections(self):
        spinboxes = [
            self.ui.doubleSpinBox, self.ui.doubleSpinBox_2, self.ui.doubleSpinBox_3,
            self.ui.doubleSpinBox_4, self.ui.doubleSpinBox_5, self.ui.doubleSpinBox_6,
            self.ui.doubleSpinBox_7, self.ui.doubleSpinBox_8, self.ui.doubleSpinBox_9
        ]
        for sb in spinboxes:
            sb.setDecimals(0)
            sb.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)

        self.ui.doubleSpinBox.setRange(0, 255)
        self.ui.doubleSpinBox_2.setRange(0, 255)
        self.ui.doubleSpinBox_3.setRange(0, 255)

        self.ui.doubleSpinBox_4.setRange(0, 100)
        self.ui.doubleSpinBox_5.setRange(0, 100)
        self.ui.doubleSpinBox_6.setRange(0, 100)

        self.ui.doubleSpinBox_7.setRange(0, 360)
        self.ui.doubleSpinBox_8.setRange(0, 100)
        self.ui.doubleSpinBox_9.setRange(0, 100)

        self.ui.horizontalSlider.setRange(0, 255)
        self.ui.horizontalSlider_2.setRange(0, 255)
        self.ui.horizontalSlider_3.setRange(0, 255)

        self.ui.horizontalSlider_4.setRange(0, 100)
        self.ui.horizontalSlider_5.setRange(0, 100)
        self.ui.horizontalSlider_6.setRange(0, 100)

        self.ui.horizontalSlider_7.setRange(0, 360)
        self.ui.horizontalSlider_8.setRange(0, 100)
        self.ui.horizontalSlider_9.setRange(0, 100)

        self.ui.horizontalSlider.valueChanged.connect(self.on_rgb_changed)
        self.ui.horizontalSlider_2.valueChanged.connect(self.on_rgb_changed)
        self.ui.horizontalSlider_3.valueChanged.connect(self.on_rgb_changed)
        self.ui.doubleSpinBox.valueChanged.connect(self.on_rgb_spinbox_changed)
        self.ui.doubleSpinBox_2.valueChanged.connect(self.on_rgb_spinbox_changed)
        self.ui.doubleSpinBox_3.valueChanged.connect(self.on_rgb_spinbox_changed)

        self.ui.horizontalSlider_4.valueChanged.connect(self.on_xyz_changed)
        self.ui.horizontalSlider_5.valueChanged.connect(self.on_xyz_changed)
        self.ui.horizontalSlider_6.valueChanged.connect(self.on_xyz_changed)
        self.ui.doubleSpinBox_4.valueChanged.connect(self.on_xyz_spinbox_changed)
        self.ui.doubleSpinBox_5.valueChanged.connect(self.on_xyz_spinbox_changed)
        self.ui.doubleSpinBox_6.valueChanged.connect(self.on_xyz_spinbox_changed)

        self.ui.horizontalSlider_7.valueChanged.connect(self.on_hsv_changed)
        self.ui.horizontalSlider_8.valueChanged.connect(self.on_hsv_changed)
        self.ui.horizontalSlider_9.valueChanged.connect(self.on_hsv_changed)
        self.ui.doubleSpinBox_7.valueChanged.connect(self.on_hsv_spinbox_changed)
        self.ui.doubleSpinBox_8.valueChanged.connect(self.on_hsv_spinbox_changed)
        self.ui.doubleSpinBox_9.valueChanged.connect(self.on_hsv_spinbox_changed)

        self.ui.pushButton_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.ui.pushButton_4.clicked.connect(self.show_color_dialog)

        self.help_button = QtWidgets.QPushButton("Help", self.ui.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(810, 10, 70, 30))
        self.help_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border-radius: 5px; font-weight: bold;"
        )
        self.help_button.clicked.connect(self.show_help)

        self.palette_button = QtWidgets.QPushButton("Палитра", self.ui.centralwidget)
        self.palette_button.setGeometry(QtCore.QRect(730, 10, 75, 30))
        self.palette_button.setStyleSheet(
            "background-color: #2196F3; color: white; border-radius: 5px; font-weight: bold;"
        )
        self.palette_button.clicked.connect(self.show_color_dialog)

    def on_rgb_spinbox_changed(self):
        r = int(self.ui.doubleSpinBox.value())
        g = int(self.ui.doubleSpinBox_2.value())
        b = int(self.ui.doubleSpinBox_3.value())
        self._block_sliders([self.ui.horizontalSlider, self.ui.horizontalSlider_2,
                             self.ui.horizontalSlider_3])
        self.ui.horizontalSlider.setValue(r)
        self.ui.horizontalSlider_2.setValue(g)
        self.ui.horizontalSlider_3.setValue(b)
        self._unblock_sliders([self.ui.horizontalSlider, self.ui.horizontalSlider_2,
                               self.ui.horizontalSlider_3])
        self.update_from_rgb(r, g, b)

    def on_rgb_changed(self):
        r = self.ui.horizontalSlider.value()
        g = self.ui.horizontalSlider_2.value()
        b = self.ui.horizontalSlider_3.value()
        self._block_spinboxes([self.ui.doubleSpinBox, self.ui.doubleSpinBox_2,
                               self.ui.doubleSpinBox_3])
        self.ui.doubleSpinBox.setValue(r)
        self.ui.doubleSpinBox_2.setValue(g)
        self.ui.doubleSpinBox_3.setValue(b)
        self._unblock_spinboxes([self.ui.doubleSpinBox, self.ui.doubleSpinBox_2,
                                 self.ui.doubleSpinBox_3])
        self.update_from_rgb(r, g, b)

    def update_from_rgb(self, r, g, b):
        self.update_button_color(r, g, b)
        x, y, z = rgb_to_xyz(r, g, b)
        self._set_xyz(int(round(x)), int(round(y)), int(round(z)), x, y, z)
        h, s, v = rgb_to_hsv(r, g, b)
        self._set_hsv(int(round(h)), int(round(s)), int(round(v)), h, s, v)

    def on_xyz_spinbox_changed(self):
        x = int(self.ui.doubleSpinBox_4.value())
        y = int(self.ui.doubleSpinBox_5.value())
        z = int(self.ui.doubleSpinBox_6.value())
        self._block_sliders([self.ui.horizontalSlider_4, self.ui.horizontalSlider_5,
                             self.ui.horizontalSlider_6])
        self.ui.horizontalSlider_4.setValue(x)
        self.ui.horizontalSlider_5.setValue(y)
        self.ui.horizontalSlider_6.setValue(z)
        self._unblock_sliders([self.ui.horizontalSlider_4, self.ui.horizontalSlider_5,
                               self.ui.horizontalSlider_6])
        self.update_from_xyz(x, y, z)

    def on_xyz_changed(self):
        x = self.ui.horizontalSlider_4.value()
        y = self.ui.horizontalSlider_5.value()
        z = self.ui.horizontalSlider_6.value()
        self._block_spinboxes([self.ui.doubleSpinBox_4, self.ui.doubleSpinBox_5,
                               self.ui.doubleSpinBox_6])
        self.ui.doubleSpinBox_4.setValue(x)
        self.ui.doubleSpinBox_5.setValue(y)
        self.ui.doubleSpinBox_6.setValue(z)
        self._unblock_spinboxes([self.ui.doubleSpinBox_4, self.ui.doubleSpinBox_5,
                                 self.ui.doubleSpinBox_6])
        self.update_from_xyz(x, y, z)

    def update_from_xyz(self, x, y, z):
        r, g, b = xyz_to_rgb(x, y, z)
        self._set_rgb(r, g, b)
        self.update_button_color(r, g, b)
        h, s, v = xyz_to_hsv(x, y, z)
        self._set_hsv(int(round(h)), int(round(s)), int(round(v)), h, s, v)

    def on_hsv_spinbox_changed(self):
        h = int(self.ui.doubleSpinBox_7.value())
        s = int(self.ui.doubleSpinBox_8.value())
        v = int(self.ui.doubleSpinBox_9.value())
        self._block_sliders([self.ui.horizontalSlider_7, self.ui.horizontalSlider_8,
                             self.ui.horizontalSlider_9])
        self.ui.horizontalSlider_7.setValue(h)
        self.ui.horizontalSlider_8.setValue(s)
        self.ui.horizontalSlider_9.setValue(v)
        self._unblock_sliders([self.ui.horizontalSlider_7, self.ui.horizontalSlider_8,
                               self.ui.horizontalSlider_9])
        self.update_from_hsv(h, s, v)

    def on_hsv_changed(self):
        h = self.ui.horizontalSlider_7.value()
        s = self.ui.horizontalSlider_8.value()
        v = self.ui.horizontalSlider_9.value()
        self._block_spinboxes([self.ui.doubleSpinBox_7, self.ui.doubleSpinBox_8,
                               self.ui.doubleSpinBox_9])
        self.ui.doubleSpinBox_7.setValue(h)
        self.ui.doubleSpinBox_8.setValue(s)
        self.ui.doubleSpinBox_9.setValue(v)
        self._unblock_spinboxes([self.ui.doubleSpinBox_7, self.ui.doubleSpinBox_8,
                                 self.ui.doubleSpinBox_9])
        self.update_from_hsv(h, s, v)

    def update_from_hsv(self, h, s, v):
        r, g, b = hsv_to_rgb(h, s, v)
        self._set_rgb(r, g, b)
        self.update_button_color(r, g, b)
        x, y, z = hsv_to_xyz(h, s, v)
        self._set_xyz(int(round(x)), int(round(y)), int(round(z)), x, y, z)

    def show_color_dialog(self):
        current_color = self.ui.pushButton_4.palette().button().color()
        color = QtWidgets.QColorDialog.getColor(current_color, self.ui.centralwidget, "Выберите цвет")
        if color.isValid():
            r, g, b = color.red(), color.green(), color.blue()
            self._set_rgb(r, g, b)
            self.update_from_rgb(r, g, b)

    def show_help(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Справка")
        msg.setText("Приложение для конвертации цветов между форматами RGB, XYZ и HSV.\n\n"
                    "• Двигайте ползунки или вводите целые числа в поля справа\n"
                    "• Кликните по цветному квадрату или кнопке «Палитра» — откроется выбор цвета\n"
                    "• RGB: 0–255, XYZ: 0–100, HSV: H 0–360°, S/V 0–100%")
        msg.exec_()

    def update_button_color(self, r, g, b):
        self.ui.pushButton_4.setStyleSheet(
            f"background-color: rgb({r}, {g}, {b}); border: 1px solid black;"
        )

    def _set_rgb(self, r, g, b):
        self._block_spinboxes([self.ui.doubleSpinBox, self.ui.doubleSpinBox_2,
                               self.ui.doubleSpinBox_3])
        self.ui.doubleSpinBox.setValue(r)
        self.ui.doubleSpinBox_2.setValue(g)
        self.ui.doubleSpinBox_3.setValue(b)
        self._unblock_spinboxes([self.ui.doubleSpinBox, self.ui.doubleSpinBox_2,
                                 self.ui.doubleSpinBox_3])
        self._block_sliders([self.ui.horizontalSlider, self.ui.horizontalSlider_2,
                             self.ui.horizontalSlider_3])
        self.ui.horizontalSlider.setValue(r)
        self.ui.horizontalSlider_2.setValue(g)
        self.ui.horizontalSlider_3.setValue(b)
        self._unblock_sliders([self.ui.horizontalSlider, self.ui.horizontalSlider_2,
                               self.ui.horizontalSlider_3])

    def _set_xyz(self, xi, yi, zi, xf, yf, zf):
        self._block_spinboxes([self.ui.doubleSpinBox_4, self.ui.doubleSpinBox_5,
                               self.ui.doubleSpinBox_6])
        self.ui.doubleSpinBox_4.setValue(xi)
        self.ui.doubleSpinBox_5.setValue(yi)
        self.ui.doubleSpinBox_6.setValue(zi)
        self._unblock_spinboxes([self.ui.doubleSpinBox_4, self.ui.doubleSpinBox_5,
                                 self.ui.doubleSpinBox_6])
        self._block_sliders([self.ui.horizontalSlider_4, self.ui.horizontalSlider_5,
                             self.ui.horizontalSlider_6])
        self.ui.horizontalSlider_4.setValue(xi)
        self.ui.horizontalSlider_5.setValue(yi)
        self.ui.horizontalSlider_6.setValue(zi)
        self._unblock_sliders([self.ui.horizontalSlider_4, self.ui.horizontalSlider_5,
                               self.ui.horizontalSlider_6])

    def _set_hsv(self, hi, si, vi, hf, sf, vf):
        self._block_spinboxes([self.ui.doubleSpinBox_7, self.ui.doubleSpinBox_8,
                               self.ui.doubleSpinBox_9])
        self.ui.doubleSpinBox_7.setValue(hi)
        self.ui.doubleSpinBox_8.setValue(si)
        self.ui.doubleSpinBox_9.setValue(vi)
        self._unblock_spinboxes([self.ui.doubleSpinBox_7, self.ui.doubleSpinBox_8,
                                 self.ui.doubleSpinBox_9])
        self._block_sliders([self.ui.horizontalSlider_7, self.ui.horizontalSlider_8,
                             self.ui.horizontalSlider_9])
        self.ui.horizontalSlider_7.setValue(hi)
        self.ui.horizontalSlider_8.setValue(si)
        self.ui.horizontalSlider_9.setValue(vi)
        self._unblock_sliders([self.ui.horizontalSlider_7, self.ui.horizontalSlider_8,
                               self.ui.horizontalSlider_9])

    def _block_sliders(self, sliders):
        for s in sliders:
            s.blockSignals(True)

    def _unblock_sliders(self, sliders):
        for s in sliders:
            s.blockSignals(False)

    def _block_spinboxes(self, boxes):
        for b in boxes:
            b.blockSignals(True)

    def _unblock_spinboxes(self, boxes):
        for b in boxes:
            b.blockSignals(False)
