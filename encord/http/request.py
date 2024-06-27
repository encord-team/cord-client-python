"""
---
title: "Request"
slug: "sdk-ref-request"
hidden: false
metadata:
  title: "Request"
  description: "Encord SDK Request."
category: "64e481b57b6027003f20aaa0"
---
"""

#
# Copyright (c) 2023 Cord Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
from typing import Any, Dict, List, Optional, Type, Union

from encord.http.query_methods import QueryMethods

UIDType = Union[None, int, str, Dict[str, str], Dict[str, object], List[int], List[str], List[Dict[str, str]]]


class Request:
    """
    Request object. Takes query parameters and prepares them for execution.
    """

    def __init__(
        self,
        query_method: QueryMethods,
        db_object_type: Type,
        uid: UIDType,
        timeout: int,
        connect_timeout: int,
        payload: Union[None, Dict[str, Any], List[Dict[str, Any]]],
    ) -> None:
        self.http_method = QueryMethods.POST
        self.data: str = json.dumps(
            {
                "query_type": db_object_type.__name__.lower(),
                "query_method": str(query_method),
                "values": {
                    "uid": uid,
                    "payload": payload,
                },
            }
        )
        self.timeout = timeout
        self.connect_timeout = connect_timeout

        self.headers: Optional[Dict] = None

    def __str__(self):
        return f"Request({self.http_method}, {self.data}, {self.headers}, {self.timeout}, {self.connect_timeout})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
