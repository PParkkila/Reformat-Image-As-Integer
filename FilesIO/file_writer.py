from PIL import Image

# method for reading in a file and returning an image


def write_file(fname, output):

    f = open(fname,mode="w")

    f.write(output)

    f.close()


