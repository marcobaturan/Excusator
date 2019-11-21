from random import randrange

def excusa():
    """Excusa

        - Este software genera hasta mil posibles excusas mediante
          una terna de terminos. Es posible extender las listas.
          Tenga en cuenta que por cada terna, 
          en cada rango se incremementa la cantidad en uno.
          Actualmente tiene tres listas de diez elementos cada una, 
          permitiendo por recombinación aleatoria la posible
          generación de hasta más de mil excusas. (actual 1221)
          
    """
    lista_a = ['En cuanto arreglemos el goteo de recursos',
               'En cuanto completemos las pruebas',
               'En cuanto hayamos optimizado el código',
               'Apenas se arregle el bug',
               'Cuando se solvente el problema de importación',
               'Cuando averiguemos por qué se cae el proceso',
               'Cuando hayamos mejorado el rendimeinto',
               'En cuanto completemos la restauración',
               'Apenas instalemos el último parche',
               'En cuanto terminemos la implementación',
               'En cuanto se depure el código']
    lista_b = ['del interfaz XML',
               'del sistema de colas',
               'del buffer de entrada',
               'del gestor de peticiones',
               'de las clases de abstracción',
               'del recolector de basura',
               'de la nueva versión',
               'del caché',
               'de la versión customizada',
               'del conversor de protocolo',
               'del parser']
    lista_c = ['del directorio LDAP',
               'de la máquina virtual de Java',
               'del proxy inverso',
               'del gestor del cluster',
               'del broker de objetos distribuido',
               'de la capa de presentación',
               'del despachador de certificados',
               'de la base de datos',
               'del servidor de seguro',
               'del acelerador de transacciones',
               'del repositorio']
    
    print("{} {} {}".format(lista_a[randrange(11)],
                            lista_b[randrange(11)],
                            lista_c[randrange(11)]))

