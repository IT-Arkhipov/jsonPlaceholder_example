## Процесс тестирования нового функционала

Описание процесса тестирование представлено в двух файлах:

1. Процесс тестирования нового функционала.docx

1. Тест-кейсы.xlsx

---

## Тестирование API-методов GET, POST, DELETE сервера https://jsonplaceholder.typicode.com/

## Конфигурация окружения Windows
В переменной окружения PATH должен быть прописан путь к папке установленного Python 3.9+

Выгрузить и распаковать архив проекта https://github.com/IT-Arkhipov/jsonPlaceholder_example

### В папке с проектом произвести установку дополнительных фреймворков

`python -m pip install -r requirements.txt`

## Запуск автотестов из папки проекта

### Тестирование метода GET

`python -m pytest -s -v -k "TestGetMethod"`

Включает в себя тесты:

test_get_correct_response_code - проверка код ответа (200) на запрос списка постов

test_get_response_posts_quantity - проверка количества постов в системе (всегда 100)

test_get_response_is_json_format - проверка тела ответа на JSON-формат

test_get_response_code_for_specific_post_positive - проверка кода ответа (200) на запрос граничных значений номеров постов (1, 99, 100)

test_get_response_code_for_specific_post_negative - проверка кода ответа (404) на запрос граничных значений номеров постов (-1, 0, 101)

test_get_response_json_for_keys_presence - проверка тела ответа на наличие ключей userId, id, title, body

### Тестирование метода POST

`python -m pytest -s -v -k "TestPostMethod"`

Включает в себя тесты:

test_post_correct_response_code - проверка кода ответа (201) при создании поста

test_post_response_body_keys - проверка тела ответа на соответствие созданных ключей

test_post_response_new_id - проверка значения ключа `id` для созданного поста (101)

test_post_negative_body - проверка кода ответа (201) при различных структурах создаваемых постов

test_post_wrong_endpoint - проверка кода ответа (404) при отправке запроса создания поста с указанием номера поста

### Тестирование метода DELETE

`python -m pytest -s -v -k "TestDeleteMethod"`

Включает в себя тесты:

test_delete_response_code_posts - проверка кода ответа (200) на удаление номера поста различных значений (-1, 0, 101, 1, 99, 100)

test_delete_code_with_body - проверка кода ответа (200) на удаление поста с телом запроса содержимого поста

### Запуск всех тестов

`python -m pytest -s -v`

---

## Тестирование через Docker-образ

Выгрузить и распаковать архив проекта https://github.com/IT-Arkhipov/jsonPlaceholder_example

Загрузить docker-образ _python:alipne_

`docker pull python:alpine`

Скачать docker-образ по ссылке https://drive.google.com/file/d/1XLHs2vA7hN44KJyMt58tDuH6mCDNBW6J/view?usp=sharing (71,1 Мб)

Загрузить docker-файл с образом:

`docker load -i api_tests.tar`

Убедиться в наличии установленных образов:

`docker image ls`



> REPOSITORY      TAG     
> pytest_runner   latest    
> python          alpine    



### Запус тестов из папки с проектом (Dockerfile):

`docker run --rm --mount type=bind,src=<Полный путь до папки с проектом>,target=/tests/ pytest_runner`


### Запус тестов из папки с проектом (docker-compose.yml):

`docker-compose up`
