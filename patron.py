def draw_pattern_h(rows=6, cols=8):
    rombo = [
        "●●"
    ]
    for r in range(rows):
        for line in rombo:
            print((line * cols)[:cols * len(line)])

draw_pattern_h()
