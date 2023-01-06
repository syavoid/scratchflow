import json
from typing import Optional, TypeAlias, Union


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
    def __init__(self, token: str, id: str, lang: Optional[str] = None) -> None:
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


_AuthProtocol: TypeAlias = Union[Standard, Cookie]


class SessionClient:
    def __init__(self, auth: _AuthProtocol) -> None:
        self.auth = auth
        self.id = None
        self.common_token = dict()

        _type = isinstance(auth, (Standard, Cookie))

        if _type == (True, False):
            pass

        elif _type == (False, True):
            pass

        elif _type == (True, True):
            pass

        elif _type == (False, False):
            pass
