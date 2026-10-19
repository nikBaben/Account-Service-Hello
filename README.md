# Account-Service-Hello

Учебный сервис: **GET /** → HTTP 200, текст `hello world`.

## Запуск на компьютере

```bash
docker compose up --build -d
curl http://127.0.0.1:38080/
docker compose down
```

## Тесты

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m pytest -q
```

## Автоматическая доставка

1. Push в `main` запускает тесты.
2. GitHub Actions собирает образ для Linux amd64 и публикует в GHCR с тегом SHA коммита.
3. Actions берёт точный digest образа и обновляет `image.env` в [Deployment-Hello](https://github.com/nikBaben/Deployment-Hello).
4. Этот commit запускает CD в Deployment-Hello. Сервер скачивает готовый образ.

Pull request запускает только тесты. `workflow_dispatch` позволяет повторить весь цикл вручную.

`DEPLOYMENT_REPO_SSH_KEY` — отдельный SSH deploy key с правом записи только в Deployment-Hello. GitHub создаёт `GITHUB_TOKEN` сам на время job; этот токен публикует образ только из данного репозитория.

Это открытый учебный репозиторий. Рабочий Account-Service в Test-CI-CD от него независим.
