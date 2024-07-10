from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    async def parse(self, stream: bytes) -> dict:
        raise NotImplementedError

