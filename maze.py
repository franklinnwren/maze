import requests
import json
import sys


m_UID = '304972327'
session = "http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/session"
get_token = requests.post(session, data={'uid': m_UID})
token = json.loads(get_token.text)['token']
m_URL = "http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=" + token
directions = ["UP", "DOWN", "LEFT", "RIGHT"]
move_back = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}


def move(dir):
    m_action = {'action': dir}
    get_result = requests.post(m_URL, m_action)
    result = json.loads(get_result.text)["result"]
    return result


def get_location(x, y, dir):
    if dir == "UP":
        return x, y-1
    elif dir == "DOWN":
        return x, y+1
    elif dir == "LEFT":
        return x-1, y
    elif dir == "RIGHT":
        return x+1, y


def in_range(x, y):
    return x >= 0 and x < width and y >= 0 and y < height


def recursion(x, y):
    if trace_maze[x][y] == 0:
        trace_maze[x][y] = 1
        for dir in directions:
            new_x, new_y = get_location(x, y, dir)
            if in_range(new_x, new_y) and not trace_maze[new_x][new_y]:
                result = move(dir)
                #print(x, y, result)
                # --- the line above is for debug purposes
                if result == "WALL":
                    trace_maze[new_x][new_y] = 1
                elif result == "END":
                    return True
                elif result == "SUCCESS":
                    next_step = recursion(new_x, new_y)
                    if next_step:
                        return True
                    else:
                        move(move_back[dir])
        return False
    return False


m_location = json.loads(requests.get(m_URL).text)
status = m_location['status']
print(status)
while status != "FINISHED":
    if status == 'PLAYING':
        x = m_location['current_location'][0]
        y = m_location['current_location'][1]
        width = m_location['maze_size'][0]
        height = m_location['maze_size'][1]
        levels_completed = m_location['levels_completed']
        print("LEVEL:", levels_completed + 1)
        trace_maze = [[0 for i in range(height)] for j in range(width)]
        recursion(x, y)
    elif status == "GAME_OVER":
        print(status)
        break
    elif status == "NONE":
        print(status)
        break
    m_location = json.loads(requests.get(m_URL).text)
    status = m_location['status']
    print(status)
