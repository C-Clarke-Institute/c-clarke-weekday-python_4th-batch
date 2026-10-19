import random
import json
from pathlib import Path

import pygame

# -------------------- Configuration --------------------
CELL_SIZE = 24
GRID_WIDTH = 30
GRID_HEIGHT = 22
HUD_HEIGHT = 76
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT + HUD_HEIGHT
FPS = 60

BACKGROUND = (13, 18, 28)
GRID_COLOR = (25, 33, 46)
PANEL_COLOR = (20, 28, 42)
GREEN = (83, 220, 125)
DARK_GREEN = (40, 160, 91)
HEAD_GREEN = (125, 255, 155)
RED = (255, 85, 100)
WHITE = (239, 245, 255)
MUTED = (150, 165, 185)
GOLD = (255, 205, 90)

SAVE_FILE = Path(__file__).with_name("snake_highscore.json")

pygame.init()
pygame.display.set_caption("SNAKE // Arcade")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

FONT_SMALL = pygame.font.Font(None, 24)
FONT_MEDIUM = pygame.font.Font(None, 32)
FONT_LARGE = pygame.font.Font(None, 56)
FONT_TITLE = pygame.font.Font(None, 76)


def load_high_score():
    """Read the saved high score; fall back safely if the file is missing or invalid."""
    try:
        data = json.loads(SAVE_FILE.read_text(encoding="utf-8"))
        return max(0, int(data.get("high_score", 0)))
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return 0


def save_high_score(score):
    """Persist the best score as JSON."""
    try:
        SAVE_FILE.write_text(
            json.dumps({"high_score": score}, indent=2),
            encoding="utf-8",
        )
    except OSError:
        # The game remains playable if the directory is read-only.
        pass


def draw_text(surface, text, font, color, center, *, shadow=False):
    image = font.render(str(text), True, color)
    rect = image.get_rect(center=center)
    if shadow:
        shadow_image = font.render(str(text), True, (0, 0, 0))
        surface.blit(shadow_image, rect.move(2, 3))
    surface.blit(image, rect)
    return rect


def draw_background():
    screen.fill(BACKGROUND)
    # Subtle grid lines make movement cells easy to read.
    for x in range(0, WIDTH + 1, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, HUD_HEIGHT), (x, HEIGHT), 1)
    for y in range(HUD_HEIGHT, HEIGHT + 1, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)


def draw_hud(score, high_score, level):
    pygame.draw.rect(screen, PANEL_COLOR, (0, 0, WIDTH, HUD_HEIGHT))
    pygame.draw.line(screen, (42, 56, 76), (0, HUD_HEIGHT - 1), (WIDTH, HUD_HEIGHT - 1), 2)
    draw_text(screen, "SNAKE", FONT_MEDIUM, GREEN, (76, 25))
    draw_text(screen, f"SCORE  {score}", FONT_MEDIUM, WHITE, (WIDTH // 2 - 10, 25))
    draw_text(screen, f"BEST  {high_score}", FONT_MEDIUM, GOLD, (WIDTH - 100, 25))
    draw_text(screen, f"LEVEL {level}", FONT_SMALL, MUTED, (WIDTH // 2, 54))
    draw_text(screen, "MOVE: ARROWS / WASD     PAUSE: SPACE     QUIT: ESC",
              FONT_SMALL, MUTED, (WIDTH // 2, 70))


def random_food(snake):
    empty_cells = [
        (x, y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x, y) not in snake
    ]
    return random.choice(empty_cells) if empty_cells else None


def new_game():
    center = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
    snake = [center, (center[0] - 1, center[1]), (center[0] - 2, center[1])]
    return {
        "snake": snake,
        "direction": (1, 0),
        "next_direction": (1, 0),
        "food": random_food(snake),
        "score": 0,
        "state": "playing",
        "won": False,
        "move_timer": 0,
    }


def draw_food(food):
    if food is None:
        return
    x, y = food
    center = (x * CELL_SIZE + CELL_SIZE // 2,
              HUD_HEIGHT + y * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, (100, 30, 48), center, CELL_SIZE // 2 - 2)
    pygame.draw.circle(screen, RED, center, CELL_SIZE // 2 - 4)
    pygame.draw.circle(screen, (255, 180, 185), (center[0] - 3, center[1] - 4), 3)
    pygame.draw.line(screen, DARK_GREEN, (center[0], center[1] - 7),
                     (center[0] + 3, center[1] - 11), 3)


def draw_snake(snake, direction):
    for index, (x, y) in enumerate(snake):
        rect = pygame.Rect(
            x * CELL_SIZE + 2,
            HUD_HEIGHT + y * CELL_SIZE + 2,
            CELL_SIZE - 4,
            CELL_SIZE - 4,
        )
        color = HEAD_GREEN if index == 0 else (GREEN if index % 2 else DARK_GREEN)
        pygame.draw.rect(screen, color, rect, border_radius=7)

        if index == 0:
            # Eyes are positioned in the direction the snake is facing.
            cx, cy = rect.center
            dx, dy = direction
            if dx:
                eye_positions = [(cx + dx * 4, cy - 5), (cx + dx * 4, cy + 5)]
            else:
                eye_positions = [(cx - 5, cy + dy * 4), (cx + 5, cy + dy * 4)]
            for eye in eye_positions:
                pygame.draw.circle(screen, (15, 25, 30), eye, 2)


def draw_overlay(title, subtitle, hint, accent=GREEN):
    overlay = pygame.Surface((WIDTH, HEIGHT - HUD_HEIGHT), pygame.SRCALPHA)
    overlay.fill((5, 9, 16, 185))
    screen.blit(overlay, (0, HUD_HEIGHT))

    center_x = WIDTH // 2
    center_y = HUD_HEIGHT + (HEIGHT - HUD_HEIGHT) // 2
    draw_text(screen, title, FONT_TITLE, accent, (center_x, center_y - 65), shadow=True)
    draw_text(screen, subtitle, FONT_MEDIUM, WHITE, (center_x, center_y - 15))
    draw_text(screen, hint, FONT_SMALL, MUTED, (center_x, center_y + 35))


def reset_game():
    return new_game()


def main():
    high_score = load_high_score()
    game = new_game()
    game["state"] = "menu"
    running = True
    direction_keys = {
        pygame.K_UP: (0, -1), pygame.K_w: (0, -1),
        pygame.K_DOWN: (0, 1), pygame.K_s: (0, 1),
        pygame.K_LEFT: (-1, 0), pygame.K_a: (-1, 0),
        pygame.K_RIGHT: (1, 0), pygame.K_d: (1, 0),
    }

    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif game["state"] == "menu":
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        game = reset_game()

                elif game["state"] == "game_over":
                    if event.key in (pygame.K_RETURN, pygame.K_r, pygame.K_SPACE):
                        game = reset_game()
                    elif event.key == pygame.K_m:
                        game = new_game()
                        game["state"] = "menu"

                elif game["state"] == "playing":
                    if event.key == pygame.K_SPACE:
                        game["state"] = "paused"
                    elif event.key in direction_keys:
                        requested = direction_keys[event.key]
                        current = game["direction"]
                        # Disallow an instant 180-degree turn.
                        if requested != (-current[0], -current[1]):
                            game["next_direction"] = requested

                elif game["state"] == "paused":
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        game["state"] = "playing"
                    elif event.key == pygame.K_r:
                        game = reset_game()

        if game["state"] == "playing":
            game["move_timer"] += dt
            # Every 5 points increases the level and snake speed, up to a limit.
            level = 1 + game["score"] // 5
            move_interval = max(0.065, 0.15 - (level - 1) * 0.012)

            while game["move_timer"] >= move_interval and game["state"] == "playing":
                game["move_timer"] -= move_interval
                game["direction"] = game["next_direction"]
                dx, dy = game["direction"]
                head_x, head_y = game["snake"][0]
                new_head = (head_x + dx, head_y + dy)

                ate_food = new_head == game["food"]
                # Moving into the tail's current cell is safe if the tail moves away.
                body_to_check = game["snake"] if ate_food else game["snake"][:-1]
                hit_wall = not (
                    0 <= new_head[0] < GRID_WIDTH
                    and 0 <= new_head[1] < GRID_HEIGHT
                )
                hit_self = new_head in body_to_check

                if hit_wall or hit_self:
                    game["state"] = "game_over"
                    if game["score"] > high_score:
                        high_score = game["score"]
                        save_high_score(high_score)
                    break

                game["snake"].insert(0, new_head)
                if ate_food:
                    game["score"] += 1
                    game["food"] = random_food(game["snake"])
                    if game["food"] is None:
                        game["state"] = "game_over"
                        game["won"] = True
                    if game["score"] > high_score:
                        high_score = game["score"]
                        save_high_score(high_score)
                else:
                    game["snake"].pop()

        draw_background()
        current_level = 1 + game["score"] // 5
        draw_hud(game["score"], high_score, current_level)
        draw_food(game["food"])
        draw_snake(game["snake"], game["direction"])

        if game["state"] == "menu":
            draw_overlay("SNAKE", "Eat food. Grow longer. Don't crash.",
                         "PRESS ENTER OR SPACE TO START", GREEN)
            draw_text(screen, "WASD / ARROWS TO MOVE", FONT_SMALL, WHITE,
                      (WIDTH // 2, HEIGHT - 75))
        elif game["state"] == "paused":
            draw_overlay("PAUSED", f"Current score: {game['score']}",
                         "SPACE / ENTER TO RESUME     R TO RESTART", GOLD)
        elif game["state"] == "game_over":
            if game["won"]:
                title, subtitle, accent = "YOU WIN!", "You filled the entire board!", GOLD
            else:
                title, subtitle, accent = "GAME OVER", f"Final score: {game['score']}", RED
            draw_overlay(title, subtitle, "PRESS R / ENTER TO PLAY AGAIN     M FOR MENU", accent)

        pygame.display.flip()

    save_high_score(high_score)
    pygame.quit()


if __name__ == "__main__":
    main()
