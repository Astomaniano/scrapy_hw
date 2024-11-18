# Задача:
## Напиши spider для нахождения всех источников освещения с сайта divan.ru

Нужно взять название источника освещения, цену и ссылку
Этот проект представляет собой Scrapy паука, который извлекает данные о товарах с сайта Divan.ru и сохраняет их в CSV файл.

# Установка

Чтобы запустить скрипт и получить CSV файл, следуйте следующим шагам:

#### Установите необходимые пакеты с помощью команды:
### pip install -r requirements.txt
#### Перейдите в папку spaiders с помощью команды:

### cd spaiders

#### Запустите скрипт с помощью команды:

### scrapy runspider lampsdivan.py -o lamps.csv
### Эти действия запустят Scrapy паука и сохранит данные в файл lamps.csv в той же директории.

LampsdivanSpider
Этот паук извлекает данные о товарах с сайта Divan.ru и сохраняет их в CSV файл. Паук использует Scrapy фреймворк для извлечения данных и сохранения их в CSV файл.

Примечания
Чтобы изменить настройки паука, откройте файл lampsdivan.py и измените необходимые параметры.
Чтобы получить более подробную информацию о пауке, используйте команду:

scrapy crawl --help