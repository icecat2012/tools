import screen_brightness_control as sbc
import os

if __name__ == '__main__':
	fpath = './screen-brightness.txt'
	if not os.path.exists(fpath):
		with open(fpath, 'w') as f:
			f.write('12\n')
			f.write('80\n')

	bright = None
	brights = list()
	with open(fpath, 'r') as f:
		for line in f:
			if bright is None:
				bright = int(line)
			else:
				brights.append(int(line))

	if bright < 101 and bright > 0:
		sbc.set_brightness(bright)
		brights.append(bright)

	with open(fpath, 'w') as f:
		for i in brights:
			f.write('{}\n'.format(i))

