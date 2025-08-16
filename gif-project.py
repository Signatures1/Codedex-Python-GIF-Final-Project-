import imageio.v3 as iio

sillyfiles = ['gun.png', 'pussinboots.png', 'blawg.png'] #shapes aren't same but it works
pictures = [ ]

for silly in sillyfiles:
    pictures.append(iio.imread(silly))

iio.imwrite('team.gif', pictures, duration=600, loop=0)