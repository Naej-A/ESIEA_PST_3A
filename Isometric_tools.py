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
        x_coord = 2 * (x_pixel - self.origine_x) / self.width_block - 4 * (y_pixel - self.origine_y) / self.height_block
        y_coord = - 2 * (x_pixel - self.origine_x) / self.width_block - 4 * (y_pixel - self.origine_y) / self.height_block

        return x_coord, y_coord

    def coordinate_to_pixel_z(self, x_coord, y_coord, z_coord):
        x_pixel = 0.5 * self.width_block * (x_coord - y_coord) + self.origine_x
        y_pixel = self.height_block * (0.5 * z_coord - 0.25 * (x_coord + y_coord)) + self.origine_y

        return x_pixel, y_pixel
