import random
from dataclasses import dataclass
from enum import StrEnum


class Emotion(StrEnum):
    JOY = "Freude"
    SADNESS = "Trauer"
    ANGER = "Wut"
    FEAR = "Angst"
    DISGUST = "Ekel"
    SURPRISE = "Überraschung"
    TRUST = "Vertrauen"


PALETTE_VERSION = "1.0"
TRIAL_COUNT = 10


@dataclass(frozen=True, slots=True)
class PaletteColor:
    id: str
    red: int
    green: int
    blue: int


PALETTE: tuple[PaletteColor, ...] = (
    PaletteColor("red", 217, 75, 101),
    PaletteColor("orange", 240, 145, 60),
    PaletteColor("yellow", 238, 205, 74),
    PaletteColor("green", 83, 166, 104),
    PaletteColor("cyan", 61, 177, 183),
    PaletteColor("blue", 42, 130, 190),
    PaletteColor("purple", 126, 91, 166),
    PaletteColor("pink", 216, 111, 157),
    PaletteColor("brown", 145, 99, 67),
    PaletteColor("gray", 126, 135, 143),
    PaletteColor("navy", 43, 65, 105),
    PaletteColor("teal", 47, 128, 119),
)


def select_palette_colors(
    palette: tuple[PaletteColor, ...] = PALETTE,
    count: int = TRIAL_COUNT,
) -> list[PaletteColor]:
    if count > len(palette):
        raise ValueError("The palette does not contain enough distinct colors.")
    return random.SystemRandom().sample(palette, count)
