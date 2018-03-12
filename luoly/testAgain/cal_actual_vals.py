
def actual_tdoa(x):
    '''
    calculate tdoa
    :param x:
    :return:
    '''
    high = 190

    length_of_side = 58
    length_of_diagonal = 82

    cos135 = -0.707

    p_p0 = pow(pow(high, 2) + pow((x + length_of_diagonal), 2), 0.5)
    p_p1_one = pow(length_of_side, 2) + pow(x, 2) - 2 * length_of_side * x * cos135
    p_p1 = pow(pow(high, 2) + p_p1_one, 0.5)
    p_p2 = pow(pow(high, 2) + pow(x, 2), 0.5)
    p_p3 = p_p1

    result = []
    result.append(p_p2 - p_p0)
    result.append(p_p2 - p_p1)
    result.append(p_p2 - p_p3)

    return result

def get_all_result(x):
    '''
    return all data
    :param x:
    :return:
    '''
    #distances = [0, -20, 2, 3] # need to calc
    distances = [0, 0, 0, 0]
    all_distances = [0 for i in range(12)]
    for i in range(len(distances)):
        dis_result = actual_tdoa(distances[i] + x)
        for j in range(3):
            all_distances[j * 4 + i] = round(dis_result[j],2)
    return all_distances


if __name__ == '__main__':
    print get_all_result(185)
    # 100: 70
    # 200: 100
    # 300: 185
    # 500: 500 # wrong



