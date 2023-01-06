import json
from typing import Union


class _BaseAuth:
    def identity(self) -> str:
        return self.data


class Standard(_BaseAuth):
    def __init__(self, username: str, password: str) -> None:
        self.data = json.dumps({
            "username": username,
            "password": password
        })


class Cookie(_BaseAuth):
    def __init__(self, token: str, id: str, lang: Union[str, None] = None) -> None:
        if lang is None:
            self.data = json.dumps({
                "scratchcsrftoken": token,
                "scratchsessionsid": id
            })

        else:
            self.data = json.dumps({
                "scratchcsrftoken": token,
                "scratchsessionsid": id,
                "scratchlanguage": lang
            })


class SessionClient:
    def __init__(self, auth: Union[Standard, Cookie]) -> None:
        pass  # TODO: 認証処理 - requests または urllib
