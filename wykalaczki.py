import pygame

S_WIDTH = 640
S_HEIGHT = 640

class Segment:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        # 0 - vertical, 1 - horizontal
        if self.s[0] == self.e[0]:
            self.o = 0
        else:
            self.o = 1

    def draw(self, win):
        if self.o == 1:
            pygame.draw.rect(win, (255,255,255), (S_WIDTH//2 + 8 * self.s[0], S_HEIGHT//2 + 8 * self.s[1], 16,2))
        else:
            pygame.draw.rect(win, (255,255,255), (S_WIDTH//2 + 8 * self.s[0], S_HEIGHT//2 + 8 * self.s[1], 2,16))
            

def next_stage(last_segments):
    new_segments = []
    for seg1 in last_segments:
        start_ok = True
        end_ok = True
        for seg2 in last_segments:
            if seg1 is not seg2:
                if seg1.s == seg2.s or seg1.s == seg2.e:
                    start_ok = False
                if seg1.e == seg2.s or seg1.e == seg2.e:
                    end_ok = False
        if start_ok:
            if seg1.o == 0:
                new_segments.append(Segment((seg1.s[0]-1, seg1.s[1]), (seg1.s[0]+1, seg1.s[1])))
            else:
                new_segments.append(Segment((seg1.s[0], seg1.s[1]-1), (seg1.s[0], seg1.s[1]+1)))

        if end_ok:
            if seg1.o == 0:
                new_segments.append(Segment((seg1.e[0]-1, seg1.e[1]), (seg1.e[0]+1, seg1.e[1])))
            else:
                new_segments.append(Segment((seg1.e[0], seg1.e[1]-1), (seg1.e[0], seg1.e[1]+1)))

    return new_segments

def run():
    
    pygame.init()
    win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    win.fill((0,0,0))

    gen = 1
    print("Generation:", gen)
    last_segments = [Segment((-1,0),(1,0))]
    last_segments[0].draw(win)
    
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    last_segments = next_stage(last_segments)
                    for seg in last_segments:
                        seg.draw(win)
                    gen += 1
                    print("Generation:", gen)
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        #draw
        pygame.display.update()

run()

        
                
