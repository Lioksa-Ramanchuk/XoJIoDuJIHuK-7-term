import numpy as np

cos_t = [            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                      [0.9807853, 0.8314696, 0.5555702, 0.1950903,
                       -0.1950903,-0.5555702,-0.8314696,-0.9807853],
                       [0.9238795, 0.3826834,-0.3826834,-0.9238795,
                        -0.9238795,-0.3826834, 0.3826834, 0.9238795],
                        [0.8314696,-0.1950903,-0.9807853,-0.5555702,
                         0.5555702, 0.9807853, 0.1950903,-0.8314696],
                         [0.7071068,-0.7071068,-0.7071068, 0.7071068,
                          0.7071068,-0.7071068,-0.7071068, 0.7071068],
                          [0.5555702,-0.9807853, 0.1950903, 0.8314696,
                           -0.8314696,-0.1950903, 0.9807853,-0.5555702],
                           [0.3826834,-0.9238795, 0.9238795,-0.3826834,
                            -0.3826834, 0.9238795,-0.9238795, 0.3826834],
                            [0.1950903,-0.5555702, 0.8314696,-0.9807853,
                             0.9807853,-0.8314696, 0.5555702,-0.1950903] ]

e = [             [0.125, 0.176777777, 0.176777777, 0.176777777,
                    0.176777777, 0.176777777, 0.176777777, 0.176777777],
                    [0.176777777, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                    [0.176777777, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                    [0.176777777, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                    [0.176777777, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                    [0.176777777, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                    [0.176777777, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                    [0.176777777, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]];

def dct(arr, **kwargs):
    s = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            temp = 0.0
            for x in range(8):
                for y in range(8):
                    try:
                        temp += cos_t[i][x] * cos_t[j][y] * arr[x][y]
                    except Exception:
                        pass
            s[i][j] = e[i][j] * temp
    return s

def idct(dct, **kwargs):
    arr = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            temp = 0
            for x in range(8):
                for y in range(8):
                    temp += dct[x][y] * cos_t[x][i] * cos_t[y][j] * e[x][y]
                    arr[i][j] = round(max(0, min(temp, 255)))
    return arr