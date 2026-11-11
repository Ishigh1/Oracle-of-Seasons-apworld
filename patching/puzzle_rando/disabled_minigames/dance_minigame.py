from ....common.patching.RomData import RomData
from ....common.patching.z80asm.Assembler import GameboyAddress


def skip_dance(rom: RomData):
    rom.write_word(GameboyAddress(0x09, 0x5C12).address_in_rom(), 0xCF5D)
