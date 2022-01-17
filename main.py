from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Пункт меню 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Пункт меню 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Навигация"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "Основное окно 1"
                    halign: "center"

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Основное окно 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MortgageCalculatorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MortgageCalculatorApp().run()