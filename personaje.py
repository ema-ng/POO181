class personaje:
    
    #constructor 
    
    def __init__(self, esp,nom,alt):
        
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #metodos de personaje 
    
    def correr (self,status):
        if(status):
            print("el personaje " + self.__nombre + " esta corriendo")
        else:
            print("el personaje " + self.__nombre +" se detubo")
    
    def lanzargranada (self):
        print("se lanzo granada")
        
    def recargararma (self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("el arma tiene ahora " + str(cargador) + " balas")
    
    """ 
    def __pensar (self):
        print("estoy pensando")
     """
     
    # declaramos los getters y setters de los atributos priveados 
        
    def __getespecie__(self):
        return self.__especie
    
    def __setespecie__(self,esp):
        self.__especie=esp
    
    def __getnombre__(self):
        return self.__nombre
    
    def __setnombre__(self,nom):
        self.__nombre=nom
        
    def __getaltura__(self):
        return self.__altura
    
    def __setaltura__(self,alt):
        self.__altura=alt
