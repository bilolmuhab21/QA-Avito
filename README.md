# Тестовое задание QA (Avito)

## Описание

Проект содержит тест-кейсы и автотесты для проверки платформы модерации объявлений.

Проверяются:

* фильтр по цене
* сортировка
* фильтр категории
* тогл "Только срочные"
* страница статистики
* переключение темы

---

## Стек

* Python
* Pytest
* Playwright

---

## Установка

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
playwright install
```

---

## Запуск

```bash
pytest -v
```

---

## Примечание

Тесты не зависят от фиксированных данных, так как используется общий тестовый стенд.

---

## Файлы

* TESTCASES.md — тест-кейсы
* BUGS.md — найденные баги
* tests/ — автотесты
