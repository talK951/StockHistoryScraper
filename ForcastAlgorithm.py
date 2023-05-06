def forcast_algorithm(data: list[list[int, float]]) -> float:
    '''
    This function is an algorithm which predicts next value of the data

    Precondition: len(data) >= 2
    '''
    stock_val = None
    forcast = None
    prev_forcast = None
    smoothing_val = 0.57

    for i in data:
        stock_val = i[1]
        if prev_forcast is None:
            prev_forcast = stock_val
            forcast = stock_val
        temp_forcast = forcast
        forcast = forcast + smoothing_val * (stock_val - prev_forcast)
        prev_forcast = temp_forcast
    return forcast

def test_forcast_algorithm():
    data = [[1, 39],
            [2, 44],
            [3, 40],
            [4, 45],
            [5, 38],
            [6, 43],
            [7, 39]]
    print(forcast_algorithm(data))
    assert 40.54 == forcast_algorithm(data)
