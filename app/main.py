import pygame
from pygame.constants import MOUSEBUTTONDOWN


class djikstra:
    def __init__(self,
                 size: [int, int],
                 start: [int, int],
                 end: [int, int],
                 list_wall: [[int, int]],
                 list_restriction: [int]
                 ) -> None:
        self.size = size
        self.start = start
        self.end = end
        self.list_wall = list_wall
        self.list_restriction = list_restriction





def print_tab(size: [int, int], start: [int, int], end: [int, int], list_wall: [[int, int]], list_restriction: [int]) -> None:
    for row in range(size[0]):
        print('|', end='')
        for col in range(size[1]):
            if start == [row, col]:
                print('S|', end='')
            elif end == [row, col]:
                print('E|', end='')
            elif [row, col] in list_wall:
                print('X|', end='')
            else:
                print(' |', end='')
        print()



def dessin_grille(screen,screen_size, size: [int, int], start: [int, int], end: [int, int], list_wall: [[int, int]], list_restriction: [int]) -> None:

    x = screen_size / size[0]
    y = screen_size / size[1]

    for row in range(size[0]):
        for col in range(size[1]):

            rect = pygame.Rect(row*x, col*y, x, y)

            if start == [row, col]:
                # Jaune
                pygame.draw.rect(screen, (255, 255, 0), rect)

            elif end == [row, col]:
                #Bleu
                pygame.draw.rect(screen, (0, 0, 255), rect)

            elif [row, col] in list_wall:
                #Rouge
                pygame.draw.rect(screen, (255, 0, 0), rect)

            else:
                #Blanc
                pygame.draw.rect(screen, (255, 255, 255), rect)

            #Maillage en noir
            pygame.draw.rect(screen, (0, 0, 0), rect, width=2)






def obtention_coo(question: str) -> list[int]:
    #Demande une coordonnée valide (format: 'col row') et la retourne sous forme [row, col]

    while True:
        answer = input(question)
        parts = answer.split()

        if len(parts) == 2 and all(p.isdigit() for p in parts):
            col, row = map(int, parts)
            return [row, col]

        print("Entrée invalide, format attendu : 'col row' (ex: '2 3'). Réessayez")






if __name__ == '__main__':

    l_wall = []
    l_resr = []



    # Demande des coordonnée

    size = obtention_coo("Entrez la coordonnée pour la taille (format: 'col row') : ")
    start = obtention_coo("Entrez la coordonnée pour start (format: 'col row') : ")
    end = obtention_coo("Entrez la coordonnée pour end (format: 'col row') : ")

    answer = ""
    while answer != "OK":

        answer = input("Entrez la coordonnée d'un mur (format: 'col row') ou tapez 'OK' pour finir : ")
        if answer == "OK":
            break

        parts = answer.split()
        if len(parts) == 2 and all(p.isdigit() for p in parts):
            col, row = map(int, parts)
            l_wall.append([row, col])
            print(f"Mur ajouté en ({row}, {col})")

            # Demande de l'influence du mur
            while True:
                restriction = input("Entrez l'influence de ce mur (entier) : ")
                if restriction.isdigit():
                    l_resr.append(int(restriction) - 1)
                    break
                print("Entrée invalide. Veuillez entrer un entier.")

        else:
            print("Coordonnée invalide. Format attendu : 'col row'.")

    print_tab(size=size, start=start, end=end, list_wall=l_wall, list_restriction=l_resr)



    #Pygame interface
    pygame.init()
    screen_size = 700
    screen = pygame.display.set_mode((screen_size, screen_size+100))
    clock = pygame.time.Clock()

    pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(0, 700, 100, 100))

    running = True
    while running:
        #controle de la fermeture
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Si un clique est repéré
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coo_click_x, coo_click_y = event.pos
                print(coo_click_x, coo_click_y)

                #Si on clique sur des bouton
                if coo_click_y > screen_size:
                    print(coo_click_x, coo_click_y)
                    pygame.draw.rect(screen, (255, 125, 255), pygame.Rect(0, 700, 100, 100))
                #Sinon c'est dans le tableau
                else:
                    coo_click_y = int(coo_click_y // (screen_size / size[0] ))
                    coo_click_x = int(coo_click_x // (screen_size / size[1]))

                    print(coo_click_x, coo_click_y)



        dessin_grille(screen,screen_size , size=size, start=start, end=end, list_wall=l_wall, list_restriction=l_resr)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()