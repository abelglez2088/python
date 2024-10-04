import wx

class Ventana(wx.Frame):

    def __init__(self, *args, **kw):
        super(Ventana, self).__init__(*args, **kw)        
        self.boton1 = wx.Button(self, label="Presionar")
        self.Bind(wx.EVT_BUTTON, self.presion_boton, self.boton1)
    
    def presion_boton(self, evento):
        wx.MessageBox("Hola mundo")

# Crear la aplicación al final del código
aplicacion = wx.App(False)

# Crear la ventana después de la aplicación
frm = Ventana(None, title='Prueba')
frm.Show()

# Iniciar el bucle de eventos
aplicacion.MainLoop()
