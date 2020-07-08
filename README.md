Тестовый набор содержит тесты для 4 методов : GET, POST, PATCH, DELETE для SMOKE тестирования rest-api 
Помимо  описанных тестов для smoke тестирования, так же можно добавить следующие:
1. Для метода GET /api/users
проверить корректность параметров фильтрации по способу сортировки для полей id, firstName, lastName, email, dayOfBirth по способам desc, asc
2. Для метода GET /api/users проверить корректность по работе параметров page и size
3. Для метода GET /api/users проверить, что response  содержит json со списком всех users ( по умолчанию 20 ) 
4. Для метода PUT /api/users/{id} проверить, что обновление всех полей для user по переданному id работает корректно
5. Проверить,  что все сгенерированные id, enmail при запуске api уникальны
6. Проверить, что все сгенерированные даты выводятся в формате строки «YYYY-MM-DD» и  раньше текущей даты
7. Проверить, что длина сгенерированных firstName и lastName от 2 до 15 символов, от 2 до 30 символов соответсвенно.
8. Провести негативную проверку на тестирование ограничений через добавление нового юзера методом POST /api/users с содержанием всех полей, выходящих за пределы допустимых ограничений.
9. Провести валидацию json схемы модели User ( в python доступно с помощью from jsonschema import validate )
10.Проверить,что при попытке удаления/обновления user с несуществующим id response отдает корректный код ошибки (404)

### Requirements
```
requests==2.23.0
pytest==5.1.1
```

### Run the tests:
```
pytest -s -v tests_api.py
```
