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
│   │   │       ├── base.cpython-313.pyc
│   │   │       ├── dummy.cpython-313.pyc
│   │   │       └── __init__.cpython-313.pyc
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── env.py
│   │   │   ├── __pycache__
│   │   │   │   └── env.cpython-313.pyc
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions
│   │   │       ├── 2025-04-07-20-25_f7a28e30105b_init.py
│   │   │       ├── __init__.py
│   │   │       └── __pycache__
│   │   │           └── 2025-04-07-20-25_f7a28e30105b_init.cpython-313.pyc
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   └── setup.cpython-313.pyc
│   │   ├── setup.py
│   │   └── tables
│   │       ├── base.py
│   │       ├── dummy.py
│   │       ├── __init__.py
│   │       └── __pycache__
│   │           ├── base.cpython-313.pyc
│   │           ├── dummy.cpython-313.pyc
│   │           └── __init__.cpython-313.pyc
│   ├── __pycache__
│   │   ├── exceptions.cpython-313.pyc
│   │   ├── __init__.cpython-313.pyc
│   │   ├── orm.cpython-313.pyc
│   │   └── sessions.cpython-313.pyc
│   └── sessions.py
├── domain
│   ├── collections
│   │   ├── enums
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-313.pyc
│   │   ├── exceptions
│   │   │   ├── dummy.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── dummy.cpython-313.pyc
│   │   │       └── __init__.cpython-313.pyc
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-313.pyc
│   ├── __init__.py
│   ├── models
│   │   ├── base.py
│   │   ├── dummy.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── base.cpython-313.pyc
│   │       ├── dummy.cpython-313.pyc
│   │       └── __init__.cpython-313.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-313.pyc
│   ├── repositories
│   │   ├── base.py
│   │   ├── dummy.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── base.cpython-313.pyc
│   │       ├── dummy.cpython-313.pyc
│   │       └── __init__.cpython-313.pyc
│   └── services
│       ├── dummy.py
│       ├── __init__.py
│       └── __pycache__
│           ├── dummy.cpython-313.pyc
│           └── __init__.cpython-313.pyc
├── endpoints
│   ├── http
│   │   ├── const
│   │   │   ├── errors
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-313.pyc
│   │   │   │   └── tags.cpython-313.pyc
│   │   │   └── tags.py
│   │   ├── deps
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── openapi
│   │   │   ├── dummy
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── __init__.cpython-313.pyc
│   │   │   │   │   ├── routers.cpython-313.pyc
│   │   │   │   │   └── schemas.cpython-313.pyc
│   │   │   │   ├── routers.py
│   │   │   │   └── schemas.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-313.pyc
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   └── schemas.cpython-313.pyc
│   │   ├── schemas.py
│   │   └── systemapi
│   │       ├── dummy
│   │       │   ├── __init__.py
│   │       │   ├── __pycache__
│   │       │   │   ├── __init__.cpython-313.pyc
│   │       │   │   ├── routers.cpython-313.pyc
│   │       │   │   └── schemas.cpython-313.pyc
│   │       │   ├── routers.py
│   │       │   └── schemas.py
│   │       ├── __init__.py
│   │       └── __pycache__
│   │           └── __init__.cpython-313.pyc
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-313.pyc
├── framework
│   ├── application.py
│   ├── __init__.py
│   ├── logger.py
│   ├── __pycache__
│   │   ├── application.cpython-313.pyc
│   │   ├── __init__.cpython-313.pyc
│   │   ├── logger.cpython-313.pyc
│   │   └── settings.cpython-313.pyc
│   └── settings.py
├── __init__.py
├── __pycache__
│   └── __init__.cpython-313.pyc
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
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   └── routing.cpython-313.pyc
│   │   └── routing.py
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-313.pyc
├── utils
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   └── strings.cpython-313.pyc
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