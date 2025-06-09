# Generic single-database configuration.

## Add revision

```bash
alembic revision -m "<revision description>"
```

### With path to alembic.ini revision

```bash
alembic -c <path to alembic.ini> revision -m "<revision description>"
```

## Start migration

```bash
alembic upgrade head
```

### With path to alembic.ini revision

```bash
alembic -c <path to alembic.ini> upgrade head
```