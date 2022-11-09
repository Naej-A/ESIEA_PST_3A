class Isometric_tools:
    def __init__(self, width_window, height_window):
        self.width_block = 31
        self.height_block = 30
        self.origine_x = (width_window - self.width_block) / 2
        self.origine_y = height_window - self.height_block

    def coordinate_to_pixel(self, x_coord, y_coord):
        x_pixel = 0.5 * self.width_block * (x_coord - y_coord) + self.origine_x
        y_pixel = -0.25 * self.height_block * (x_coord + y_coord) + self.origine_y

        return x_pixel, y_pixel

    def pixel_to_coordinate(self, x_pixel, y_pixel):
        x_coord = (x_pixel / (0.5 * self.width_block) - self.origine_x) + (y_pixel / (-0.25 * self.height_block) - self.origine_y)
        y_coord = - (x_pixel / (0.5 * self.width_block) - self.origine_x) + (y_pixel / (-0.25 * self.height_block) - self.origine_y)

        return x_coord, y_coord
