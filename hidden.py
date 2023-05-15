class Header:
    def __init__(self, width: int, height: int, max_color: int):
        self.width = width
        self.height = height
        self.max_color = max_color


class Pixel:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f"({self.red}, {self.green}, {self.blue})"


# Design Recipe
# 1) read a ppm file and get its header and pixels
# 2) read_file(fname: str)->(Header, list[str])
# 3) template of function
#   - open file
#   - read first line
#   - strip and split the second line to get its width and height for header
#   - gets the third line for max color
#   - read through each line and strip it
# 4) test case:
# 5)

def read_file(fname: str) -> (Header, list[str]):
    fil = open(fname, 'r')
    fil.readline()
    rd = fil.readline().strip().split()
    header = Header(int(rd[0]), int(rd[1]), int(fil.readline()))
    pixels = []
    for line in fil:
        pixels.append(line.strip())
    return header, pixels


# Design Recipe
# 1) goes through a list of strings and makes pixels
# 2) make_pixels(lst: list[str]) ->list[Pixel]
# 3) template of function
#   - make empty list
#   - iterate through the list by 3
#   - make Pixel objects with the 3 items from the list
#   - append the pixel into the list
# 4) test case:
# 5)

def make_pixels(lst: list[str]) -> list[Pixel]:
    pix_obj = []
    for x in range(0, len(lst), 3):
        pix = Pixel(int(lst[x]), int(lst[x + 1]), int(lst[x + 2]))
        pix_obj.append(pix)
    return pix_obj


# Design Recipe
# 1) changes the pixel by multiplying red by 10 and making green and blue equal to the new red
# 2) pix_fix(lst: list[Pixel])->list[Pixel]
# 3) template of function
#   - make empty list
#   - cycle through the list of pixels
#   - multiply the red number by 10
#   - if the new red color is greater than 255 than make it equal to 255
#   - make two new variables for green and blue equal to the new red
#   - use the new variable to make new pixel objects
#   - append the new pixels into the list
# 4) test case:
# 5)

def pix_fix(lst: list[Pixel]) -> list[Pixel]:
    new_p = []
    for x in lst:
        n_red = x.red * 10
        if n_red > 255:
            n_red = 255
        n_green = n_red
        n_blue = n_red
        n_pixel = Pixel(n_red, n_green, n_blue)
        new_p.append(n_pixel)
    return new_p


# Design Recipe
# 1) writes to a new file with the using header and pixel list
# 2) new_ppm(fname: str, p_lst: list[Pixel], header: Header)
# 3) template of function
#   - try to open the new file to write if not exit
#   - for the first line write P3
#   - second line is the header
#   - third line is the max color
#   - go through the list of pixels and in each line write its value separately
# 4) test case:
# 5)

def new_ppm(fname: str, p_lst: list[Pixel], header: Header):
    try:
        filo = open(fname, 'w')
    except FileNotFoundError:
        print("cannot open")
        exit()
    filo.write('P3\n')
    filo.write(f"{header.width} {header.height}\n")
    filo.write(f"{header.max_color}\n")
    for p in p_lst:
        filo.write(f"{p.red} {p.green} {p.blue}\n")
    filo.close()

def main():
    file_name = input("Name of ppm file: ")
    header, lst_str = read_file(file_name)
    lst_p = make_pixels(lst_str)
    new_pixs = pix_fix(lst_p)
    out_file = input("Name of out file: ")
    new_ppm(out_file, new_pixs, header)

if __name__ == '__main__':
    main()