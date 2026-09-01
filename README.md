# QA Portfolio - API Testing (JSONPlaceholder)

Учебный проект по ручному и автоматизированному тестированию REST API. Объект тестирования - публичный бесплатный API [JSONPlaceholder](https://jsonplaceholder.typicode.com)

## Что внутри

| Папка / файл | Что это |
|---|---|
| `test-cases.md` | Ручные тест-кейсы: позитивные, негативные, пограничные сценарии |
| `bug_reports.md` | Найденные особенности/баги поведения API, оформленные как баг-репорты |
| `test_api.py` | Автотесты на `pytest` + `requests` |
| `insomnia_collection/jsonplaceholder.insomnia_collection.yaml` | Коллекция запросов для Insomnia (импортируется напрямую) |

## Запуск автотестов

pip install pytest requests

pytest test_api.py -v

