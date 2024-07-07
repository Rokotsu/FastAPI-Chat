from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from app.domain.events.base import BaseEvent

ET = TypeVar(name='ET', bound=BaseEvent)
ER = TypeVar(name='ER', bound=Any)

@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    def handler(self, event: ET) -> ER:
        ...