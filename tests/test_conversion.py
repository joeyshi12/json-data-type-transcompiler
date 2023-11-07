import os
import json
from typing import Dict
from jdtt.conversion import json_to_language_str, TargetLanguage


def test_conversions():
    directory_path = os.path.dirname(os.path.realpath(__file__))
    json_directory = os.path.join(directory_path, "json")
    json_files = os.listdir(json_directory)
    json_dict = {file_name.split(".")[0]: os.path.join(json_directory, file_name) for file_name in json_files}
    validate_schemas(os.path.join(directory_path, "schema", "python"), TargetLanguage.PYTHON, json_dict)
    validate_schemas(os.path.join(directory_path, "schema", "scala"), TargetLanguage.SCALA, json_dict)
    validate_schemas(os.path.join(directory_path, "schema", "typescript"), TargetLanguage.TYPESCRIPT, json_dict)


def validate_schemas(folder_path: str, target_language: TargetLanguage, json_dict: Dict[str, str]):
    for schema_file in os.listdir(folder_path):
        name = schema_file.split(".")[0]
        json_file_path = json_dict.get(name)
        if json_file_path is None:
            continue

        with open(json_file_path, "r") as f1:
            with open(os.path.join(folder_path, schema_file), "r") as f2:
                json_obj = json.load(f1)
                assert json_to_language_str(json_obj, target_language).strip() == f2.read().strip()
