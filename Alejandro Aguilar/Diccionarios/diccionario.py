# Los diccionarios 
#apliquemos buenas practicas 
from cmath import polar


def run():
#    mi_diccionario ={
        #en python no delimitamos codigo
 #       'llave1': 1,
 #       'llave2':2,
 #       'llave3':3 ,
  #  }#vamos a acceder al elemento atraves de sus llaves
    #print (mi_diccionario)
    #print(mi_diccionario#['llave1'])
    #print(mi_diccionario['llave2'])
    #print(mi_diccionario['llave3'])
    
    
    #genera un diccionar
    poblacion_paises = {
       'Argentina': 44938712,
        'Brasil':21047125,
       'Colombia':50372424
    }
    
    #print(poblacion_paises['Argentina'])
    
    #ahora vamos a ver como recorre el diccionario apartir de las llaves, atraves del ciclo for
    
    #for pais in poblacion_paises.keys():
    #   print(pais)            //muestra los paises
    
    #si quiero moestrar el contenido -
    #values me va a devolver los valores de mis llaves
   # for pais in poblacion_paises.values():
    #    print (pais)
        
        
     # Si quiero mostrar los dos valores
     
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene: '+ str(poblacion)+' habitantes')  
        
        
    

if __name__ =='__main__':
    run()