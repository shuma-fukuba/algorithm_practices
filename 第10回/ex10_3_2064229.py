route_list = [[0, 1, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [0, 1, 0, 1, 0]] # 経路

nums = []

def solution(route:list, i=0):
    global nums
    mazes = [0, 1, 2, 3, 4]
    for r, maze in zip(route, mazes):
        if r == 1:
            if maze == 4:
                nums.append(maze)
                print(nums)
            else:
                nums.append(maze)
                solution(route_list[maze])


solution(route_list[0])
