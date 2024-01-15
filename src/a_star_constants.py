COLOR_TO_SPEED_MAP = {
        (248, 148, 18): 6.0,  # Open land
        (255, 192, 0): 1,  # Rough meadow
        (255, 255, 255): 4.0,  # Easy movement forest
        (2, 208, 60): 2.0,  # Slow run forest
        (2, 136, 40): 1.5,  # Walk forest
        (5, 73, 24): 0.2,  # Impassible vegetation
        (0, 0, 255): 0.01,  # Lake/Swamp/Marsh
        (71, 51, 3): 7.0,  # Paved road
        (0, 0, 0): 5.5,  # Footpath
        (205, 0, 101): 0.0001,  # Out of bounds
    }
