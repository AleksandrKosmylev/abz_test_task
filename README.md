### Описание
Тестовое задание для abz.agency

### Установка
Приложение использует  виртульное окружение Poetry
```
pipx install poetry
```

1. Скачать репозиторий и перейти в директорию с приложением :
    ```
   git clone git@github.com:AleksandrKosmylev/abz_test_task.git
   cd abz_test_task/
    ```
2. Установить зависимости: 
    ```
    make install
    ```
3. Активировать виртуальное окружение
   ```
    poetry shell
   ```
4. Мигрировать данные 
   ```
    make migration

5. Запустить  приложение:
   ```
   make run 
   ```
*. Заполнить приложение данными о сотрудниках/
   очистить базу данных сотрудников 

   ```
    make add_employees
    make delete_employees
   ```