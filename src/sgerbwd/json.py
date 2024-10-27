import json
import typing as tp
from datetime import datetime as dt
from functools import partial

from sqlalchemy import Row

__all__ = ['dumps', 'jsonify_rows']


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):  # type: ignore
        if isinstance(obj, dt):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


dumps = partial(json.dumps, cls=ComplexEncoder)


def jsonify_rows(rows: list[Row[tp.Any]]) -> list[dict[str, tp.Any]]:
    """Jsonify sqlalchemy.Row.

    Different version and easier to read would be:

    .. code-block:: python
    resp = []
    for row in rows:
        resp.append(dict([x for x in zip(row._fields, row)]))

    return resp

    """
    resp = [dict([x for x in zip(row._fields, row, strict=False)]) for row in rows]

    return resp
