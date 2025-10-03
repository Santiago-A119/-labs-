# grafico_porcentual.py
import re

def read_sequence(path="sequence.txt"):
    """Reads numbers from a file and returns a list of floats."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        nums = re.findall(r"[-+]?\d*\.?\d+", text)
        return [float(n) for n in nums]
    except FileNotFoundError:
        # Example fallback data
        return [-10, -8, -4, 5, 7, 9, 12]

def filter_range(values):
    """Keeps only numbers in [-10,-5] or [5,10]."""
    return [v for v in values if (5 <= v <= 10) or (-10 <= v <= -5)]

def chart_last_digit_distribution(values):
    """Draws a percentage chart of the last digit distribution (0-9)."""
    counts = [0] * 10
    for v in values:
        d = abs(int(round(v))) % 10
        counts[d] += 1
    total = sum(counts) if sum(counts) else 1
    print("\nPercentage chart by last digit:\n")
    for d, c in enumerate(counts):
        perc = c * 100.0 / total
        bar = "█" * int(round(perc / 2))  # each block ≈ 2%
        print(f"{d}: {perc:5.1f}% |{bar}")

if __name__ == "__main__":
    values = read_sequence()
    filtered = filter_range(values)
    print("Filtered values:", filtered)
    chart_last_digit_distribution(filtered)
