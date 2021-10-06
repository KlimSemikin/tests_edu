import json


class JsonConverter:
    @classmethod
    def is_json(cls, string):
        try:
            cls.from_json(string)
        except json.decoder.JSONDecodeError:
            return False
        return True

    @classmethod
    def from_json(cls, json_string):
        result = json.loads(json_string)
        return result

    @classmethod
    def to_json(cls, string):
        result = json.dumps(string)
        return result
