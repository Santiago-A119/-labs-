
def percentage_chart(numbers):
    print("=== PERCENTAGE CHART ===\n")

    
    valid = [n for n in numbers if (5 <= n <= 10) or (-10 <= n <= -5)]
    print("Filtered numbers:", valid, "\n")

  
    positive = len([n for n in valid if n > 0])
    negative = len([n for n in valid if n < 0])
    total = positive + negative if positive + negative != 0 else 1  

  
    pos_perc = positive * 100 / total
    neg_perc = negative * 100 / total

    
    print(f"Positive numbers: {pos_perc:5.1f}% | {'█' * int(pos_perc / 2)}")
    print(f"Negative numbers: {neg_perc:5.1f}% | {'█' * int(neg_perc / 2)}")


numbers = [-10, -8, -4, 5, 7, 9, 12]
percentage_chart(numbers)

