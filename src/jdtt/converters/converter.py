from typing import Dict


class Converter:
    def schema_to_string(schema: Schema, members: Dict[str, str]):
        raise NotImplemented()

Schema = Dict[str, Dict[str, str]]

class TargetLanguage(Enum):
    PYTHON = 1
    SCALA = 2
    TYPESCRIPT = 3

@dataclass
class TargetLanguageTypes:
    bool_type: str
    int_type: str
    str_type: str
    list_type: str
    date_type: str
