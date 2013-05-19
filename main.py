import requests
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Menu(Widget):
    pass


class MenuApp(App):
    def build(self):
        r = requests.get('http://0.0.0.0:5000/bar/3',headers = {'accept': 'application/json'})
        beer_list = r.json
        this_menu = Menu()
        layout = BoxLayout(orientation='vertical', padding=10)
        # layout.size_hint = (80, 70)
        this_menu.add_widget(layout)
        layout.pos_hint = (.5,.5)
        print this_menu.height, this_menu.width
        for beer in (a['beer'] for a in beer_list['availabilities']):
          button = Button(text=u'{0} - {1}'.format(beer['brewery_name'], beer['name']), ) # (this_menu.width/2, 24)
          # button.size_hint = 
          layout.add_widget(button)

        return this_menu


if __name__ == '__main__':
    MenuApp().run()