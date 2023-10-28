from utils.visualization import save_fig_visualization

import vidmaker
import contextlib

with contextlib.redirect_stdout(None):
    import pygame


def output(matrix, bonus_points, start, end, route, traversed_nodes, save_file_path):
    save_fig_visualization(matrix, bonus_points, start, end, save_file_path, route)
    game = Game()
    game.demo_with_pygame(
        matrix, bonus_points, start, end, route, traversed_nodes, save_file_path
    )


class Game:
    def __init__(self):
        self.WALL_RECT = pygame.Rect(17 * 4, 17 * 5, 16, 16)
        self.BACKGROUND_RECT = pygame.Rect(17, 0, 16, 16)
        self.START_RECT = pygame.Rect(17 * 16, 17 * 8, 16, 16)
        self.END_RECT = pygame.Rect(17 * 15, 17 * 9, 16, 16)
        self.BONUS_RECT = pygame.Rect(17 * 14, 17 * 10, 16, 16)
        self.ROUTE_RECT = pygame.Rect(17 * 7, 17 * 4, 16, 16)
        self.TRAVERSED_NODE_RECT = pygame.Rect(17 * 17, 17 * 10, 16, 16)
        self.UNIT = 40
        self.sprite_image = pygame.image.load("src/sprite.png")

    def demo_with_pygame(
        self, matrix, bonus_points, start, end, route, traversed_nodes, export_file_path
    ):
        pygame.init()

        SCREEN_WIDTH = self.UNIT * len(matrix[0])
        SCREEN_HEIGHT = self.UNIT * len(matrix)
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((255, 0, 0))
        pygame.display.set_caption("pygame window")
        self.video = vidmaker.Video(path=export_file_path + ".mp4", late_export=True)

        # setting fps
        clock = pygame.time.Clock()

        # draw background
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                self.draw_object(col, row, self.BACKGROUND_RECT)
                if matrix[row][col] == "x":
                    self.draw_object(col, row, self.WALL_RECT)
                self.draw_border(col, row, row, col, len(matrix), len(matrix[row]))

        # draw end point
        self.draw_object(end[1], end[0], self.END_RECT)
        # draw start point
        self.draw_object(start[1], start[0], self.START_RECT)
        # draw bonus_points
        for bonus_point in bonus_points:
            self.draw_object(bonus_point[1], bonus_point[0], self.BONUS_RECT)
        pygame.display.flip()

        # draw traversed_nodes
        for traversed_node in traversed_nodes:
            self.draw_object(
                traversed_node[1], traversed_node[0], self.TRAVERSED_NODE_RECT
            )
            clock.tick(60)
            self.video.update(pygame.surfarray.pixels3d(self.screen).swapaxes(0, 1))
            pygame.display.update()

        for i in route:
            self.draw_object(i[1], i[0], self.ROUTE_RECT)
            clock.tick(60)
            self.video.update(pygame.surfarray.pixels3d(self.screen).swapaxes(0, 1))
            pygame.display.update()

        pygame.time.delay(500)

        self.video.export()
        pygame.quit()

    def draw_object(self, x, y, item_rect_on_sheet, rotate=0):
        scaled_item = pygame.transform.scale(
            self.sprite_image.subsurface(item_rect_on_sheet), (self.UNIT, self.UNIT)
        )
        if rotate != 0:
            scaled_item = pygame.transform.rotate(scaled_item, rotate)

        self.screen.blit(scaled_item, (x * self.UNIT, y * self.UNIT))

    def draw_border(self, x, y, row, col, width, height):
        if row == 0:
            self.draw_object(x, y, pygame.Rect(17, 17 * 4, 16, 16), 180)
        if col == height - 1:
            self.draw_object(x, y, pygame.Rect(17, 17 * 4, 16, 16), 90)
        if row == width - 1:
            self.draw_object(x, y, pygame.Rect(17, 17 * 4, 16, 16))
        if col == 0:
            self.draw_object(x, y, pygame.Rect(17, 17 * 4, 16, 16), 270)
        if row == 0 and col == 0:
            self.draw_object(x, y, pygame.Rect(0, 17 * 4, 16, 16), 270)
        if row == 0 and col == height - 1:
            self.draw_object(x, y, pygame.Rect(0, 17 * 4, 16, 16), 180)
        if row == width - 1 and col == 0:
            self.draw_object(x, y, pygame.Rect(0, 17 * 4, 16, 16))
        if row == width - 1 and col == height - 1:
            self.draw_object(x, y, pygame.Rect(0, 17 * 4, 16, 16), 90)
