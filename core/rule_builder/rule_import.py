from ... import OracleOfSeasonsWorld

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
    Rule = CoreRule[OracleOfSeasonsWorld]
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
