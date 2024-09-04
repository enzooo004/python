from pygame import mixer
class Reproductor:
    archivo = None
    def __init__(self,archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)
    def play(self):
        mixer.music.play()
        return "Reproduciendo musica"
    def pause(self):
        mixer.music.pause()
        return"La musica a sido pausada"
    def stop(self):
        mixer.music.stop()
        return "La musica se detuvo"
    def volumen(self, v):
        mixer.music.set_volume(v)
        return "definiendo volumen{}". format(v)
    
        