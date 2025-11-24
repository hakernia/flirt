#!/usr/bin/env python3
import os
import argparse


def split_file_into_pages(input_path, n, output_dir="output"):

    # --- Wczytaj wszystkie linie ---
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # --- Katalog wyjściowy ---
    os.makedirs(output_dir, exist_ok=True)

    pages = []
    page_num = 1

    # --- Podział na strony ---
    for i in range(0, len(lines), n):
        fragment = lines[i:i+n]
        page = [f"- {page_num}"] + fragment
        pages.append(page)
        page_num += 1

    # --- Zapisywanie stron w blokach po 9 ---
    for i in range(0, len(pages), 9):
        chunk = pages[i:i+9]
        first_page = i + 1
        last_page = i + len(chunk)

        filename = f"flirt-{first_page}-{last_page}.csv"
        output_path = os.path.join(output_dir, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            for page in chunk:
                for line in page:
                    f.write(line + "\n")

    print(f"Gotowe! Zapisano { (len(pages)-1)//9 + 1 } plików w katalogu: {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Dzieli duży plik na strony po n linii i zapisuje je partiami po 9 stron."
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Ścieżka do pliku wejściowego"
    )

    parser.add_argument(
        "-n", "--n",
        required=True,
        type=int,
        help="Liczba linii przypadająca na jedną stronę"
    )

    parser.add_argument(
        "-o", "--output",
        default="output",
        help="Katalog wyjściowy (domyślnie: output)"
    )

    args = parser.parse_args()

    split_file_into_pages(args.input, args.n, args.output)


if __name__ == "__main__":
    main()

