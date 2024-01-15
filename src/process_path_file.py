def process_path_file(path_filename):
    points_list = []
    with open(path_filename) as f:
        for line in f:
            x_val, y_val = line.strip().split()
            points_list.append((int(x_val), int(y_val)))

    return points_list
