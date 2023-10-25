from utils.visualization import save_fig_visualization

import contextlib

with contextlib.redirect_stdout(None):
    import pygame


def output(matrix, bonus_points, start, end, route, traversed_nodes, save_file_path):
    save_fig_visualization(matrix, bonus_points, start, end, save_file_path, route)
    demo_with_pygame(matrix, bonus_points, start, end, route, traversed_nodes)


def demo_with_pygame(matrix, bonus_points, start, end, route, traversed_nodes):
    pygame.init()

    # constants
    UNIT = 40

    WALL_RECT = pygame.Rect(17 * 4, 17 * 5, 16, 16)
    BACKGROUND_RECT = pygame.Rect(17, 0, 16, 16)
    START_RECT = pygame.Rect(17 * 16, 17 * 8, 16, 16)
    END_RECT = pygame.Rect(17 * 15, 17 * 9, 16, 16)
    BONUS_RECT = pygame.Rect(17 * 14, 17 * 10, 16, 16)
    ROUTE_RECT = pygame.Rect(17 * 7, 17 * 4, 16, 16)
    TRAVERSED_NODE_RECT = pygame.Rect(17 * 17, 17 * 10, 16, 16)

    # get sprite
    sprite_image = pygame.image.load("src/sprite.png")

    screen = pygame.display.set_mode((UNIT * len(matrix[0]), UNIT * len(matrix)))

    # setting fps
    clock = pygame.time.Clock()

    traversal_counter = 0
    route_counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw background
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                draw_object(
                    screen,
                    col * UNIT,
                    row * UNIT,
                    BACKGROUND_RECT,
                    sprite_image,
                    UNIT,
                )
                if matrix[row][col] == "x":
                    draw_object(
                        screen, col * UNIT, row * UNIT, WALL_RECT, sprite_image, UNIT
                    )
                draw_border(
                    screen,
                    col * UNIT,
                    row * UNIT,
                    sprite_image,
                    UNIT,
                    row,
                    col,
                    len(matrix),
                    len(matrix[row]),
                )

        # draw traversed_nodes
        for i in range(traversal_counter):
            draw_object(
                screen,
                traversed_nodes[i][1] * UNIT,
                traversed_nodes[i][0] * UNIT,
                TRAVERSED_NODE_RECT,
                sprite_image,
                UNIT,
            )

        # draw bonus_points
        for bonus_point in bonus_points:
            draw_object(
                screen,
                bonus_point[1] * UNIT,
                bonus_point[0] * UNIT,
                BONUS_RECT,
                sprite_image,
                UNIT,
            )

        # limits FPS to 60
        clock.tick(40)

        # finish and draw the route
        if traversal_counter >= len(traversed_nodes):
            for i in range(route_counter):
                draw_object(
                    screen,
                    route[i][1] * UNIT,
                    route[i][0] * UNIT,
                    ROUTE_RECT,
                    sprite_image,
                    UNIT,
                )

            if route_counter >= len(route):
                pygame.time.delay(1000)
                running = False

            route_counter += 1
        else:
            traversal_counter += 1

        # draw start point
        draw_object(
            screen, start[1] * UNIT, start[0] * UNIT, START_RECT, sprite_image, UNIT
        )

        # draw end point
        draw_object(screen, end[1] * UNIT, end[0] * UNIT, END_RECT, sprite_image, UNIT)

        # re-render window
        pygame.display.flip()

    pygame.quit()


def draw_object(screen, x, y, item_rect_on_sheet, sprite_image, UNIT, rotate=0):
    scaled_item = pygame.transform.scale(
        sprite_image.subsurface(item_rect_on_sheet), (UNIT, UNIT)
    )
    if rotate != 0:
        scaled_item = pygame.transform.rotate(scaled_item, rotate)
    screen.blit(scaled_item, (x, y))


def draw_border(screen, x, y, sprite_image, UNIT, row, col, width, height):
    if row == 0:
        draw_object(
            screen, x, y, pygame.Rect(17, 17 * 4, 16, 16), sprite_image, UNIT, 180
        )
    if col == height - 1:
        draw_object(
            screen, x, y, pygame.Rect(17, 17 * 4, 16, 16), sprite_image, UNIT, 90
        )
    if row == width - 1:
        draw_object(screen, x, y, pygame.Rect(17, 17 * 4, 16, 16), sprite_image, UNIT)
    if col == 0:
        draw_object(
            screen, x, y, pygame.Rect(17, 17 * 4, 16, 16), sprite_image, UNIT, 270
        )

    if row == 0 and col == 0:
        draw_object(
            screen, x, y, pygame.Rect(0, 17 * 4, 16, 16), sprite_image, UNIT, 270
        )
    if row == 0 and col == height - 1:
        draw_object(
            screen, x, y, pygame.Rect(0, 17 * 4, 16, 16), sprite_image, UNIT, 180
        )
    if row == width - 1 and col == 0:
        draw_object(screen, x, y, pygame.Rect(0, 17 * 4, 16, 16), sprite_image, UNIT)
    if row == width - 1 and col == height - 1:
        draw_object(
            screen, x, y, pygame.Rect(0, 17 * 4, 16, 16), sprite_image, UNIT, 90
        )
