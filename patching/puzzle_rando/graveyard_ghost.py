import random


def randomize_ghini(texts: dict[str, str]) -> None:
    if random.randint(0, 1) == 0:
        texts["TX_4c15"] = texts["TX_4c15"].replace("there were more", "had an odd count")
        texts["TX_4c17"] = texts["TX_4c17"].replace("were there more\nof", "was the odd\none")
