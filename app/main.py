from asyncio.windows_events import NULL
from enum import Enum, auto
import pygame

class Mode(Enum):
    START = auto()
    END = auto()
    WALL = auto()
    REFRESH = auto()
    TRAITEMENT = auto()


class djikstra:
    def __init__(self,
                 size: [int, int],
                 screen,
                 screen_size:int

                 ) -> None:
        self.size = size
        self.start = [-1, -1]
        self.end = [-1, -1]
        self.list_wall = {}
        self.screen = screen
        self.screen_size = screen_size

    def get_start(self) -> [int, int]:
        return self.start

    def set_start(self, start):
        self.start = start

    def get_end(self) -> [int, int]:
        return self.end

    def set_end(self, end):
        self.end = end

    def get_list_wall(self) -> {(int, int), int}:
        return self.list_wall

    def dessin_grille(self) -> None:
        x = self.screen_size / self.size[0]
        y = self.screen_size / self.size[1]

        for row in range(self.size[0]):
            for col in range(self.size[1]):
                rect = pygame.Rect(row * x, col * y, x, y)

                if self.start == [row, col]:
                    pygame.draw.rect(self.screen, (0, 0, 255), rect)

                elif self.end == [row, col]:
                    pygame.draw.rect(self.screen, (255, 255, 0), rect)

                elif (row, col) in self.list_wall:
                    pygame.draw.rect(self.screen, (255, 0, 0), rect)

                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), rect)

                pygame.draw.rect(self.screen, (0, 0, 0), rect, width=2)


    def clique_tableau(self, coo_click_x: int, coo_click_y: int, mode):

        coo_click_y = int(coo_click_y // (self.screen_size / self.size[0]))
        coo_click_x = int(coo_click_x // (self.screen_size / self.size[1]))

        x = screen_size / self.size[0]
        y = screen_size / self.size[1]

        rect = pygame.Rect(coo_click_x * x, coo_click_y * y, x, y)

        match mode:


            case Mode.START:
                if (coo_click_x, coo_click_y) in self.list_wall:
                    del self.list_wall[(coo_click_x, coo_click_y)]

                elif [coo_click_x, coo_click_y] == self.end:
                    self.end.clear()

                self.start = [coo_click_x, coo_click_y]


            case Mode.END:
                if (coo_click_x, coo_click_y) in self.list_wall:
                    del self.list_wall[(coo_click_x, coo_click_y)]

                elif [coo_click_x, coo_click_y] == self.start:
                    self.start.clear()

                self.end = [coo_click_x, coo_click_y]


            case Mode.WALL:
                if (coo_click_x, coo_click_y) in self.list_wall:
                    del self.list_wall[(coo_click_x, coo_click_y)]

                else:
                    if [coo_click_x, coo_click_y] == self.start:
                        self.start.clear()

                    elif [coo_click_x, coo_click_y] == self.end:
                        self.end.clear()

                    self.list_wall[(coo_click_x, coo_click_y)] = 1


            case Mode.REFRESH:
                self.list_wall.clear()
                self.end.clear()
                self.start.clear()

        dij.dessin_grille()
        pygame.draw.rect(screen, (0, 0, 0), rect, width=2)

    def clique_bouton(self, coo_click_x: int) ->Enum:

        if coo_click_x < 100:
            pygame.draw.rect(screen, (125, 125, 255), pygame.Rect(0, 700, 100, 100))  # Start
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(100, 700, 100, 100))  # End
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200, 700, 100, 100))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 700, 100, 100))
            return Mode.START

        elif coo_click_x > 100 and coo_click_x < 200:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 700, 100, 100))  # Start
            pygame.draw.rect(screen, (255, 255, 125), pygame.Rect(100, 700, 100, 100))  # End
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200, 700, 100, 100))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 700, 100, 100))
            return Mode.END

        elif coo_click_x > 200 and coo_click_x < 300:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 700, 100, 100))  # Start
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(100, 700, 100, 100))  # End
            pygame.draw.rect(screen, (255, 125, 125), pygame.Rect(200, 700, 100, 100))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 700, 100, 100))
            return Mode.WALL

        elif coo_click_x > 300 and coo_click_x < 400:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 700, 100, 100))  # Start
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(100, 700, 100, 100))  # End
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200, 700, 100, 100))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 700, 100, 100))
            return Mode.REFRESH

        elif coo_click_x > 600 and coo_click_x < 700:
            print(f"""- Start : {dij.get_start()}
    - End : {dij.get_end()}
    - Liste mur : {dij.get_list_wall()}
                            """)
            return Mode.TRAITEMENT


def obtention_coo(question: str) -> list[int]:
    # Demande une coordonnée valide (format: 'col row') et la retourne sous forme [row, col]

    while True:
        answer = input(question)
        parts = answer.split()

        if len(parts) == 2 and all(p.isdigit() for p in parts):
            col, row = map(int, parts)
            return [row, col]

        print("Entrée invalide, format attendu : 'col row' (ex: '2 3'). Réessayez")


if __name__ == '__main__':
    # Demande des coordonnée
    size = obtention_coo("Entrez la coordonnée pour la taille (format: 'col row') : ")
    mode = ""
    answer = ""


    # Pygame interface
    pygame.init()
    screen_size = 700
    screen = pygame.display.set_mode((screen_size, screen_size + 100))
    clock = pygame.time.Clock()


    # Bonton paramètrage
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 700, 100, 100))  # Start
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(100, 700, 100, 100))  # End
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200, 700, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 700, 100, 100))

    #Lancement de Dijkstra
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(600, 700, 100, 100))

    dij = djikstra(screen=screen, size=size, screen_size=screen_size)
    dij.dessin_grille()

    running = True
    while running:
        # controle de la fermeture
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Si un clique est repéré
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coo_click_x, coo_click_y = event.pos
                #print(coo_click_x, coo_click_y)

                # Si on clique sur des boutons
                if coo_click_y > screen_size:
                    mode = dij.clique_bouton(coo_click_x=coo_click_x)

                # Sinon c'est dans le tableau
                else:
                    dij.clique_tableau(coo_click_x=coo_click_x, coo_click_y=coo_click_y, mode=mode)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()