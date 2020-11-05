import sys
import png
from plvl import Plvl

def split(a, n):
	k, m = divmod(len(a), n)
	return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def main(input_file):
	level = Plvl.from_file(input_file)
	rawscr = level.unknown_header
	pixels = []

	# turn the raw screen into a list
	for i in rawscr:
		pixels.append(i)

	# split the list into 128-long list entries
	pixels = list(split(pixels, 128))

	# 
	reverse_pixels = []
	for i in range(127, -1, -1):
		reverse_pixels.append(pixels[i])

	pngfile = open('exported.png', 'wb')
	pngwriter = png.Writer(128, 128, greyscale=True)
	pngwriter.write(pngfile, reverse_pixels)
	pngfile.close()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("[WARNING] No file chosen, will use level.plvl in working directory if it exists.")
		main("level.plvl")
	else:
		main(sys.argv[1])
