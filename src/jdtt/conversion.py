import re
from enum import Enum
from typing import Dict
from dataclasses import dataclass

@dataclass
class Schema:
    name: str
    members: Dict[str, str]

class TargetLanguage(Enum):
    PYTHON = 1
    SCALA = 2

def schema_to_python_str(schema: Schema) -> str:
    formatter = "@dataclass\nclass {class_name}:\n{members}"
    member_str_list = []
    for member, mtype in schema.members.items():
        member_str_list.append(f"    {member}: {mtype}")
    members_str = "\n".join(member_str_list)
    return formatter.format(class_name=schema.name, members=members_str)

def schema_to_scala_str(schema: Schema) -> str:
    formatter = "case class {class_name}(\n{members}\n)"
    member_str_list = []
    for member, mtype in schema.members.items():
        member_str_list.append(f"    {member}: {mtype}")
    members_str = ",\n".join(member_str_list)
    return formatter.format(class_name=schema.name, members=members_str)

converters = {
    TargetLanguage.PYTHON: schema_to_python_str,
    TargetLanguage.SCALA: schema_to_scala_str
}

language_dtypes = {
    TargetLanguage.PYTHON: {
        "bool": "bool",
        "int": "int",
        "str": "str",
        "list": "list",
        "date": "datetime.datetime"
    },
    TargetLanguage.SCALA: {
        "bool": "Boolean",
        "int": "Int",
        "str": "String",
        "list": "IndexedSeq",
        "date": "DateTime"
    }
}

import_statements = {
    TargetLanguage.PYTHON: "import datetime\nfrom dataclasses import dataclass",
    TargetLanguage.SCALA: "import org.joda.time.DateTime"
}

file_extensions = {
    TargetLanguage.PYTHON: ".py",
    TargetLanguage.SCALA: ".scala"
}

date_regex = r"\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2})?(\.\d{3})?Z"

def json_to_schemas(schema, target_language: TargetLanguage, root_name="Root", detect_date=True) -> Dict[str, Schema]:
    """Converts a json schema to a dictionary of Schema objects."""
    return _json_to_schemas(root_name, schema, language_dtypes[target_language], {}, detect_date)

def _json_to_schemas(name, schema, dtypes: Dict[str, str], infos: Dict[str, Schema], detect_date: bool) -> Dict[str, Schema]:
    if not isinstance(schema, dict) or name in infos:
        return infos
    info = Schema(name, {})
    infos[name] = info
    for member, mvalue in schema.items():
        _get_or_create_member_type(member, mvalue, dtypes, info, infos, detect_date)
    return infos

def _get_or_create_member_type(member: str, mvalue, dtypes: Dict[str, str], info: Schema, infos: Dict[str, Schema], detect_date: bool):
    """Returns the type of a member, creating a new schema if necessary."""
    schema_type = type(mvalue)
    if detect_date and isinstance(mvalue, str) and re.match(date_regex, mvalue):
        info.members[member] = dtypes["date"]
    elif schema_type == bool:
        info.members[member] = dtypes["bool"]
    elif schema_type == int:
        info.members[member] = dtypes["int"]
    elif schema_type == str:
        info.members[member] = dtypes["str"]
    elif schema_type == list:
        item_name = member + "Item"
        count = 1
        while item_name in infos:
            item_name = member + "Item" + str(count)
            count += 1
        schema_item = mvalue[0]
        info.members[member] = f"{dtypes['list']}[{item_name}]"
        _json_to_schemas(item_name, schema_item, dtypes, infos, detect_date)
    else:
        info.members[member] = member
        _json_to_schemas(member, mvalue, dtypes, infos, detect_date)

def json_to_language_str(schema_json, target_language: TargetLanguage, root_name: str, detect_date=True) -> str:
    """Converts a json schema to a string of the target language."""
    infos = json_to_schemas(schema_json, target_language, root_name, detect_date)
    schema_strs = []
    to_language_str = converters[target_language]
    for _, schema in infos.items():
        schema_strs.append(to_language_str(schema))

    schema_str = "\n\n".join(schema_strs)
    target_import_statements = import_statements[target_language]
    return target_import_statements + "\n\n" + schema_str
