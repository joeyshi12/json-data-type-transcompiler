import re
from enum import Enum
from typing import Dict
from dataclasses import dataclass

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

def schema_to_python_str(name: str, members: Dict[str, str]) -> str:
    formatter = "@dataclass\nclass {class_name}:\n{members}"
    member_str_list = []
    for member, mtype in members.items():
        member_str_list.append(f"    {member}: {mtype}")
    members_str = "\n".join(member_str_list)
    return formatter.format(class_name=name, members=members_str)

def schema_to_scala_str(name: str, members: Dict[str, str]) -> str:
    formatter = "case class {class_name}(\n{members}\n)"
    member_str_list = []
    for member, mtype in members.items():
        member_str_list.append(f"    {member}: {mtype}")
    members_str = ",\n".join(member_str_list)
    return formatter.format(class_name=name, members=members_str)

def schema_to_typescript_str(name: str, members: Dict[str, str]) -> str:
    formatter = "export interface {class_name} {{\n{members}\n}}"
    member_str_list = []
    for member, mtype in members.items():
        member_str_list.append(f"    {member}: {mtype};")
    members_str = "\n".join(member_str_list)
    return formatter.format(class_name=name, members=members_str)

converters = {
    TargetLanguage.PYTHON: schema_to_python_str,
    TargetLanguage.SCALA: schema_to_scala_str,
    TargetLanguage.TYPESCRIPT: schema_to_typescript_str
}

language_dtypes = {
    TargetLanguage.PYTHON: TargetLanguageTypes("bool", "int", "str", "list[{item_name}]", "datetime.datetime"),
    TargetLanguage.SCALA: TargetLanguageTypes("Boolean", "Int", "String", "IndexedSeq[{item_name}]", "DateTime"),
    TargetLanguage.TYPESCRIPT: TargetLanguageTypes("boolean", "number", "string", "{item_name}[]", "Date")
}

import_statements = {
    TargetLanguage.PYTHON: "import datetime\nfrom dataclasses import dataclass",
    TargetLanguage.SCALA: "import org.joda.time.DateTime",
    TargetLanguage.TYPESCRIPT: ""
}

file_extensions = {
    TargetLanguage.PYTHON: ".py",
    TargetLanguage.SCALA: ".scala",
    TargetLanguage.TYPESCRIPT: ".ts"
}

date_regex = r"\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2})?(\.\d{3})?Z"

def json_to_schemas(schema_json, target_language: TargetLanguage, root_name="Root", detect_date=True) -> Schema:
    """Converts a json schema to a dictionary of Schema objects."""
    return _json_to_schemas(root_name, schema_json, language_dtypes[target_language], {}, detect_date)

def _json_to_schemas(name: str, schema_json, dtypes: TargetLanguageTypes, schema: Schema, detect_date: bool) -> Schema:
    if not isinstance(schema_json, dict) or name in schema:
        return schema
    members = {}
    schema[name] = members
    for member, mvalue in schema_json.items():
        members[member] = _get_or_create_member_type(member, mvalue, dtypes, schema, detect_date)
    return schema

def _get_or_create_member_type(member: str, mvalue, dtypes: TargetLanguageTypes, schema: Schema, detect_date: bool):
    """Returns the type of a member, creating a new schema if necessary."""
    schema_type = type(mvalue)
    if detect_date and schema_type == str and re.match(date_regex, mvalue):
        return dtypes.date_type
    if schema_type == bool:
        return dtypes.bool_type
    if schema_type == int:
        return dtypes.int_type
    if schema_type == str:
        return dtypes.str_type
    if schema_type == list:
        item_name = member + "Item"
        count = 1
        while item_name in schema:
            item_name = member + "Item" + str(count)
            count += 1
        schema_item = mvalue[0]
        item_type = _get_or_create_member_type(item_name, schema_item, dtypes, schema, detect_date)
        return dtypes.list_type.format(item_name=item_type)
    _json_to_schemas(member, mvalue, dtypes, schema, detect_date)
    return member

def json_to_language_str(schema_json, target_language: TargetLanguage, root_name="Root", detect_date=True) -> str:
    """Converts a json schema to a string of the target language."""
    infos = json_to_schemas(schema_json, target_language, root_name, detect_date)
    schema_strs = []
    to_language_str = converters[target_language]
    for name, schema in infos.items():
        schema_strs.append(to_language_str(name, schema))

    schema_str = "\n\n".join(schema_strs)
    target_import_statements = import_statements[target_language]
    return target_import_statements + "\n\n" + schema_str
