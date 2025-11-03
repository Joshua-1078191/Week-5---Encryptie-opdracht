# Week-5---Encryptie# Week 5 — Encryptie 
Repository: https://github.com/Joshua-1078191/Week-5---Encryptie-opdracht

Python CLI om tekst te versleutelen en te ontsleutelen met AES‑256‑GCM.

## Installatie
```bash
pip install -r requirements.txt
```

## Gebruik
- Encrypt:
```bash
python app.py encrypt --text "Hallo" --password "sterkWachtwoord"
```
- Decrypt (gebruik de exacte base64 van encrypt):
```bash
python app.py decrypt --data "HIER_BASE64" --password "sterkWachtwoord"
```

## Bestanden
- `app.py`
- `requirements.txt`

## Hoe de applicatie werkt
De applicatie laat je tekst versleutelen en weer ontsleutelen via de command line.

Je voert een tekst en een wachtwoord in. Met dat wachtwoord wordt automatisch een sleutel gemaakt waarmee de tekst wordt versleuteld met **AES-256-GCM**.

Bij elke versleuteling maakt de app een nieuwe **salt** en **nonce**, zodat het resultaat altijd uniek en veilig is.

De versleutelde tekst wordt omgezet naar base64 zodat je deze makkelijk kunt opslaan of delen.

Bij het ontsleutelen gebruik je hetzelfde wachtwoord om de originele tekst terug te krijgen.

---

## Gebruikte encryptiemethode en algoritme
De applicatie gebruikt **AES-256-GCM**, een moderne en veilige manier van symmetrische encryptie.

Deze methode zorgt ervoor dat de tekst geheim blijft en dat gecontroleerd kan worden of er niets is aangepast.

Ik heb voor AES-256-GCM gekozen omdat het:
- veilig en betrouwbaar is,
- snel werkt,
- en in veel beveiligde systemen wordt gebruikt, zoals HTTPS en VPN’s.

---

## Sleutelbeheer en beveiligingsimplicaties
De sleutel wordt niet opgeslagen, maar wordt afgeleid uit het wachtwoord van de gebruiker met de **Scrypt**-functie.

Dat maakt het moeilijk om wachtwoorden te raden met brute-force aanvallen.

Elke versleuteling gebruikt een nieuwe **salt** en **nonce**, zodat dezelfde tekst nooit hetzelfde resultaat geeft.

Het wachtwoord zelf wordt niet bewaard, dus de veiligheid hangt af van hoe sterk het wachtwoord is.

Voor persoonlijk gebruik is dit veilig, maar bij veel gebruikers is het lastiger om een gedeelde sleutel goed te beveiligen.

---

## Reflectie 
Kerckhoffs’s Principe zegt dat een versleutelingssysteem veilig moet blijven, ook als iedereen weet hoe het werkt, zolang alleen de sleutel geheim blijft.

Mijn applicatie voldoet aan dit principe, omdat alles over de werking en het algoritme (**AES-256-GCM** en **Scrypt**) bekend mag zijn.

De beveiliging hangt alleen af van het wachtwoord, niet van het geheimhouden van de code.

Zelfs als iemand de hele code kent, kan hij zonder de juiste sleutel de tekst niet ontsleutelen.

De gekozen methode past dus goed bij dit principe: de **veiligheid hangt af van de sleutel, niet van geheimhouding van het systeem**.

---

