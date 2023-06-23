# pylint: disable=import-outside-toplevel
from typing import Callable, List, Any

from gptcache.utils.error import NotFoundError


class EvictionBase:
    """
    EvictionBase to evict the cache data.
    """

    def __init__(self):
        raise EnvironmentError(
            "EvictionBase is designed to be instantiated, "
            "please using the `EvictionBase.get(name, policy, maxsize, clean_size)`."
        )

    @staticmethod
    def get(name: str, policy: str, maxsize: int, clean_size: int, on_evict: Callable[[List[Any]], None], **kwargs):
        if name not in "memory":
            raise NotFoundError("eviction base", name)
        from gptcache.manager.eviction.memory_cache import MemoryCacheEviction

        return MemoryCacheEviction(policy, maxsize, clean_size, on_evict, **kwargs)
