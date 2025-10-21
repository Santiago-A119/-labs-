import csv
import random
import xml.etree.ElementTree as ET

PRICE_THRESHOLD = 200.0  # Variant 9
BIBLIO_COUNT = 20
AUTHOR_LIMIT = 10


# -------------------------------
# 1. Read and filter books
# -------------------------------
def load_books():
    try:
        with open("books-en.csv", encoding="latin-1") as file:
            # your file uses ";" as delimiter
            reader = csv.DictReader(file, delimiter=";")
            books = []
            for row in reader:
                try:
                    price = float(row["Price"])
                    if price > PRICE_THRESHOLD:
                        books.append(row)
                except (ValueError, KeyError):
                    continue

            if not books:
                print(" No books found with Price > 200.")
            else:
                print(f" Books loaded: {len(books)} (Price > {PRICE_THRESHOLD})")
            return books
    except FileNotFoundError:
        print(" File 'books-en.csv' not found.")
        return 


# -------------------------------
# 2. Count titles longer than 30 characters
# -------------------------------
def count_long_titles(books):
    count = sum(1 for b in books if len(b.get("Book-Title", "")) > 30)
    print(f" Number of titles longer than 30 characters: {count}")


# -------------------------------
# 3. Search by author
# -------------------------------
def search_by_author(books):
    author_name = input("Enter author name: ").strip().lower()
    results = [b for b in books if author_name in b.get("Book-Author", "").lower()]
    print(f"\n🔍 Found {len(results)} books by '{author_name}':")
    for b in results[:AUTHOR_LIMIT]:
        print(f"  {b['Book-Author']} — {b['Book-Title']} ({b['Year-Of-Publication']})")


# -------------------------------
# 4. Generate 20 bibliographic references
# -------------------------------
def create_bibliography(books):
    if not books:
        print("No books available.")
        return
    selected = random.sample(books, min(BIBLIO_COUNT, len(books)))
    with open("bibliography.txt", "w", encoding="utf-8") as out:
        for i, b in enumerate(selected, 1):
            out.write(f"{i}. {b['Book-Author']}. {b['Book-Title']} – {b['Year-Of-Publication']}\n")
    print("File 'bibliography.txt' created successfully.")


# -------------------------------
# 5. Show unique publishers
# -------------------------------
def show_unique_publishers(books):
    publishers = sorted(set(b["Publisher"] for b in books if b.get("Publisher")))
    print("\n📚 Unique publishers:")
    for p in publishers:
        print(" ", p)


# -------------------------------
# 6. Show Top 20 most popular books (by Downloads)
# -------------------------------
def top_20_books(books):
    if not books:
        print(" No books available to analyze.")
        return
    try:
        top = sorted(books, key=lambda x: float(x.get("Downloads", 0)), reverse=True)[:20]
        print("\n Top 20 most popular books (by Downloads):")
        for b in top:
            print(f"{b['Book-Title']} — {b['Downloads']} downloads")
    except Exception as e:
        print(" Error while sorting books:", e)


# -------------------------------
# 7. Parse currency.xml (Variant 9)
# -------------------------------
def parse_currency():
    try:
        tree = ET.parse("currency.xml")
        root = tree.getroot()
        num_codes = [int(x.text) for x in root.findall(".//NumCode") if x.text and x.text.isdigit()]
        char_codes = [x.text for x in root.findall(".//CharCode") if x.text]
        print("\n NumCode list:", num_codes)
        print(" CharCode list:", char_codes)
    except FileNotFoundError:
        print(" File 'currency.xml' not found.")
    except Exception as e:
        print("Error parsing XML:", e)


# -------------------------------
# Main program
# -------------------------------
def main():
    print("=== LAB #2 — Variant 9 (books-en.csv + currency.xml) ===")
    books = load_books()

    while True:
        print("\nMENU:")
        print("1 - Count titles > 30 characters")
        print("2 - Search books by author")
        print("3 - Create 20 bibliographic references")
        print("4 - Show unique publishers")
        print("5 - Show Top 20 popular books (by Downloads)")
        print("6 - Parse currency.xml (NumCode & CharCode)")
        print("0 - Exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            count_long_titles(books)
        elif choice == "2":
            search_by_author(books)
        elif choice == "3":
            create_bibliography(books)
        elif choice == "4":
            show_unique_publishers(books)
        elif choice == "5":
            top_20_books(books)
        elif choice == "6":
            parse_currency()
        elif choice == "0":
            print(" Exiting program.")
            break
        else:
            print(" Invalid option. Try again.")


if __name__ == "__main__":
    main()
