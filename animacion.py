# animacion.py
import os, time

def clear_console():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def animate_three_frames(duration_sec=5):
    """Runs a simple 3-frame animation."""
    frames = ["(•  )", "( • )", "(  •)"]
    t0 = time.time()
    i = 0
    while time.time() - t0 < duration_sec:
        clear_console()
        print("Three-frame animation:\n")
        print(frames[i % len(frames)])
        i += 1
        time.sleep(0.2)

if __name__ == "__main__":
    animate_three_frames()
