from PIL import Image

if __name__ == '__main__':
    
    WIDTH = 1025
    HEIGHT = 512
    IMG = Image.new('RGB', (WIDTH, HEIGHT))

    pixel_set = IMG.load()
    for row in range(HEIGHT // 2):
        for col in range (WIDTH // 2):
            color = (row, abs(col - row), col)
            rev_col, rev_row = WIDTH - col - 1, HEIGHT - row - 1
            pixel_set[col, row] = color
            pixel_set[rev_col, row] = color
            pixel_set[col, rev_row] = color
            pixel_set[rev_col, rev_row] = color

    print("done.")
    IMG.show()
