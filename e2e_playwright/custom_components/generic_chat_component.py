# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2026)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit.components.v1 as components


_COMPONENT_PATH = Path(__file__).parent / "generic_chat_component"
_generic_chat_component = components.declare_component(
    "generic_chat_component",
    path=_COMPONENT_PATH,
)


def generic_chat_component(
    *,
    messages: list[dict[str, Any]],
    placeholder: str = "Message the assistant",
    user_label: str = "You",
    assistant_label: str = "Assistant",
    message_status: str = "ready",
    disabled: bool = False,
    height: int = 720,
    key: str = "generic_chat_component",
) -> dict[str, Any] | None:
    """Render a minimal, bidirectional custom chat component.

    Returns a JSON-serializable event like {"id": "...", "text": "..."} when
    the user submits a prompt from inside the component.
    """
    return _generic_chat_component(
        messages=messages,
        placeholder=placeholder,
        user_label=user_label,
        assistant_label=assistant_label,
        message_status=message_status,
        disabled=disabled,
        height=height,
        default=None,
        key=key,
    )
