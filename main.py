from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Crear un diseño principal
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Agregar widgets al diseño
        label = Label(text="¡Bienvenido a mi App con Kivy!", font_size=24)
        button1 = Button(text="Botón 1", size_hint=(1, 0.2))
        button2 = Button(text="Botón 2", size_hint=(1, 0.2))

        # Conectar funciones a los botones
        button1.bind(on_press=self.on_button1_click)
        button2.bind(on_press=self.on_button2_click)

        # Agregar widgets al diseño
        layout.add_widget(label)
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

    def on_button1_click(self, instance):
        print("Botón 1 presionado")

    def on_button2_click(self, instance):
        print("Botón 2 presionado")

if __name__ == "__main__":
    MyApp().run()

