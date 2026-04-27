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

import streamlit as st

from streamlit.components.generic_chat import generic_chat


def build_response(prompt: str) -> str:
    return (
        "This is a demo response from a generic custom chat component.\n\n"
        f"1. Received prompt: {prompt}\n"
        "2. The input lives inside the component iframe.\n"
        "3. The component returns a JSON event to Python."
    )


st.set_page_config(page_title="Generic chat component", layout="wide")
st.title("Generic chat component")

if "generic_chat_messages" not in st.session_state:
    st.session_state.generic_chat_messages = [
        {
            "role": "assistant",
            "content": "Ask anything. This minimal chat surface is domain-neutral.",
        }
    ]

if "last_generic_chat_event_id" not in st.session_state:
    st.session_state.last_generic_chat_event_id = None

if st.button("Reset chat"):
    st.session_state.generic_chat_messages = []
    st.session_state.last_generic_chat_event_id = None
    st.rerun()

event = generic_chat(
    messages=st.session_state.generic_chat_messages,
    placeholder="Message the assistant",
    message_status="demo",
    key="generic_chat_demo",
)

if isinstance(event, dict):
    event_id = event.get("id")
    event_text = str(event.get("text", "")).strip()
    if event_text and event_id != st.session_state.last_generic_chat_event_id:
        st.session_state.last_generic_chat_event_id = event_id
        st.session_state.generic_chat_messages.append(
            {"role": "user", "content": event_text}
        )
        st.session_state.generic_chat_messages.append(
            {
                "role": "assistant",
                "content": build_response(event_text),
                "sources": ["generic_chat_component_demo.py"],
                "tool_trace": ["Received component value", "Appended mock response"],
            }
        )
        st.rerun()
