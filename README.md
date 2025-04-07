```
src/
├── databases
│   ├── exceptions.py
│   ├── orm.py
│   ├── postgres
│   │   ├── crud
│   │   │   ├── base.py
│   │   │   └── dummy.py
│   │   ├── migrations
│   │   │   ├── env.py
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions
│   │   │       └── 2025-04-07-20-25_f7a28e30105b_init.py
│   │   ├── setup.py
│   │   └── tables
│   │       ├── base.py
│   │       └── dummy.py
│   └── sessions.py
├── domain
│   ├── collections
│   │   └── exceptions
│   │       └── dummy.py
│   ├── models
│   │   ├── base.py
│   │   └── dummy.py
│   ├── repositories
│   │   ├── base.py
│   │   └── dummy.py
│   └── services
│       └── dummy.py
├── endpoints
│   └── http
│       ├── const
│       │   └── tags.py
│       ├── openapi
│       │   └── dummy
│       │       ├── routers.py
│       │       └── schemas.py
│       ├── schemas.py
│       └── systemapi
│           └── dummy
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