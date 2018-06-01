import math
import random

__all__ = ['ball_in_box']



def pro_points(xrange, yrange, percision):

    points = []
    x_dv = (xrange[1] - xrange[0]) * 1.0 / percision
    y_num = int((yrange[1] - yrange[0]) / x_dv)
    for i in range(1, percision):
        for j in range(1, y_num):
            points.append((xrange[0] + i * x_dv, yrange[0] + j * x_dv))

    return points

def get_max_r(point, xrange, yrange, blockers, circles):

    pre_r_list = []
    pre_r_list.append(abs(point[0] - xrange[0]))
    pre_r_list.append(abs(point[0] - xrange[1]))
    pre_r_list.append(abs(point[1] - yrange[0]))
    pre_r_list.append(abs(point[1] - yrange[1]))
    for blocker in blockers:
        d = math.sqrt((point[0] - blocker[0])**2 + (point[1] - blocker[1])**2)
        pre_r_list.append(d)

    for circle in circles:
        d = math.sqrt((point[0] - circle[0])**2 +
                      (point[1] - circle[1])**2) - circle[2]
        
        if d <= 0:
            return 0
        pre_r_list.append(d)
    r = xrange[1] - xrange[0]
    for pre_r in pre_r_list:
        if pre_r < r:
            r = pre_r
    return r


def ball_in_box(m, blockers):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """
    xrange = [-1,1]
    yrange = [-1,1]
    percision = 800
    circles = []
    points = pro_points(xrange, yrange, percision)
    for i in range(m):
        temp_r = 0
        circle = [0, 0, 0]
        for point in points:
            r = get_max_r(point, xrange, yrange, blockers, circles)
            if r > temp_r:
                temp_r = r
                circle[0] = point[0]
                circle[1] = point[1]
                circle[2] = temp_r

        points.remove((circle[0], circle[1]))
        circles.append((circle[0], circle[1], circle[2]))
  
    return circles
