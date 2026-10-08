from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window


Window.clearcolor = (0.043, 0.058, 0.098, 1)


class HackApp(App):

    def build(self):
        self.title = "Abdo Saad - Cyber Lab"

        main_layout = BoxLayout(
            orientation="vertical",
            padding=[20, 30, 20, 30],
            spacing=15
        )

        title = Label(
            text="[b]مختبر الأمن السيبراني التعليمي[/b]",
            color=(0, 1, 0.8, 1),
            font_size="18sp",
            markup=True,
            size_hint=(1, 0.15)
        )
        main_layout.add_widget(title)

        info = Label(
            text="أدخل رقمًا للتجربة والمحاكاة فقط:",
            color=(1, 1, 1, 1),
            font_size="14sp",
            size_hint=(1, 0.08)
        )
        main_layout.add_widget(info)

        self.phone_entry = TextInput(
            multiline=False,
            font_size="16sp",
            background_color=(0.1, 0.13, 0.22, 1),
            foreground_color=(0, 1, 0.8, 1),
            cursor_color=(1, 1, 1, 1),
            size_hint=(1, 0.12),
            input_filter="int"
        )
        main_layout.add_widget(self.phone_entry)

        self.status_box = TextInput(
            text="[ النظام جاهز للمحاكاة... ]\n",
            readonly=True,
            multiline=True,
            font_size="12sp",
            background_color=(0.07, 0.09, 0.15, 1),
            foreground_color=(0, 1, 0.8, 1),
            size_hint=(1, 0.35)
        )
        main_layout.add_widget(self.status_box)

        start_button = Button(
            text="بدء المحاكاة ⚡",
            background_color=(0, 0.6, 0.9, 1),
            font_size="16sp",
            size_hint=(1, 0.15),
            bold=True
        )

        start_button.bind(on_press=self.run_simulation)
        main_layout.add_widget(start_button)

        return main_layout

    def run_simulation(self, instance):

        target = self.phone_entry.text.strip()

        if target == "":
            self.show_popup(
                "تنبيه",
                "برجاء كتابة رقم للتجربة أولًا."
            )
            return

        self.status_box.text = (
            f"[*] بدء المحاكاة للرقم: {target}\n"
        )

        Clock.schedule_once(
            lambda dt: self.append_status(
                "[+] فحص تجريبي للنظام...\n"
            ),
            0.5
        )

        Clock.schedule_once(
            lambda dt: self.append_status(
                "[+] تحليل إعدادات الأمان...\n"
            ),
            1.0
        )

        Clock.schedule_once(
            lambda dt: self.append_status(
                "[+] انتهت المحاكاة بنجاح.\n"
            ),
            1.5
        )

        Clock.schedule_once(
            lambda dt: self.show_popup(
                "انتهت المحاكاة",
                "هذه تجربة تعليمية فقط ولا يتم اختراق أي جهاز."
            ),
            2.0
        )

    def append_status(self, text):
        self.status_box.text += text

    def show_popup(self, title, message):

        content = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        content.add_widget(
            Label(
                text=message,
                color=(1, 1, 1, 1),
                font_size="14sp"
            )
        )

        btn = Button(
            text="حسنًا",
            size_hint=(1, 0.4),
            background_color=(0, 0.6, 0.9, 1)
        )

        content.add_widget(btn)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.85, 0.4),
            title_color=(0, 1, 0.8, 1),
            background_color=(0.07, 0.09, 0.15, 1)
        )

        btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == "__main__":
    HackApp().run()
