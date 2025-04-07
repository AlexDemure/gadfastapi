```
src/
├── clients
│   └── __init__.py
├── databases
│   ├── exceptions.py
│   ├── __init__.py
│   ├── orm.py
│   ├── postgres
│   │   ├── crud
│   │   │   ├── base.py
│   │   │   ├── dummy.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── base
│   │   │       ├── dummy
│   │   │       └── __init__
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── env.py
│   │   │   ├── __pycache__
│   │   │   │   └── env
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions
│   │   │       ├── 2025-04-07-20-25_f7a28e30105b_init.py
│   │   │       ├── __init__.py
│   │   │       └── __pycache__
│   │   │           └── 2025-04-07-20-25_f7a28e30105b_init
│   │   ├── __pycache__
│   │   │   ├── __init__
│   │   │   └── setup
│   │   ├── setup.py
│   │   └── tables
│   │       ├── base.py
│   │       ├── dummy.py
│   │       ├── __init__.py
│   │       └── __pycache__
│   │           ├── base
│   │           ├── dummy
│   │           └── __init__
│   ├── __pycache__
│   │   ├── exceptions
│   │   ├── __init__
│   │   ├── orm
│   │   └── sessions
│   └── sessions.py
├── domain
│   ├── collections
│   │   ├── enums
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__
│   │   ├── exceptions
│   │   │   ├── dummy.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── dummy
│   │   │       └── __init__
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__
│   ├── __init__.py
│   ├── models
│   │   ├── base.py
│   │   ├── dummy.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── base
│   │       ├── dummy
│   │       └── __init__
│   ├── __pycache__
│   │   └── __init__
│   ├── repositories
│   │   ├── base.py
│   │   ├── dummy.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── base
│   │       ├── dummy
│   │       └── __init__
│   └── services
│       ├── dummy.py
│       ├── __init__.py
│       └── __pycache__
│           ├── dummy
│           └── __init__
├── endpoints
│   ├── http
│   │   ├── const
│   │   │   ├── errors
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__
│   │   │   │   └── tags
│   │   │   └── tags.py
│   │   ├── deps
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── openapi
│   │   │   ├── dummy
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── __init__
│   │   │   │   │   ├── routers
│   │   │   │   │   └── schemas
│   │   │   │   ├── routers.py
│   │   │   │   └── schemas.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__
│   │   ├── __pycache__
│   │   │   ├── __init__
│   │   │   └── schemas
│   │   ├── schemas.py
│   │   └── systemapi
│   │       ├── dummy
│   │       │   ├── __init__.py
│   │       │   ├── __pycache__
│   │       │   │   ├── __init__
│   │       │   │   ├── routers
│   │       │   │   └── schemas
│   │       │   ├── routers.py
│   │       │   └── schemas.py
│   │       ├── __init__.py
│   │       └── __pycache__
│   │           └── __init__
│   ├── __init__.py
│   └── __pycache__
│       └── __init__
├── framework
│   ├── application.py
│   ├── __init__.py
│   ├── logger.py
│   ├── __pycache__
│   │   ├── application
│   │   ├── __init__
│   │   ├── logger
│   │   └── settings
│   └── settings.py
├── __init__.py
├── __pycache__
│   └── __init__
├── static
├── storages
│   ├── __init__.py
│   └── s3
│       ├── __init__.py
│       └── setup.py
├── tools
│   ├── fastapi
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__
│   │   │   └── routing
│   │   └── routing.py
│   ├── __init__.py
│   └── __pycache__
│       └── __init__
├── utils
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__
│   │   └── strings
│   └── strings.py
└── utils.py

56 directories, 110 files
```

```
tests/
├── conftest.py
├── const.py
├── factories
│   ├── __init__.py
│   └── models
│       └── __init__.py
├── __init__.py
├── mocking
│   └── __init__.py
├── test_integrations
│   ├── conftest.py
│   └── __init__.py
├── test_loads
│   └── __init__.py
└── test_units
    ├── conftest.py
    └── __init__.py

7 directories, 11 files
```