# Projekt do webových aplikací

Od 3tí lekce jsem vše doplňoval do jednoho projektu, proto to není dále rozdělno. Nechtěl jsem dělat zbytečně kopie, když jsou to stejně změny, které jsou oddělené

Vše se spouští pomocí `docker compose up`, u lecture_3 se pak spustí i REST API posledního úkolu.

## REST API

- připojeno přes docker compose, testování:

```bash

curl http://localhost:3000/get
curl http://localhost:3000/get/1

curl -X DELETE http://localhost:3000/delete/1

curl -X POST http://localhost:3000/post \
    -H "Content-Type: application/json" \
    -d '{"name": "Roman", "lastname": "Příjmení", "email": "roman@seznam.cz"}'

curl -X POST http://localhost:3000/update/41 \
    -H "Content-Type: application/json" \
    -d '{"name": "Roman", "lastname": "Příjmení", "email": "roman.nema@seznam.cz"}'
