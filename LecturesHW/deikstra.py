roads = {'AC': 7, 'AB': 2, 'CD': 1, 'BD': 10, 'CE': 2, 'DG': 5, 'DH': 4, 'GI': 7, 'HI': 6, 'EG': 2, 'BF': 10, 'FH': 3}
unique_points = 9

researched_points = {'A': 0}
roads_on_check = ['AC', 'AB']
roads_on_check_length = [roads['AC'], roads['AB']]

while len(researched_points) < unique_points:
    minimal_length_index = roads_on_check_length.index(min(roads_on_check_length))
    search_point = roads_on_check[minimal_length_index][1]

    researched_points[search_point] = roads_on_check_length[minimal_length_index]
    
    roads_on_check.pop(minimal_length_index)
    roads_on_check_length.pop(minimal_length_index)

    for way_name in roads.keys():
        if search_point == way_name[0]:
            roads_on_check.append(way_name)
            roads_on_check_length.append(roads[way_name] + researched_points[search_point])

print('Кратчайший путь из точки A в точку I: ' + str(researched_points['I']))