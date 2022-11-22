![KUL](beamer/logo_kul.jpeg)
# AI dla każdego

**AI dla każdego** to nazwa projektu zainicjowanego i prowadzonego przez [AI KUL](https://ai.kul.pl). 

Celem projektu jest stworzenie materiałów służących do nauki AI. Tworzone materiały są notatnikami Jupytera, zawierają zarówno tekst jak i wykonywalny kod Pythona lub R. Planowana jest również wersja "książkowa" materiałów.

## Schemat zależności 

Poniższy schemat pokazuje program studiów pierwszego stopnia [AI KUL](https://ai.kul.pl) uwzględniając ścieżki zależości zajęć, a tym samym również materiałów dydaktycznych. 

![schemat zależności zajęć](pliki_yEd/mapa%20zależności%20zajęć%20SI%20trans.png)


## Planowane materiały i wskaźnik postępu

### Semestr 1
1. Programowanie w języku Python 1 (100%)
2. Programowanie w języku Python 2 (70%)
3. Wprowadzenie do AI (90%)
4. Język programowania R (30%)

### Semestr 2
1. Teoretyczne podstawy reprezentacji wiedzy (60%)

### Semestr 3
1. Podstawy uczenia maszynowego (70%)
2. Głębokie sieci neuronowe (10%)

### Semestr 4
1. Głębokie sieci neuronowe w rozpoznawaniu obrazów (1%)
2. Przetwarzanie języka naturalnego (60%)
3. SI w sztuce (1%)

### Semestr 5
1. Etyka w AI (1%)
2. Głębokie sieci neuronowe w modelowaniu danych sekwencyjnych (1%)

### Semestr 6
1. Logika jako język programowania (1%)





## Organizacja tekstu w notatnikach

Notatniki powinny być zorganizowane zgodnie z zasadami podanymi poniżej. 

Celem "sztywnej" organizacji zawartości notatników jest późniejsza możliwość automaczycznego wygenerowania slajdów prezentacji LaTeX/Beamer.

Notatnik należy traktować jako rozdział większej całości.

### Nagłówki

Pierwsze trzy poziomy nagłówków powinny być używane w następujący sposób.

- Nagłówek pierwszego poziomu,'#', występuje tylko na początku w pierwszej komórce. To **tytuł rozdziału**. Pierwsza komórka nie powinna zawierać niczego innego poza nagłówkiem pierwszego poziomu.
- Nagłówek drugiego poziomu,'##', odpowiada **tytułowi sekcji rozdziału**. Powinien znajdować się w osobnej komórce.
- Nagłówek trzeciego poziomu, '###', odpowiada **paragrafowi sekcji**. Będzie również odpowidał **tytułowi slajdu**. Nagłówek trzeciego poziomu, wraz z treścią paragrafu powinien znajdować się w jednej komórce.

Pisząc "myśl slajdami"!

### Bibliografia

- Sekcja "Bibliografia" jest obowiązkowa i powinna znaleźć się na końcu.
- Musi być sformatowana jak poniżej:

```
## <span t="slide_title">Bibliografia</span>
- <span t="l1">Pierwsza pozycja</span>
- [<span t="l1">URL do materiałów</span>](URL do materiałów)
```
### Obrazy

Obrazy należy umieszczać za pomocą HTMLowego
```
<img src="../KATALOG/NAZWA_PLIKU" width="XXX">
```

`KATALOG` może mieć trzy wartości:

- `pliki_yEd` - to katalog zawierający obrazy utworzonych za pomocą yEd i ich źródła; obrazy utworzone za pomocą yEd powinny zostać wyeksportowane do formatu PNG.
- `pliki_z_internetu` - to katalog obrazów pobranych z internetu; w folderze znajduje się plik zrodla_zdjec.md, gdzie należy podać skąd został pobrany obraz
- `pliki_wlasne` - to katalog obrazów własnych innych niż obrazy utworzonych za pomocą yEd

### Treść slajdów

Napisaliśmy wyżej, że nagłówek trzeciego poziomu, '###', odpowiada paragrafowi sekcji i tytułowi slajdu jednocześnie, i że nagłówek trzeciego poziomu, wraz z treścią paragrafu powinien znajdować się w jednej komórce. 

Treść paragrafu, którą chcemy umieścić na slajdzie należy otoczyć znacznikami `<span t="TAG"></span>`. Wartościami `TAG` mogą być:

- `l1` - element listy poziomu 1
- `l2` - element listy poziomu 2
-  `q` - cytat lub definicja
-  `v` - kod, który zostanie umieszczony w środowisku verbatim

Jeśli w kolejnej komórce nie będzie tytułu (czyli nagłówka poziomu trzeciego), to slajd koresponsujący z tą komórką  będzie miał ten sam tytuł co poprzedni.

Umieść tabelę markdowna w znacznikach: `<div t="t"> TABELA_MARKDOWN </div>`, jeśli chesz, aby znalazła się na slajdach

## Generowanie slajdów

Aby wygenerować slajdy skorzystać z notatnika ipynb2beamer.ipynb. Skrypt generuje slajdy dla wszystkich notatników ze wskazanych folderów.

Wygenerowane slajdy znajdują się w pliku z rozszerzeniem `.tex` w katalogu `beamer`.

## Współpracownicy
- [Robert Trypuz](https://www.linkedin.com/in/robert-trypuz-a1262617/)
- [Paweł Garbacz](https://www.linkedin.com/in/pawel-garbacz-3b041318/)
- [Rafał Trójczak](https://www.linkedin.com/in/rafa-trjczak-a112b714b/)
- Krzysztof Pancerz

## Licencja

Materiały dostępne w tym repozytorium są objęte licencją 
- **Creative Commons Uznanie autorstwa - Użycie niekomercyjne - Bez Utworów Zależnych 4.0 Międzynarodowa Licencja Publiczna** [Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-shield]][cc-by]

[cc-by]: https://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%20NC%20ND%204.0-lightgrey.svg
