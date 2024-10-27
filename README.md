# Template for a webapp

Tools used:

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLModel](https://sqlmodel.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [Asyncpg](https://magicstack.github.io/asyncpg/current/)
* [PostgreSQL](https://www.postgresql.org)

Useful tools:

* [jq](https://jqlang.github.io/jq/)
* [http](https://httpie.io/)
* [wrk](https://github.com/wg/wrk)

## Installation

Clone the repo.

Start dabtabase with `COMPOSE_PROFILES=infra docker compose up -d` and then

    uv sync
    make run

See the endpoints:
* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* [http://127.0.0.1:8000/users](http://127.0.0.1:8000/users)
* [http://127.0.0.1:8000/users/1](http://127.0.0.1:8000/users/1)

## Multiplatform builds

[OrbStack multiplatform](https://docs.orbstack.dev/docker/images#multiplatform)
[Docker multiplatform](https://docs.docker.com/build/building/multi-platform/#building-multi-platform-images)
[Docker container](https://docs.docker.com/build/drivers/docker-container)

### References

See [docs/manual.adoc](Manual) for documentation.

Sgerbwd means skeleton in Welsh.
