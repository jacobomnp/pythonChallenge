'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo resultado seguido de:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

'''
def juegoTenis(juegos):
    jugadas = juegos
    score1 = 0
    score2 = 0

    print("punto para jugador 1 = 'p1'")

    print("punto para jugador 2 = 'p2'")

    while jugadas >= 1:
        
        score1 = 'love' if score1 == 0 else score1
        score2 = 'love' if score2 == 0 else score2
        
        print(f'j1: {score1} j2: {score2}') if (score1 or score2) == 'love' or 'love' != (score1 and score2) <= 40 else print('') 
        
        score1 = 0 if score1 == 'love' else score1 
        score2 = 0 if score2 == 'love' else score2

        
        jugada = input('punto para? ')

        validar = True if jugada == 'p1' or jugada == 'p2' else False


        if validar == True:
            if jugada == 'p1':
                if score1 >= 30:
                    score1 +=10
                else:
                    score1 += 15
            else:
                if score2 >= 30:
                    score2 += 10
                else:
                    score2 += 15

            if score1 > 50:
                print('gana jugador 1')
                break
            elif score2 > 50:
                print('gana jugador 2')
                break
            elif score1 > 40 and score1 > score2:
                print('ventaja jugador 1')
            elif score2 > 40 and score2 > score1:
                print('ventaja jugador 2')
            elif (score1 and score2) >= 40 and (score1 == score2):
                print('sauce')

            jugadas-=1
        elif validar == False:
            print('jugada no valida')
        
    print(f'Deuce j1: {score1} j2: {score2}') if score1 == score2 else print(f'j1: {score1} - j2: {score2}') 

juegoTenis(20)