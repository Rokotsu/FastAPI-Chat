from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text


@dataclass
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

