from nicegui import ui, app


class LineApp:
    def __init__(self, position: str ="top", color: str = '#007BFF'):
        self.position = position
        self.color = color

    def setup(self):
        ui.add_head_html("""
        <style>
            body, html {
                margin: 0;
                padding: 0;
            }
        </style>
        """)

        with ui.row().style('margin: 0; padding: 0; width: 100%; height: auto;'):
            if self.position == "left":
                with ui.card().style(
                        f'background-color: {self.color}; width: 100px; position: fixed; left: 0; top: 0; bottom: 0; border-radius: 0;'):
                    pass
            elif self.position == "top":
                with ui.card().style(
                        f'background-color: {self.color}; height: 100px; position: fixed; left: 0; top: 0; right: 0; border-radius: 0;'):
                    pass
            else:
                raise ValueError("Invalid position. Use 'left' or 'top'.")

    def run(self):
        self.setup()
        ui.run(reload=True)


@ui.page('/')
def main_page():
    manager = LineApp(position='top', color='#30d5c8')
    manager.setup()

app.on_startup(main_page)
ui.run()
