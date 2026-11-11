from ....common.patching.RomData import RomData
from ....common.patching.z80asm.Assembler import Z80Assembler
from .dance_minigame import skip_dance
from .hide_and_seek import disable_hns


def disable_minigames(rom: RomData, assembler: Z80Assembler) -> None:
    disable_hns(assembler)
    skip_dance(rom)
