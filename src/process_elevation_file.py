

def process_elevation_file(elevation_filename):
    """
    Function to process the elevation file for the given map.
    :param elevation_filename:
    :return:
    """
    elevation_data = []
    with open(elevation_filename) as f:
        for line in f:
            raw_line = line.strip().split()
            elevation_values = [float(x) for x in raw_line[:-5]]
            elevation_data.append(elevation_values)

    return elevation_data
