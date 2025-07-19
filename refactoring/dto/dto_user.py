from pydantic import BaseModel, validator


class InputUser(BaseModel):
    username: str
    password: str
    confirm_password: str
    name: str

    @validator("confirm_password")
    def passwords_matchs(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        
        return v

class InputLogin(BaseModel):
    username: str
    password: str