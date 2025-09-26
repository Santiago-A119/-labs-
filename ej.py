import time

CSI = '\x1b['
RESET = f'{CSI}0m'
ZERO = f'{CSI}0G'

def draw_line(offset, length, color=220):
    offset_part = ' ' * offset
    filled_part = ' ' * length
    line = f'{offset_part}{CSI}48;5;{color}m{filled_part}{RESET}'
    print(line)

def draw_romb(height):
    center = height // 2
    offset = height // 2
    step = 1
    length = 1

    for line in range(height):
        draw_line(offset, length)
        if line < center:
            offset -= step
            length += step * 2
        else:
            offset += step
            length -= step * 2
        time.sleep(0.05)

if __name__ == "__main__":
    draw_romb(15)
