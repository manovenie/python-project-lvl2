from enum import Enum


class Status(Enum):
    ADDED = 'added'
    CHANGED = 'changed'
    DELETED = 'deleted'
    NESTED = 'nested'
    UNCHANGED = 'unchanged'
