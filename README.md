## Тестирование API методов GET, POST, DELETE сервера https://jsonplaceholder.typicode.com/

## Конфигурация окружения Windows
В системе должен быть установлен Python 3.9+, прописаны пути к папке установки ..\Python3x, ..\Python3.x\Scripts

### Произвести установку дополнительных фреймворков

`pip3 install -r requirements.txt`

## Запуск автотестов из папки проекта

### Тестирование метода GET

`pytest -s -v -k "TestGetMethod"`

Включает в себя тесты:

test_get_correct_response_code - проверка код ответа (200) на запрос списка постов

test_get_response_posts_quantity - проверка количества постов в системе (всегда 100)

test_get_response_is_json_format - проерка тела ответа на JSON-формат

test_get_response_code_for_specific_post_positive - код ответа (200) на запрос граничных значений номеров постов (1, 99, 100)

test_get_response_code_for_specific_post_positive - код ответа (404) на запрос граничных значений номеров постов (-1, 0, 101)

test_get_response_json_for_keys_presence - проверка тела ответа на наличие userId, id, title, body

### Тестирование метода POST

`pytest -s -v -k "TestPostMethod"`

### Тестирование метода DELETE

`pytest -s -v -k "TestDeleteMethod"`

### Запуск всех тестов

`pytest -s -v`
