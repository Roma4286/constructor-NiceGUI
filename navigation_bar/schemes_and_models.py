import re
from typing import List

from pydantic import BaseModel, field_validator
from nicegui import ui

class BaseColorModel(BaseModel):
    @staticmethod
    def validate_hex_color(value: str) -> str:
        if not value.startswith('#') or len(value) not in {4, 7}:
            raise ValueError('The color must start with "#" and be 4 or 7 characters long.')
        hex_pattern = r'^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$'
        if not re.match(hex_pattern, value):
            raise ValueError('Invalid hex color code format.')
        return value


class Tabs(BaseColorModel):
    name: str
    icon_name: str
    icon_color: str = '#000'
    url: str

    @field_validator('icon_color')
    @classmethod
    def validate_icon_color(cls, value):
        return cls.validate_hex_color(value)


class Params(BaseColorModel):
    background_color: str
    active_tab_color: str
    name_active_tab: str
    length: int
    tabs: List[Tabs]

    @field_validator('background_color', 'active_tab_color')
    @classmethod
    def validate_colors(cls, value):
        return cls.validate_hex_color(value)


class MyModel:
    def __init__(self, params: Params):
        self.background_color = params.background_color
        self.active_tab_color = params.active_tab_color
        self.name_active_tab = params.name_active_tab
        self.length = params.length
        self.tabs = params.tabs

    def main_page(self):
        ui.add_head_html("""
        <style>
            body, html {
                margin: 0;
                padding: 0;
            }
        </style>
        <link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />
        """)

    def change_active_tab(self, name_tab: str):
        self.name_active_tab = name_tab

    # for tests
    def run(self):
        self.main_page()
        ui.run(reload=True)