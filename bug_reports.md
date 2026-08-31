# Bug reports

## BUG-1: POST /posts возвращает 201 без обязательных полей title и body

**Окружение**
- API: https://jsonplaceholder.typicode.com
- Endpoint: POST /posts
- Инструмент: pytest + requests (test_api.py, тест test_create_new_post_nobody)

**Шаги воспроизведения:**
1. Отправить POST-запрос на /posts с телом: {"userId": 1}
2. Посмотреть код ответа

**Ожидаемый результат:**
API должен вернуть 400, так как отсутствуют обязательные поля

**Фактический результат:**
API возвращает 201 и создает объект, в котором нет полей title и body

**Severity:** 
Minor

**Priority:**
Low

## BUG-2: POST /posts возвращает 201 но созданный объект не сохраняется

**Окружение**
- API: https://jsonplaceholder.typicode.com
- Endpoint: POST /posts, затем GET /posts/{id}
- Инструмент: pytest + requests (test_api.py, тест test_create_post_not_persisted)

**Шаги воспроизведения:**
1. Отправить POST-запрос на /posts с телом: {"title": "Test", "body": "Test", "userId": 1}
2. Получить ответ 201 и id нового объекта из ответа
3. Отправить GET-запрос на /posts/{полученный id}

**Ожидаемый результат:**
GET должен вернуть 200 и тот же объект, который был создан

**Фактический результат:**
GET возвращает 404 - объект не создан

**Severity:** 
Minor

**Priority:**
Low