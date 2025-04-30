from gadfastetcd import Etcd
from src.framework import settings

etcd = Etcd(
    url=settings.ETCD_HOST,
    storage=settings.ETCD_STORAGE,
    settings=settings,
)
