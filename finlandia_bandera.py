import time

CSI = '\x1b['
RESET = f'{CSI}0m'

def draw_line(offset, length, color=255):  
    
    offset_part = ' ' * offset
    filled_part = ' ' * length
    line = f'{offset_part}{CSI}48;5;{color}m{filled_part}{RESET}'
    print(line)

def draw_finland_flag(scale=2, delay=0.03):

    H = 11 * scale
    W = 18 * scale
    THICK = 3 * scale

    x_left_white = 5 * scale      # inicio de cruz vertical
    y_top_white = 4 * scale       # inicio de cruz horizontal

    for y in range(H):

        in_horizontal_cross = y_top_white <= y < y_top_white + THICK
        
        line_str = ""
        for x in range(W):
            
            in_vertical_cross = x_left_white <= x < x_left_white + THICK

            if in_horizontal_cross or in_vertical_cross:
                line_str += f"{CSI}48;5;27m  {RESET}"  # azul
            else:
                line_str += f"{CSI}48;5;255m  {RESET}"  # blanco
        
        print(line_str)
        time.sleep(delay)

if __name__ == "__main__":
    draw_finland_flag(scale=2, delay=0.05)
