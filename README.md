<p align="center">
  <a href="https://github.com/AlexDemure/gadfastapi">
    <a href="https://ibb.co/YB0bHZCd"><img src="https://i.ibb.co/hFYC3f6d/logo.png" alt="logo" border="0"></a>
  </a>
</p>

<p align="center">
  File architecture for FastApi app
</p>

---

This repository presents a modular file architecture for FastAPI applications — with a focus on simplicity, clarity, and separation of concerns. It’s designed to help developers quickly scaffold and maintain clean service layers across databases, domain logic, endpoints, and framework configuration.

At the moment, the project is evolving around the idea of **code generation and automation** — reducing boilerplate by generating typical service code (repositories, services, endpoints, schemas), while leaving business logic implementation in a dedicated space. The goal is to speed up development without losing flexibility and control.

Explore the templates or try generating your own modules with:

```shell
uv init; uv add gadcodegen isort ruff;

# Add project
uv run gadcodegen -f https://raw.githubusercontent.com/AlexDemure/gadfastapi/refs/heads/main/.templates/project.toml;

# Add module
uv run gadcodegen -f https://raw.githubusercontent.com/AlexDemure/gadfastapi/refs/heads/main/.templates/module.toml --context '{"module": {"snake": {"single": "user", "many": "users"}, "pascal": {"single": "User", "many": "Users"}, "kebab": {"single": "user", "many": "users"}}}';
```
```>>> tree```
```shell
src/
├── databases
│   ├── exceptions.py
│   ├── orm.py
│   ├── postgres
│   │   ├── crud
│   │   ├── migrations
│   │   ├── setup.py
│   │   └── tables
│   └── sessions.py
├── domain
│   ├── collections
│   │   └── exceptions
│   ├── models
│   ├── repositories
│   └── services
├── endpoints
│   └── http
│       ├── const
│       │   └── tags.py
│       ├── openapi
│       │   └── {{module}}
│       │       ├── routers.py
│       │       └── schemas.py
│       ├── schemas.py
│       └── systemapi
│           └── {{module}}
│               ├── routers.py
│               └── schemas.py
├── framework
│   ├── application.py
│   ├── logger.py
│   └── settings.py
├── storages
│   └── s3
│       └── setup.py
├── tools
│   └── fastapi
│       └── routing.py
└── utils
    └── strings.py
tests/
├── conftest.py
├── const.py
├── test_integrations
│   └── conftest.py
└── test_units
    └── conftest.py
```