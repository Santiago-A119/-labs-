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
       
        return [-10, -8, -4, 5, 7, 9, 12]

def filter_range(values):
    return [v for v in values if (5 <= v <= 10) or (-10 <= v <= -5)]

def chart_last_digit_distribution(values):
  
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

