import pygame, random
import matplotlib.pyplot as plt

pygame.init()

W, H = 400, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("AI Dodge Learning")
clock = pygame.time.Clock()

actions = ["left", "right", "stay"]
Q = {}

alpha, gamma, epsilon = 0.2, 0.9, 0.3

episodes = 0
dodges = 0

x_data = []
y_data = []

prize = False

def get_state(px, ox):
    return (ox - px) // 20

def choose(s):
    if random.random() < epsilon:
        return random.choice(actions)
    return max(Q.get(s, {a:0 for a in actions}),
               key=lambda a: Q.get(s, {}).get(a, 0))

def update(s, a, r, s2):
    Q.setdefault(s, {x:0 for x in actions})
    Q.setdefault(s2, {x:0 for x in actions})
    Q[s][a] += alpha * (r + gamma * max(Q[s2].values()) - Q[s][a])

def spawn(px):
    if random.random() < 0.7:
        return max(0, min(W-40, px + random.randint(-60,60)))
    return random.randint(0, W-40)

def smooth(data, n=10):
    return [sum(data[max(0,i-n):i+1])/(i+1-max(0,i-n)) for i in range(len(data))]

plt.ion()
fig, ax = plt.subplots()

px = W // 2
ox = random.randint(0, W-40)
oy = 0

font = pygame.font.SysFont(None, 30)

frame = 0 

running = True
while running:

    screen.fill((20, 20, 30))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    state = get_state(px, ox)
    action = choose(state)

    if action == "left":
        px -= 7
    elif action == "right":
        px += 7

    px = max(0, min(W-40, px))

    oy += 8

    if oy > H:
        oy = 0
        ox = spawn(px)
        dodges += 1

        x_data.append(episodes)
        y_data.append(dodges)

        if dodges >= 50:
            prize = True

    hit = px < ox+40 and px+40 > ox and oy > H-40

    dx = (ox - px) // 20
    reward = -100 if hit else 2 - abs(dx)*0.1
    if action == "stay":
        reward -= 0.5

    update(state, action, reward, get_state(px, ox))

    if hit:
        episodes += 1
        dodges = 0
        prize = False

        px = W // 2
        oy = 0
        ox = spawn(px)

    epsilon = max(0.05, epsilon * 0.999)

    frame += 1
    if frame % 15 == 0:  
        ax.clear()

        if dodges < 60:
            ax.plot(smooth(y_data, 10))
        else:
            ax.plot(y_data)

        ax.set_title("AI Learning")
        ax.set_xlabel("Time")
        ax.set_ylabel("Dodges")

        fig.canvas.draw()
        fig.canvas.flush_events()

    pygame.draw.rect(screen, (0,150,255), (px, H-40, 40, 40))
    pygame.draw.rect(screen, (255,50,50), (ox, oy, 40, 40))

    screen.blit(font.render(f"Dodges: {dodges}", True, (255,255,255)), (10,10))
    screen.blit(font.render(f"Games: {episodes}", True, (255,255,255)), (10,40))

    if prize:
        pygame.draw.circle(screen, (255,215,0), (W//2,100), 30)
        screen.blit(font.render("PRIZE!", True, (255,255,0)), (150,70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()