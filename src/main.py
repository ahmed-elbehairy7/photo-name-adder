from os import listdir
from os.path import join, splitext
from get_dir import get_dir
from write import write


def main():
    dir = get_dir()
    output_dir = "test/output"

    for image in listdir(dir):
        write(join(dir, image), join(output_dir, image), splitext(image)[0])


if __name__ == "__main__":
    main()
