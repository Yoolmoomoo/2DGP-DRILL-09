#world = [] # 단일 계층 구조

# world[0] : Background Objects
# world[1] : Foreground Objects
world = [ [], [] ]

def add_object(o, depth):
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
      return # 최적화 : 지우는 미션은 달성. 다른 요소는 더 이상 체크할 필요 없다.
  print('ERROR : 존재하지 않는 객체를 지운다고?')