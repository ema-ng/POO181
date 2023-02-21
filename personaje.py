class personaje:
    
    #atributos de clase 
    especie="humano"
    nombre="marcus fenix"
    altura= 1.90
    
    #metodos de personaje 
    
    def correr (self,status):
        if(status):
            print("el personaje" + self.nombre + "esta corriendo")
        else:
            print("el personaje " + self.nombre +"se detubo")
    
    def lanzargranada (self):
        print("se lanzo granada")
        
    def recargararma (self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("el arma tiene ahora" + cargador + "balas")