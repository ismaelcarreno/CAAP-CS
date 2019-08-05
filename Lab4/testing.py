import main
import turtle

print("This test file will take in any image and checks the execution through the image. It will load the list of colors and list of pixels. It will also draw out the image.")
name = input("Type the name of the file you're using. To quit type ':q'.\nOptions: [1]banana [2]pac_ghost [3]smile [4]spiderman [5]alien [6]mario [7]mushroom [8]yoshi\nImage name: ")
while name != ':q':
	file = "art/" + name + ".txt"
	def load(file):
		pixel_list, color_list = main.load_art(file)
		print("Pixel List: ", pixel_list)
		print("Color List: ", color_list)
	load(file)

	def ddraw(file):
		pixel_list, color_list = main.load_art(file)
		main.draw(pixel_list, color_list)
		# turtle.done()
	ddraw(file)
	name = input("Type the name of the file you're using. To quit type ':q'.\nOptions: [1]banana [2]pac_ghost [3]smile [4]spiderman [5]alien [6]mario [7]mushroom [8]yoshi\nImage name: ")


