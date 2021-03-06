# Парсер рішень Миколаївської міської ради.
## можна використовувати як зразок для написання власних парсерів рішень.


```shell
mv .env-example .env
python main.py
```

Ваша задача як розробника написати парсер рішень який буде відправляти документ типу **[Document](https://github.com/Svyat33/mmr_docs_parse/blob/874269d9c53330950551be290694fe23b372dd22/parse/struct.py#L40)** перетворенний у JSON формат на ендпоінт сервісу.
Валідатори типів у Document можуть пояснити тип полей. Зауважте, якщо рішення викладаються у форматі doc, то зміст doc файлу треба передавати у бейз64 вигляді у поле file_content, та file_type має бути саме doc. 

Зауважте, що API ключ потрібно одержати індівідуально для парсеру.

Якщо документ вже додавався то HTTP стстус відповіді буде 400 з текстом `{"link": ["Document from this link already stored"]}`

Якщо це новий документ до HTTP статус 201 та відповідь виду 
```json
{"pk": 12, 
  "region_id": 13, 
  "file": "/srv/site/uploads/13/4e6b8ad520455dcc9a91fcf14d88d241.txt", 
  "link": "https://mkrada.gov.ua/documents/37182.html", 
  "title": "6/95, 8 Липня 2021", 
  "radaname": "Миколаївський р-н, Миколаївська міська рада", 
  "problems": {}, 
  "status": 1}
```