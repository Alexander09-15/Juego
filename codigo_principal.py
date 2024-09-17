import random
import os

class Player:
    """
    Se definira las caracteristicas del jugador
    """
    def __init__(self, nick , health , health_actually , level , experience , experience_need , points_level , daño_minimo , daño_maximo):
        self.nick = nick
        self.health = health
        self.health_actually = health_actually
        self.level = level
        self.experience = experience
        self.experience_need = experience_need   
        self.points_level = points_level
        self.daño_minimo = daño_minimo
        self.daño_maximo = daño_maximo 
    def level_up(self): # Funcion para subir de nivel
        if self.experience >= self.experience_need:
            self.level += 1
            self.experience = self.experience - self.experience_need
            self.experience_need *= 1.5 
            self.points_level += 1
    def asiggnament_points(self):
        os.system("cls")
        if self.points_level > 0:
            decision = input("Digita [1] para aumentar 20 puntos de daño o digita [2] para aumentar 50 puntos de vida... |> ")
            while decision != "1" and decision != "2":
                decision = input("Digita una opcion correcta... |>")
            if decision == "1":
                player.daño_minimo += 20
                player.daño_maximo += 20
                player.points_level -= 1
            elif decision == "2":
                player.health += 50
                player.points_level -= 1
        elif self.points_level == 0:
            v = input("Puntos de nivel insuficientes... Pulsa cualquier tecla para volver... |> ")    
            caracteristicas()        
                                   
class Enemy:
    """
    Se definiran las caracteristicas de los enemigos de cada piso
    """
    def __init__(self , enemy_name , enemy_health , enemy_damage , rareza , exp):
        self.enemy_name = enemy_name
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.rareza = rareza
        self.exp = exp     
class Pisos:
    def __init__(self , pisos , enemigos):
        self.pisos = pisos
        self.enemigos = enemigos         
        
enemigos = [
    Enemy("Vex" , 150 , 40,  1 , 15),
    Enemy("Drax" , 200 , 60 , 2 , 25),
    Enemy("Lynx" , 250 , 55 , 1 , 15),
    Enemy("Spike" , 270 , 65 , 2 , 25),
    Enemy("Fang" , 260 , 70 , 3 , 35),
    Enemy("Grim" , 280 , 75 , 3 , 35),
    Enemy("Hex" , 280 , 100 , 3 , 35),
    Enemy("Vor" , 310 , 115 , 4 , 45),
    Enemy("Raze" , 340 , 130 , 4 , 45),
    Enemy("Morloth the Dreadlord" , 550 , 300 , 5 , 60)        
] 

def combate():
    os.system("cls")
    enemigo = random.choice(enemigos)
    vida_enemigo = enemigo.enemy_health
    print(f"¡{player.nick} has encontrado un nuevo enemigo!")
    print(f"""
        Este es el estado de tu personaje
        Vida = {player.health_actually}/{player.health} | Daño = {player.daño_minimo} - {player.daño_maximo}
          
        ¡Este es| tu enemigo!
        {enemigo.enemy_name} | Vida = {vida_enemigo}/{enemigo.enemy_health} | Daño = {enemigo.enemy_damage} | Rareza = {enemigo.rareza}
          """)
    start = input("\n Pulsa cualquier tecla para comenzar el combate... > ")
    os.system("cls")
    daño_jugador = random.randint(player.daño_minimo , player.daño_maximo)
    verificacion = True
    while verificacion:
        vida_enemigo -= daño_jugador
        print(f"----------¡Le has hecho {daño_jugador} de daño a tu enemigo!-----------") 
        print(f'''\nEste es el estado actual de tu enemigo
        Salud = {vida_enemigo}/{enemigo.enemy_health}  
              ''')
        if vida_enemigo > 0:
            print(" ¡Ahora es turno de tu adversario!")
            conti = input("Pulsa cualquier tecla para continuar... > ")
            os.system("cls")
            player.health_actually -= enemigo.enemy_damage
            print(f"---------¡El enemigo te ha hecho {enemigo.enemy_damage} de daño!----------")  
            
            print(f"""Este es la vida actual de tu personaje
                Vida = {player.health_actually}/{player.health}     
                """)
            ver = input("Pulsa cualquier tecla para continuar...")
            if player.health_actually > 0:
                os.system("cls")
                print("¡Es tu turno nuevamente!")
            elif player.health_actually <= 0:
                print("\n ¡Has muerto!...")
                v = input("Pulsa cualquier tecla para volver al menu... > ")
                player.health_actually = player.health
                menu()
                verificacion = False
        elif vida_enemigo <= 0:
            print(f"""¡Has ganado el combate!
\nRecompensas obtenidas 
    exp +{enemigo.exp}
                """)
            player.experience += enemigo.exp
            volver = input("Pulsa cualquier tecla para regresar al menu... > ")
            verificacion = False
            menu()   
 
def caracteristicas():
    """
    Aqui van las carcateristicas del jugador a medida que avanze en el juego
    """
    os.system("cls")
    print(f"""
        CARACTERISTICAS:
        Nick = {player.nick}
        Vida =  {player.health_actually} / {player.health}  
        Daño = {player.daño_minimo} - {player.daño_maximo} 
    
        Nivel = {player.level}
        Experiencia = {player.experience}/{player.experience_need}
        Puntos de nivel = {player.points_level}
          """)
    volver_menu = input("Pulsa [1] para acomodar tus puntos de nivel o cualquier otra tecla para volver al menu... > ")
    if volver_menu == "1":
        player.asiggnament_points()
    menu()  
                
def menu():
    """
    Aqui va el menu del juego con sus opciones 
    """
    os.system("cls")
    print(""" \n-------------MENU DEL JUEGO-------------
          
        1.Avanzar al siguiente enemigo  
        2.Caracteristicas de tu personaje  
        3.Terminar juego  
        """)
 
    decision = input("Eige una opcion para continuar el juego... > ")
    while decision != "1" and decision != "2" and decision != "3":
        decision = input("Elige una opcion para continuar el juego... > ")
    verificacion = True
    while verificacion:
        if decision == "1":
            combate()
            verificacion = False
        elif decision == "2":
            player.level_up()
            caracteristicas()
            verificacion = False
        elif decision == "3":
            os.system("cls")
            print(f"\n Gracias por jugar {player.nick} :) \n")
            verificacion = False
            break
        
veri = True
while veri:
    os.system("cls")
    print("""  
          ==========REINO DE ÉTER==========
          
        1. Nueva Partida  
        2. En desarrollo  
        3. Salir   
          """)
    Status = input("Elige una opcion... > ")
    if Status == "1":
        veri = False
        os.system("cls")
        player = Player(input("Digita un nick para tu personaje: ") , 300 , 300 , 1 , 0 , 100 , 0 , 100 , 150)
        vida_jugador = player.health
        menu()   
    elif Status == "2":
        os.system("cls")
        print("Opcion en desarrollo... \n")
        v = input("Pulsa cualquier tecla para volver... > ")
    elif Status == "3":
        veri = False
        os.system("cls")
        print("\n¡Juego finalizado...!")
        break               
    