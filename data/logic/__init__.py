from rule_builder.rules import Rule as BaseRule
from worlds.tloz_oos import OracleOfSeasonsWorld
from worlds.tloz_oos.data.regions import RegionName

Rule = BaseRule[OracleOfSeasonsWorld]

LogicLine = tuple[RegionName, str, bool, Rule | None] | tuple[RegionName, str, bool, Rule | None, bool]
