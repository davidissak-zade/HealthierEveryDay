from main import *

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # Get width
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 110

            # Set max width
            if width == 110:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # Animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()