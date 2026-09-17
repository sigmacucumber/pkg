from PyQt5 import QtWidgets, QtGui
from model import rgb_to_xyz, xyz_to_rgb, rgb_to_hsv, hsv_to_rgb, xyz_to_hsv, hsv_to_xyz

class ColorController:
    def __init__(self, ui):
        self.ui = ui
        self.current_source = 'rgb'
        
    def setup_connections(self):

        self.ui.doubleSpinBox.setRange(0, 255)
        self.ui.doubleSpinBox.setDecimals(0)
        self.ui.doubleSpinBox_2.setRange(0, 255)
        self.ui.doubleSpinBox_2.setDecimals(0)
        self.ui.doubleSpinBox_3.setRange(0, 255)
        self.ui.doubleSpinBox_3.setDecimals(0)
        
        self.ui.doubleSpinBox_4.setRange(0, 100)
        self.ui.doubleSpinBox_4.setDecimals(2)
        self.ui.doubleSpinBox_5.setRange(0, 100)
        self.ui.doubleSpinBox_5.setDecimals(2)
        self.ui.doubleSpinBox_6.setRange(0, 100)
        self.ui.doubleSpinBox_6.setDecimals(2)

        self.ui.doubleSpinBox_7.setRange(0, 360)
        self.ui.doubleSpinBox_7.setDecimals(2)
        self.ui.doubleSpinBox_8.setRange(0, 100)
        self.ui.doubleSpinBox_8.setDecimals(2)
        self.ui.doubleSpinBox_9.setRange(0, 100)
        self.ui.doubleSpinBox_9.setDecimals(2)
        

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
        

        self.ui.horizontalSlider_4.valueChanged.connect(self.on_xyz_changed)
        self.ui.horizontalSlider_5.valueChanged.connect(self.on_xyz_changed)
        self.ui.horizontalSlider_6.valueChanged.connect(self.on_xyz_changed)
        

        self.ui.horizontalSlider_7.valueChanged.connect(self.on_hsv_changed)
        self.ui.horizontalSlider_8.valueChanged.connect(self.on_hsv_changed)
        self.ui.horizontalSlider_9.valueChanged.connect(self.on_hsv_changed)

        self.ui.doubleSpinBox.valueChanged.connect(self.on_rgb_spinbox_changed)
        self.ui.doubleSpinBox_2.valueChanged.connect(self.on_rgb_spinbox_changed)
        self.ui.doubleSpinBox_3.valueChanged.connect(self.on_rgb_spinbox_changed)
        
    def on_rgb_spinbox_changed(self):

        r = int(self.ui.doubleSpinBox.value())
        g = int(self.ui.doubleSpinBox_2.value())
        b = int(self.ui.doubleSpinBox_3.value())
        

        self.ui.horizontalSlider.blockSignals(True)
        self.ui.horizontalSlider_2.blockSignals(True)
        self.ui.horizontalSlider_3.blockSignals(True)
        self.ui.horizontalSlider.setValue(r)
        self.ui.horizontalSlider_2.setValue(g)
        self.ui.horizontalSlider_3.setValue(b)
        self.ui.horizontalSlider.blockSignals(False)
        self.ui.horizontalSlider_2.blockSignals(False)
        self.ui.horizontalSlider_3.blockSignals(False)
        

        self.update_from_rgb(r, g, b)
        
    def on_rgb_changed(self):
        self.current_source = 'rgb'
        r = self.ui.horizontalSlider.value()
        g = self.ui.horizontalSlider_2.value()
        b = self.ui.horizontalSlider_3.value()
        

        self.ui.doubleSpinBox.blockSignals(True)
        self.ui.doubleSpinBox_2.blockSignals(True)
        self.ui.doubleSpinBox_3.blockSignals(True)
        self.ui.doubleSpinBox.setValue(r)
        self.ui.doubleSpinBox_2.setValue(g)
        self.ui.doubleSpinBox_3.setValue(b)
        self.ui.doubleSpinBox.blockSignals(False)
        self.ui.doubleSpinBox_2.blockSignals(False)
        self.ui.doubleSpinBox_3.blockSignals(False)
        
        self.update_from_rgb(r, g, b)
        
    def update_from_rgb(self, r, g, b):

        self.update_button_color(r, g, b)
        

        x, y, z = rgb_to_xyz(r, g, b)
        
        self.ui.horizontalSlider_4.blockSignals(True)
        self.ui.horizontalSlider_5.blockSignals(True)
        self.ui.horizontalSlider_6.blockSignals(True)
        self.ui.horizontalSlider_4.setValue(int(x))
        self.ui.horizontalSlider_5.setValue(int(y))
        self.ui.horizontalSlider_6.setValue(int(z))
        self.ui.horizontalSlider_4.blockSignals(False)
        self.ui.horizontalSlider_5.blockSignals(False)
        self.ui.horizontalSlider_6.blockSignals(False)

        self.ui.doubleSpinBox_4.setValue(round(x, 2))
        self.ui.doubleSpinBox_5.setValue(round(y, 2))
        self.ui.doubleSpinBox_6.setValue(round(z, 2))
        

        h, s, v = rgb_to_hsv(r, g, b)
        

        self.ui.horizontalSlider_7.blockSignals(True)
        self.ui.horizontalSlider_8.blockSignals(True)
        self.ui.horizontalSlider_9.blockSignals(True)
        self.ui.horizontalSlider_7.setValue(int(h))
        self.ui.horizontalSlider_8.setValue(int(s))
        self.ui.horizontalSlider_9.setValue(int(v))
        self.ui.horizontalSlider_7.blockSignals(False)
        self.ui.horizontalSlider_8.blockSignals(False)
        self.ui.horizontalSlider_9.blockSignals(False)

        self.ui.doubleSpinBox_7.setValue(round(h, 2))
        self.ui.doubleSpinBox_8.setValue(round(s, 2))
        self.ui.doubleSpinBox_9.setValue(round(v, 2))
        
    def on_xyz_changed(self):

        self.current_source = 'xyz'
        x = self.ui.horizontalSlider_4.value()
        y = self.ui.horizontalSlider_5.value()
        z = self.ui.horizontalSlider_6.value()

        self.ui.doubleSpinBox_4.blockSignals(True)
        self.ui.doubleSpinBox_5.blockSignals(True)
        self.ui.doubleSpinBox_6.blockSignals(True)
        self.ui.doubleSpinBox_4.setValue(x)
        self.ui.doubleSpinBox_5.setValue(y)
        self.ui.doubleSpinBox_6.setValue(z)
        self.ui.doubleSpinBox_4.blockSignals(False)
        self.ui.doubleSpinBox_5.blockSignals(False)
        self.ui.doubleSpinBox_6.blockSignals(False)
        

        r, g, b = xyz_to_rgb(x, y, z)
        

        self.ui.horizontalSlider.blockSignals(True)
        self.ui.horizontalSlider_2.blockSignals(True)
        self.ui.horizontalSlider_3.blockSignals(True)
        self.ui.horizontalSlider.setValue(r)
        self.ui.horizontalSlider_2.setValue(g)
        self.ui.horizontalSlider_3.setValue(b)
        self.ui.horizontalSlider.blockSignals(False)
        self.ui.horizontalSlider_2.blockSignals(False)
        self.ui.horizontalSlider_3.blockSignals(False)
        

        self.ui.doubleSpinBox.blockSignals(True)
        self.ui.doubleSpinBox_2.blockSignals(True)
        self.ui.doubleSpinBox_3.blockSignals(True)
        self.ui.doubleSpinBox.setValue(r)
        self.ui.doubleSpinBox_2.setValue(g)
        self.ui.doubleSpinBox_3.setValue(b)
        self.ui.doubleSpinBox.blockSignals(False)
        self.ui.doubleSpinBox_2.blockSignals(False)
        self.ui.doubleSpinBox_3.blockSignals(False)
        

        h, s, v = xyz_to_hsv(x, y, z)

        self.ui.horizontalSlider_7.blockSignals(True)
        self.ui.horizontalSlider_8.blockSignals(True)
        self.ui.horizontalSlider_9.blockSignals(True)
        self.ui.horizontalSlider_7.setValue(int(h))
        self.ui.horizontalSlider_8.setValue(int(s))
        self.ui.horizontalSlider_9.setValue(int(v))
        self.ui.horizontalSlider_7.blockSignals(False)
        self.ui.horizontalSlider_8.blockSignals(False)
        self.ui.horizontalSlider_9.blockSignals(False)
        self.ui.doubleSpinBox_7.setValue(round(h, 2))
        self.ui.doubleSpinBox_8.setValue(round(s, 2))
        self.ui.doubleSpinBox_9.setValue(round(v, 2))
        

        self.update_button_color(r, g, b)
        
    def on_hsv_changed(self):

        self.current_source = 'hsv'
        h = self.ui.horizontalSlider_7.value()
        s = self.ui.horizontalSlider_8.value()
        v = self.ui.horizontalSlider_9.value()
        

        self.ui.doubleSpinBox_7.blockSignals(True)
        self.ui.doubleSpinBox_8.blockSignals(True)
        self.ui.doubleSpinBox_9.blockSignals(True)
        self.ui.doubleSpinBox_7.setValue(h)
        self.ui.doubleSpinBox_8.setValue(s)
        self.ui.doubleSpinBox_9.setValue(v)
        self.ui.doubleSpinBox_7.blockSignals(False)
        self.ui.doubleSpinBox_8.blockSignals(False)
        self.ui.doubleSpinBox_9.blockSignals(False)

        r, g, b = hsv_to_rgb(h, s, v)
        

        self.ui.horizontalSlider.blockSignals(True)
        self.ui.horizontalSlider_2.blockSignals(True)
        self.ui.horizontalSlider_3.blockSignals(True)
        self.ui.horizontalSlider.setValue(r)
        self.ui.horizontalSlider_2.setValue(g)
        self.ui.horizontalSlider_3.setValue(b)
        self.ui.horizontalSlider.blockSignals(False)
        self.ui.horizontalSlider_2.blockSignals(False)
        self.ui.horizontalSlider_3.blockSignals(False)

        self.ui.doubleSpinBox.blockSignals(True)
        self.ui.doubleSpinBox_2.blockSignals(True)
        self.ui.doubleSpinBox_3.blockSignals(True)
        self.ui.doubleSpinBox.setValue(r)
        self.ui.doubleSpinBox_2.setValue(g)
        self.ui.doubleSpinBox_3.setValue(b)
        self.ui.doubleSpinBox.blockSignals(False)
        self.ui.doubleSpinBox_2.blockSignals(False)
        self.ui.doubleSpinBox_3.blockSignals(False)
        
        x, y, z = hsv_to_xyz(h, s, v)

        self.ui.horizontalSlider_4.blockSignals(True)
        self.ui.horizontalSlider_5.blockSignals(True)
        self.ui.horizontalSlider_6.blockSignals(True)
        self.ui.horizontalSlider_4.setValue(int(x))
        self.ui.horizontalSlider_5.setValue(int(y))
        self.ui.horizontalSlider_6.setValue(int(z))
        self.ui.horizontalSlider_4.blockSignals(False)
        self.ui.horizontalSlider_5.blockSignals(False)
        self.ui.horizontalSlider_6.blockSignals(False)
        

        self.ui.doubleSpinBox_4.setValue(round(x, 2))
        self.ui.doubleSpinBox_5.setValue(round(y, 2))
        self.ui.doubleSpinBox_6.setValue(round(z, 2))
        

        self.update_button_color(r, g, b)
        
    def update_button_color(self, r, g, b):
        self.ui.pushButton_4.setStyleSheet(
            f"background-color: rgb({r}, {g}, {b}); border: 1px solid black;"
        )