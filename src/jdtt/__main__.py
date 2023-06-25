import json
import argparse
from jdtt.conversion import json_to_language_str, TargetLanguage, file_extensions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target_language", type=str, choices=["python", "scala", "typescript"], default="python", help="target language")
    parser.add_argument("--root_schema", type=str, default="Root", help="name of root schema")
    parser.add_argument("--detect_date", action="store_true", help="detect datetime fields and convert to date type")
    parser.add_argument("schema_path", type=str, help="filepath to schema json")
    args = parser.parse_args()

    schema_path = args.schema_path
    target_language = TargetLanguage[args.target_language.upper()]
    target_path = schema_path + file_extensions[target_language]

    with open(schema_path, "r", encoding="utf-8") as f:
        schema_json = json.loads(f.read())

    with open(target_path, "w", encoding="utf-8") as f:
        language_str = json_to_language_str(schema_json, target_language, args.root_schema)
        f.write(language_str)
        print(f"{args.target_language} schemas written to {target_path}")

if __name__ == "__main__":
    main()
