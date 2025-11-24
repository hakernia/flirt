#!/usr/bin/env python3
import argparse
from collections import deque


def interleave_files(input_paths, n, output_path):

    # --- Wczytaj wszystkie pliki do kolejek ---
    queues = []
    for path in input_paths:
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        if lines:  # ignoruj puste pliki
            queues.append(deque(lines))

    # --- Plik wynikowy ---
    out = open(output_path, "w", encoding="utf-8")

    # --- Główna pętla ---
    while queues:
        # aktywne pliki = te, które nadal mają linie
        active = [q for q in queues if q]

        # jeśli zostały tylko puste kolejki → koniec
        if not active:
            break

        # jeśli aktywnych jest mniej niż wcześniej, usuwamy te puste
        queues = active

        # Zapewniamy: w każdej paczce n linii musi być
        # co najmniej jedna linia z każdego aktywnego pliku
        batch = []

        # 1) najpierw "obowiązkowe" linie — po jednej z każdej kolejki
        for q in queues:
            batch.append(q.popleft())

        # 2) jeśli miejsca zostało → uzupełniamy do n wykorzystując round-robin
        if len(batch) < n:
            i = 0
            while len(batch) < n and any(len(q) > 0 for q in queues):
                q = queues[i % len(queues)]
                if q:
                    batch.append(q.popleft())
                i += 1

        # zapisujemy paczkę
        for line in batch:
            out.write(line + "\n")

    out.close()
    print(f"Gotowe! Zapisano wynik do: {output_path}")
    


def main():
    parser = argparse.ArgumentParser(
        description="Miesza linie z kilku plików tak, aby w każdych n liniach był wkład z każdego wciąż dostępnego pliku."
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        nargs="+",
        help="Ścieżki do 1–5 plików wejściowych"
    )

    parser.add_argument(
        "-n", "--n",
        required=True,
        type=int,
        help="Wielkość grupy n, w której każdy aktywny plik musi mieć ≥ 1 linie"
    )

    parser.add_argument(
        "-o", "--output",
        default="wynik.txt",
        help="Plik wyjściowy (domyślnie wynik.txt)"
    )

    args = parser.parse_args()

    if not (1 <= len(args.input) <= 5):
        raise ValueError("Podaj od 1 do 5 plików!")

    interleave_files(args.input, args.n, args.output)



if __name__ == "__main__":
    main()

