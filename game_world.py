#world = []


# world[0] : 백그라운드 객체 : 맨 아래에 그려야 할 객체들
# world[1] : 포어그라운드 객체 : 위에 그려야 할 객체들
world = [[], [], []]

def add_object(o,depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print('에러 : 존재하지 않는 객체를 지우려고 함')
    pass
