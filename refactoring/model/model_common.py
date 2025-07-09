from bson import ObjectId

class PyObjectId(ObjectId):

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        # Menyesuaikan dengan format string pada OpenAPI schema
        return {"type": "string"}

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, info):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
