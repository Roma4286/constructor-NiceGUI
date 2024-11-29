import re
from typing import List

from pydantic import BaseModel, field_validator
from nicegui import ui

class Tabs(BaseModel):
    name: str
    img: str
    url: str

class Params(BaseModel):
    background_color: str
    active_tab_color: str
    length: int
    tabs: List[Tabs]

    @field_validator('background_color', 'active_tab_color')
    @classmethod
    def validate_hex_color(cls, value):
        if not value.startswith('#') or len(value) not in {4, 7}:
            raise ValueError('The color must start with "#" and be 4 or 7 characters long.')
        hex_pattern = r'^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$'
        if not re.match(hex_pattern, value):
            raise ValueError('Invalid hex color code format.')
        return value

class MyModel:
    def __init__(self, params: Params):
        self.background_color = params.background_color
        self.active_tab_color = params.active_tab_color
        self.length = params.length
        self.tabs = params.tabs

    def setup(self):
        ui.add_head_html("""
        <style>
            body, html {
                margin: 0;
                padding: 0;
            }
        </style>
        """)

    # for tests
    def run(self):
        self.setup()
        ui.run(reload=True)