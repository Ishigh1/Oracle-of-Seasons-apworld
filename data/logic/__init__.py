from ...core.rule_builder.rule_import import Rule
from ...data.regions import RegionName

LogicLine = tuple[RegionName, RegionName, bool, Rule]
