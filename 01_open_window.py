"""
juego de plataforma
"""
import arcade

# Constantes
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 500
SCREEN_TITLE = 'Juego De Plataforma'


class MyGame(arcade.Window):
    """
    Clase principal de la aplicación
    """
    
    def __init__(self):
        
        # Llamar a la clase superior y programar la ventana
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.PLUM)
        
    def setup(self):
        """Programar el juego aqui. Llama esta funcion para reiniciar el juego"""
        pass
    
    def on_draw(self):
        """Dibujar la pantalla"""
        
        self.clear()
        # Codigo para dibujar la pantalla va aqui
        
        
def main():
    """funcion principal"""
    window = MyGame()
    window.setup()
    arcade.run()
    
    
if __name__ == "__main__":
    main()
