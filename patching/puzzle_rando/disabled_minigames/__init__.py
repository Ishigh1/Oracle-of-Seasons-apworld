from ....common.patching.z80asm.Assembler import Z80Assembler
from .hide_and_seek import disable_hns


def disable_minigames(assembler: Z80Assembler) -> None:
    disable_hns(assembler)
