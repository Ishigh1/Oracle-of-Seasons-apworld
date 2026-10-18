try:
    from rule_builder.rules import (
        And,
        AtLeast,
        CanReachRegion,
        False_,
        Has,
        HasAll,
        HasFromList,
        HasGroup,
        Or,
        True_,
    )
    from rule_builder.rules import Rule as CoreRule

    from ... import OracleOfSeasonsWorld
    Rule = CoreRule[OracleOfSeasonsWorld]

    # RB needs to implement the from_resolved we are expecting and implementing the optimization tied to it
    if not hasattr(Or, "from_resolved"):
        raise ImportError("#6085 is missing")
    from collections.abc import Iterator
    if Or.from_resolved.__annotations__["children_to_process"].__origin__ is not Iterator:
        raise ImportError("#6478 is missing")
except ImportError:
    from .rules import And, AtLeast, CanReachRegion, False_, Has, HasAll, HasFromList, HasGroup, Or, Rule, True_

__all__ = [
    "And",
    "AtLeast",
    "CanReachRegion",
    "False_",
    "Has",
    "HasAll",
    "HasFromList",
    "HasGroup",
    "Or",
    "Rule",
    "True_",
]
