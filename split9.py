#!/usr/bin/env python3
import os
import argparse


def split_lines_into_files(input_path, output_dir="output"):
    # --- Wczytaj wszystkie linie ---
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    os.makedirs(output_dir, exist_ok=True)

    chunk_size = 9
    file_counter = 1

    # --- Dziel po 9 linii ---
    for i in range(0, len(lines), chunk_size):
        chunk = lines[i:i+chunk_size]

        # Ustal zakres linii (numeracja od 1)
        first_line = i + 1
        last_line = i + len(chunk)

        filename = f"bingo-{first_line}-{last_line}.csv"
        output_path = os.path.join(output_dir, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            for line in chunk:
                f.write(line + "\n")

        file_counter += 1

    print(f"Gotowe! Zapisano {file_counter - 1} plików w katalogu '{output_dir}'.")
    

def main():
    parser = argparse.ArgumentParser(
        description="Dzieli plik na mniejsze pliki po 9 linii."
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Ścieżka do pliku wejściowego"
    )

    parser.add_argument(
        "-o", "--output",
        default="output",
        help="Katalog wyjściowy (domyślnie: output)"
    )

    args = parser.parse_args()

    split_lines_into_files(args.input, args.output)


if __name__ == "__main__":
    main()

