# demo-pr-repo

Учебный репозиторий, чтобы показать работу с Pull Request.

## Что внутри
- `app.py` — функция приветствия и простая калькуляция скидки
- `tests/test_app.py` — тесты (pytest)
- `.gitignore` — стандартные исключения для Python

## Быстрый старт
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Как показать Pull Request
1. Форкните или склонируйте репозиторий:
   ```bash
   git clone <url-репозитория>
   cd demo-pr-repo
   ```
2. Создайте ветку под задачу:
   ```bash
   git checkout -b feature/greeting-name
   ```
3. Внесите правку (например, добавьте параметр в `greet`), закоммитьте:
   ```bash
   git add app.py
   git commit -m "Добавить персональное приветствие"
   git push -u origin feature/greeting-name
   ```
4. Откройте Pull Request в интерфейсе хостинга (GitHub / GitLab / Bitbucket):
   base: `main`, compare: `feature/greeting-name`.
5. Попросите коллегу поревьюить. CI (если настроен) запустит pytest.
6. После аппрува нажмите Merge — ветку можно удалить.
