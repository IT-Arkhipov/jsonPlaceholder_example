## Тестирование API методов GET, POST, DELETE сервера https://jsonplaceholder.typicode.com/

## Конфигурация окружения Windows
В переменной окружения PATH должен быть прописан путь к папке установленного Python 3.9+

### Из папки с проектом произвести установку дополнительных фреймворков

`python -m pip install -r requirements.txt`

## Запуск автотестов из папки проекта

### Тестирование метода GET

`python -m pytest -s -v -k "TestGetMethod"`

Включает в себя тесты:

test_get_correct_response_code - проверка код ответа (200) на запрос списка постов

test_get_response_posts_quantity - проверка количества постов в системе (всегда 100)

test_get_response_is_json_format - проверка тела ответа на JSON-формат

test_get_response_code_for_specific_post_positive - проверка код ответа (200) на запрос граничных значений номеров постов (1, 99, 100)

test_get_response_code_for_specific_post_negative - проверка код ответа (404) на запрос граничных значений номеров постов (-1, 0, 101)

test_get_response_json_for_keys_presence - проверка тела ответа на наличие userId, id, title, body

### Тестирование метода POST

`python -m pytest -s -v -k "TestPostMethod"`

Включает в себя тесты:

test_post_correct_response_code - проверка кода ответа (201) при создании поста

test_post_response_body_keys - проверка тела ответа на соответствие созданных ключей

test_post_response_new_id - проверка значения ключа `id` для созданного поста (101)

test_post_negative_body - проверка кода ответа (201) на различные комбинации

test_post_wrong_endpoint - проверка кода ответа (404) при отправке запроса создания поста с указанием номера поста

### Тестирование метода DELETE

`python -m pytest -s -v -k "TestDeleteMethod"`

Включает в себя тесты:

test_delete_response_code_posts - проверка кода ответа (200) на удаление номера поста различных значений (-1, 0, 101, 1, 99, 100)

test_delete_code_with_body - проверка кода ответа (200) на удаление поста с телом запроса содержимого поста

### Запуск всех тестов

`python -m pytest -s -v`
