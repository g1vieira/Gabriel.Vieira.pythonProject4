import arcade

file1 = open("nationsPop.txt", "r")

some_lines = file1.readlines()

for lines in some_lines:
    lines = lines.split(',')


my_window = arcade.open_window(800, 800, "Populations Of Largest Nations")
arcade.set_background_color(arcade.color.WINE)

arcade.start_render()

# x and y axis
arcade.draw_line(100, 100, 800, 100, arcade.color.BLACK)
arcade.draw_line(100, 100, 100, 800, arcade.color.BLACK)












arcade.finish_render()
arcade.run()