[![Python application](https://github.com/Eik-Lab/GITHUB_WS_CICD/actions/workflows/python-app.yml/badge.svg)](https://github.com/Eik-Lab/GITHUB_WS_CICD/actions/workflows/python-app.yml)
# GIT WORKSHOP

## Introduksjon
Dette er en workshop som går videre fra grunnleggende git-kommandoer. Vi skal i dag se på GIT CI/CD, og hvordan vi kan bruke git til å automatisere bygging og testing av kode.

## Forutsetninger
- Du har installert git på maskinen din
- Du har en github-konto
- Du har installert Visual Studio Code

## Hva er CI/CD?
CI/CD står for Continuous Integration/Continuous Deployment. Dette er en praksis innen softwareutvikling hvor utviklere jobber i små, hyppige endringer, og hvor disse endringene automatisk bygges og testes. 

## Hvorfor CI/CD?
CI/CD hjelper oss med å oppdage feil tidlig i utviklingsprosessen, og gjør det enklere å fikse disse feilene. Dette gjør at vi kan levere kode raskere, og med høyere kvalitet. 

## OK, hva betyr dette for meg?
I dag skal vi se på hvordan vi kan bruke github actions til å automatisere bygging og testing av kode. Dette gjør vi ved å skrive enkle konfigurasjonsfiler som forteller github hva vi vil at den skal gjøre.

For eksempel, hvis vi lager en python applikasjon, kan vi lage vår egen autmatisrt test som sjekker at koden vår fungerer som den skal før vi pusher den til main-branchen. I dag skal vi se hvordan vi kan sette opp en slik test ved bruk av en pytest og en flake8 test.

Vi skal også se på hvordn vi kan teste en html-side ved bruk av en html-validator. Dette kan være nyttig hvis vi for eksempel lager en nettside, og vil være sikre på at den fungerer som den skal før vi pusher endringer den til main-branchen.


## La oss komme i gang!
1. Klon dette repoet til maskinen din ved å gå inn på EIK-lab sin github-side, finn dette repoet, og trykk på "fork" i øvre høyre hjørne. Dette lager en kopi av repoet på din egen github-konto.
2. Når du har gjort dette, kan du trykke på "Code" og kopiere "HTTPS" URL-en til repoet ditt.
3. Åpne Visual Studio Code, og trykk på "Clone GIT repository" i startvinduet. Lim inn URL-en til repoet ditt, og trykk enter.
4. Nå bør du ha en kopi av repoet ditt på maskinen din. Du skal ha tre filer i mappen:
- area.py: En python-fil som inneholder funksjoner som regner ut arealet av forskjellige figurer
- test_area.py: En python-fil som inneholder tester for funksjonene.
- README.md: En readme-fil som inneholder informasjon om repoet.

## La oss lage en github action!
Vi skal nå lage en github action som tester at koden vår fungerer som den skal. Vi skal bruke pytest til å teste at funksjonene våre fungerer som de skal, og flake8 til å sjekke at koden vår følger PEP8-standardene.

1. Vi gjør dette på den lette måten: Gå inn på github-siden din, og trykk på "Actions" i menyen.  Søk på "Python application", og trykk "Configure" når du finner filen.
2. Ved å inspisere filen som dukker opp, kan vi se at github har laget en konfigurasjonsfil for oss. Det er hovedsakelig to ting denne filen gjør:
- Den kjører en flake8-test for å sjekke at koden vår følger PEP8-standardene
- Den kjører en pytest-test for å sjekke at funksjonene våre fungerer som de skal.
3. Trykk på "Commit changes" for å lagre filen.

## Liten bonus, legg til en pass/fail-badge
Vi kan legge til en badge som viser om testene våre er vellykkede eller ikke. Dette gjør vi ved å legge til en liten kode i README.md.
1. Gå til Actions-fanen på github-siden din, og trykk på "Python application" helt til venstre. Helt øverst til høyre vil du se "...". Trykk på denne, og velg "Create status badge". Kopier koden som dukker opp.
2. Gå tilbake til VSCode, og åpne README.md. Lim inn koden du kopierte helt øverst i dokuentet, og trykk på "Commit" for å lagre endringene.
3. Når du nå går tilbake til github-siden din, vil du se en badge øverst i README.md som viser om testene dine er vellykkede eller ikke.

Med en status-badge i README.md, kan du enkelt se om testene dine er vellykkede eller ikke, uten å måtte gå inn på github-siden din.

Badgen din vil se slik ut:
[![Python application](https://github.com/Envestoren/GIT_workshop_2/actions/workflows/python-app.yml/badge.svg)](https://github.com/Envestoren/GIT_workshop_2/actions/workflows/python-app.yml)



## La oss prøve det ut!
1. Når du la til actionen, begynte github autmatisk å kjøre testene for deg. Du kan se resultatet av testene ved å trykke på "Actions" i menyen, og deretter på "Python application". Her kan du se at testene kjørte, og at de var vellykkede. Så lenge du ikke har endret noe i koden, skal testene være vellykkede.
2. Prøv å endre på koden, og se hva som skjer. Gå inn i area.py, og finn denne funksjonen:
```python 
def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError('Length and width must be positive numbers')
    return length * width
```
Endre denne funksjonen slik at du adderer lengde og bredde istedenfor å multiplisere dem. Slik:
```python
def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError('Length and width must be positive numbers')
    return length + width
```

Når du nå pusher endringene til main-branchen, vil github kjøre testene for deg. Du vil se at testene feiler, og at du får en rød "X" ved siden av commiten din. Dette er fordi testene feilet, og du kan se hva som gikk galt ved å trykke på "Python application" i menyen, og deretter på commiten din. Her kan du se at testene feilet, og at det var fordi vi endret på koden vår.

Du ser også at badgen din har endret seg til en rød "X", som viser at testene dine feilet. Om den ikke oppdaterer seg med en gang, kan du prøve å refreshe siden din med "CTRL + SHIFT + R"

3. Endre koden tilbake til det den var, og push endringene til main-branchen. Nå skal testene være vellykkede igjen.

4. La oss nå prøve å få en flake8-test til å feile. Gå inn i area.py, og legg til en ekstra linje med kode nederst i filen. For eksempel:
```python
def
```
Ved å kun skrive "def" uten å skrive en funksjon, vil vi få en flake8-feil. Push endringene til main-branchen, og se hva som skjer. Du vil se at testene feiler, og at du får en rød "X" ved siden av commiten din. Dette er fordi flake8-testen feilet, og du kan se hva som gikk galt ved å trykke på "Python application" i menyen, og deretter på commiten din. Her kan du se at testene feilet, og at det var fordi vi endret på koden vår.

5. Endre koden tilbake til det den var, og push endringene til main-branchen. Nå skal testene være vellykkede igjen.

## Du har nå laget din første github action!

## La oss lage en ny action!
Vi skal nå lage en ny action som tester at en html-side fungerer som den skal. Vi skal bruke en html-validator til å sjekke at html-siden vår er skrevet riktig.

Før vi begynner, skrur vi av python-actionen vi lagde tidligere. Dette gjør vi ved å gå inn på github-siden din, trykke på "Actions" i menyen, og deretter på "Python application". Trykk på "Disable workflow" øverst til høyre.

1. Gå til VSCode, og lag en ny fil som heter "index.html". Skriv inn følgende kode:
```html
<!DOCTYPE html>
<html lang="no">
    <head>
        <title>Min første nettside</title>
    </head>
    <body>
        <h1>Hei, verden!</h1>
    </body>
</html>
```

2. Push denne filen til Github.

3. Gå inn på github-siden din, og trykk på "Actions" i menyen. Trykk på "New workflow".

4. Velg "Set up a workflow yourself", og skriv inn følgende kode:
```yaml
name: HTML Validation

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  html_validation:
    name: Validate HTML
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2
      
      - name: Install Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'

      - name: Install HTML Validator
        run: npm install html-validator-cli -g

      - name: Validate HTML
        run: html-validator --verbose --file ./index.html
```
4. Trykk på "Commit changes" for å lagre filen. Kall filen "html-validation.yml".
5. Når du har lagt til actionen, begynner github automatisk å kjøre testene for deg. Du kan se resultatet av testene ved å trykke på "Actions" i menyen, og deretter på "HTML Validation". Her kan du se at testene kjørte, og at de var vellykkede. Så lenge du ikke har endret noe i koden, skal testene være vellykkede.

6. Gå til actions-fanen og finn "HTML  Validation". Trykk på de tre prikkene øverst til høyre, og velg "Create status badge". Kopier koden som dukker opp og lim den inn øverst i README.md under din første badge. Trykk på "Commit" for å lagre endringene.

7. Prøv å endre på koden, og se hva som skjer. Gå inn i index.html, og endre linjen med "Hei, verden!" ved å fjerne den bakerste ">" For eksempel:
```html
    <h1>Hei, verden!</h1
```
8. Push endringene til main-branchen, og se hva som skjer. Du vil se at testene feiler, og at du får en rød "X" ved siden av commiten din. Dette er fordi testene feilet, og du kan se hva som gikk galt ved å trykke på "HTML Validation" i menyen, og deretter på commiten din. Her kan du se at testene feilet, og at det var fordi vi endret på koden vår.

9. Endre koden tilbake til det den var, og push endringene til main-branchen. Nå skal testene være vellykkede igjen.

## Bygge og deploye en nettside
Vi har nå laget en action som sjekker at html-siden vår er skrevet riktig. La oss nå se på hvordan vi kan bygge og deploye en nettside ved bruk av github actions.
1. Gå til innstillinger på github-siden din, og trykk på "Pages" i menyen til venstre.
2. I source velger du "Github actions"
3. Velg "Deploy static content to page" workflow-filen, og trykk "Save"
4. Vi trenger ikke å gjøre noe mer, github vil nå automatisk bygge og deploye nettsiden vår for oss. Du kan se statusen til byggingen ved å trykke på "Actions" i menyen, og deretter på "Deploy static content to page". Her kan du se at github bygger og deployer nettsiden din for deg.

## Hvordan finne nettsiden din?
1. Trykk på innstillinger ved siden av about-fanen.
2. Under "Website", huk av for "Use your GitHub website". 
3. Du vil nå se en link under "about"

## Oppsummering
I dag har vi sett på hvordan vi kan bruke github actions til å automatisere bygging og testing av kode. Vi har sett på hvordan vi kan bruke pytest og flake8 til å teste en python-applikasjon, og hvordan vi kan bruke en html-validator til å teste en html-side. Vi har også sett på hvordan vi kan bygge og deploye en nettside ved bruk av github actions.



