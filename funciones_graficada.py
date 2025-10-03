# funciones de graficos en consola
def plot_function_first_quadrant(f=lambda x: x/2, x_max=10, width=60, height=20):
    y_max = f(x_max)
    canvas = [[" " for _ in range(width + 1)] for _ in range(height + 1)]

    for r in range(height + 1):
        canvas[r][0] = "|"
    for c in range(width + 1):
        canvas[height][c] = "-"
    canvas[height][0] = "+"

    for col in range(1, width + 1):
        x = x_max * col / width
        y = f(x)
        if 0 <= y <= y_max:
            row = height - int(round((y / y_max) * height))
            canvas[row][col] = "█"

    for r in range(height + 1):
        print("".join(canvas[r]))

plot_function_first_quadrant()
