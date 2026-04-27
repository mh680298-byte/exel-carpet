from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

import openpyxl

class CarpetViewer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.wb = None
        self.ws = None
        self.last_row = 1
        self.last_col = 1
        self.current_row = 1
        self.current_col = 1

        # دکمۀ انتخاب فایل
        self.btn_open = Button(text='انتخاب فایل اکسل', size_hint=(1, 0.1))
        self.btn_open.bind(on_press=self.open_filechooser)
        self.add_widget(self.btn_open)

        # نمایش رنگ (مستطیل رنگی)
        with self.canvas:
            self.bg_color = Color(1, 1, 1, 1)  # سفید
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_rect, pos=self.update_rect)

        # نمایش مقدار و مختصات
        self.lbl_value = Label(text='', font_size='24sp', halign='center', size_hint=(1, 0.2))
        self.add_widget(self.lbl_value)

        # دکمۀ بعدی (Next)
        self.btn_next = Button(text='Next (Enter)', size_hint=(1, 0.1))
        self.btn_next.bind(on_press=self.next_cell)
        self.add_widget(self.btn_next)

        # اتصال کلید Enter
        Window.bind(on_key_down=self.on_key_down)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def open_filechooser(self, instance):
        content = FileChooserListView(filters=['*.xlsx', '*.xlsm'])
        popup = Popup(title='فایل اکسل را انتخاب کنید', content=content, size_hint=(0.9, 0.9))
        content.bind(on_submit=lambda *x: self.load_workbook(content.selection, popup))
        popup.open()

    def load_workbook(self, selection, popup):
        if selection:
            filepath = selection[0]
            self.wb = openpyxl.load_workbook(filepath, data_only=True)
            self.ws = self.wb.active
            self.last_row = self.find_last_row()
            self.last_col = self.find_last_col()
            self.current_row = self.last_row
            self.current_col = self.last_col
            self.show_cell()
            popup.dismiss()

    def find_last_row(self):
        for r in range(self.ws.max_row, 0, -1):
            for c in range(1, self.ws.max_column + 1):
                if self.ws.cell(r, c).value not in (None, '', ' '):
                    return r
        return 1

    def find_last_col(self):
        for c in range(self.ws.max_column, 0, -1):
            for r in range(1, self.ws.max_row + 1):
                if self.ws.cell(r, c).value not in (None, '', ' '):
                    return c
        return 1

    def get_hex_color(self, cell):
        fill = cell.fill
        if not fill or not fill.fgColor:
            return '#FFFFFF'
        fg = fill.fgColor
        if fg.type == 'rgb' and fg.rgb and len(fg.rgb) >= 6:
            return '#' + fg.rgb[-6:]
        if fg.type == 'theme':
            try:
                theme_idx = fg.theme
                theme = self.wb.theme
                if theme and theme.themeElements and theme.themeElements.clrScheme:
                    arr = [
                        theme.themeElements.clrScheme.dk1,
                        theme.themeElements.clrScheme.lt1,
                        theme.themeElements.clrScheme.dk2,
                        theme.themeElements.clrScheme.lt2,
                        theme.themeElements.clrScheme.accent1,
                        theme.themeElements.clrScheme.accent2,
                        theme.themeElements.clrScheme.accent3,
                        theme.themeElements.clrScheme.accent4,
                        theme.themeElements.clrScheme.accent5,
                        theme.themeElements.clrScheme.accent6
                    ]
                    if 0 <= theme_idx < len(arr):
                        return '#' + arr[theme_idx].srgbClr.val
            except:
                pass
        return '#FFFFFF'

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))

    def show_cell(self):
        if self.ws is None:
            return
        cell = self.ws.cell(self.current_row, self.current_col)
        color_hex = self.get_hex_color(cell)
        self.bg_color.rgb = self.hex_to_rgb(color_hex)
        self.lbl_value.text = f'R{self.current_row} C{self.current_col}\n{cell.value}'

    def next_cell(self, *args):
        if self.ws is None:
            return
        self.current_col -= 1
        if self.current_col < 1:
            self.current_row -= 1
            self.current_col = self.last_col
        if self.current_row < 1:
            self.lbl_value.text = 'پایان داده‌ها'
            return
        self.show_cell()

    def on_key_down(self, window, key, *args):
        # کد کی Enter معمولاً 13 است
        if key == 13:  # Enter
            self.next_cell()

class CarpetApp(App):
    def build(self):
        return CarpetViewer()

if __name__ == '__main__':
    CarpetApp().run()
