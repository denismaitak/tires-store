from dataclasses import dataclass

__all__ = (
    'Season',
)


@dataclass
class Season:
    WINTER: str = 'winter'
    SUMMER: str = 'summer'
    ALL: str = 'all'
