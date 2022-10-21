#CODE WILL NOT RUN TRUST ME

import arcade

file1 = open("nationsPop.txt", "r")

all_lines = file1.readlines()


# i kept getting /n on my numbers hence the use of .strip
for lines in all_lines:
    lines = lines.strip()
    lines = lines.split(',')

# variable for line 43
percentage = [lines[2]]

my_window = arcade.open_window(800, 800, "Populations Of Largest Nations")
arcade.set_background_color(arcade.color.WINE)

arcade.start_render()


# x and y axis
arcade.draw_line(100, 100, 800, 100, arcade.color.BLACK)
arcade.draw_line(100, 100, 100, 800, arcade.color.BLACK)

scale = (800 - 100) / len(range(100, 1500, 100))
currentY = 100

bar_height = (int(lines[1])-100_000_000)/1_000_000


#line 34,35,38,39 are attempts at making the percentages turn the bar either green or red

#if (int(float(lines[2])) >= 0):
    #arcade.color.GREEN


#if (int(lines[2]) < 0.00):
   # arcade.color.RED

# i dont understand how im supposed to put the percentages from the txt file into here and making it be able to adapt
# to another text file
for lines in percentage:
    if lines >= 0:
        arcade.color.GREEN
    else:
        arcade.color.RED


#y-axis labels
for i in range(100 ,1500, 100):
    currentlabel= arcade.Text(f"{i}M", 5, currentY, arcade.color.WHITE)
    currentlabel.draw()
    currentY += scale

#x-axis labels, this does not work i dont understand how to make it output the names or make it go across the chart horizontally
for i in all_lines:
    currentxlabel = arcade.Text(f"{lines[0]}", 120, 75, arcade.color.WHITE)
    arcade.draw_xywh_rectangle_filled(100, 120, 10, bar_height, bar_color )
    currentxlabel.draw()
    currentY += scale

arcade.finish_render()
arcade.run()

