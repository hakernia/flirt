Jak tworzyć wydruki flirtów i kart bingo.


Jak poprawnie pozbyć się pustych linii i dziwnych cudzysłowów z pliku utf-8:
	grep "^„" flirt-t.txt |sed 's/„//g' |sed 's/”//g' > flirt-tak.txt



# Struktura katalogów

	katalog główny - tu są:
		pliki wejściowe:
			bingo.csv
			flirt.txt
		skrypty:
			split9.py		
			split_flirt_into_pages_cli.py
		html-e formatujące wydruki:
			bingo.html
			flirt.html
	podkatalog img/     - obrazki wejściowe; ich nazwy są w bingo.csv

Dodatkowo tworzone są żądane podkatalogi wyjściowe przez oba skrypty py.
Szczegóły niżej.



# zgrupowanie flirtów z różnymi odcieniami do jednego pliku
parametry:
	-i <file> <file>  - 1-5 plików wejściowych z liniami tekstu
	-n 6              - liczba linii w których powinny się znaleźć cząstki z wszystki plików wejściowych
	-o <file>         - plik wyjściowy
	python interleave_n.py -i flirt-grzeczne.txt flirt-pazur.txt flirt-przecz.txt flirt-tak.txt -n 6 -o flirt.txt


# Podział flirtów na pliki do załadowania przez flirt.html
parametry:
	-i flirt.txt    - lista tekstów flirtowych
	-n 6            - karty będą miały po 6 tekstów
	-o teksty_po_6  - katalog wyjściowy

	python split_flirt_into_pages_cli.py -i flirt.txt -n 6 -o teksty_po_6


# Podział wróżb na pliki do załadowania przez bingo.html
parametry:
	-i bingo.csv    - lista wróżb w formacie "wróźba",<nazwa_pliku_obrazka>,x,y,z
	-o bingo        - katalog wyjściowy

	python split9.py -i bingo.csv -o bingo


# Odpalanie html-i

	python -m http.server

	http://localhost:8000/bingo.html
	http://localhost:8000/flirt.html
	
	W obu działa się tak samo:
	1. Wybierz plik wejściowy
	2. Wciśnij "Wczytaj flirt.csv" lub "Wczytaj CSV"
	3. Wciśnij Save as image

	Pliki obrazów z 9 kartami na stronie trafią do głównego katalogu.
	Stamtąd oddajemy je do druku.

