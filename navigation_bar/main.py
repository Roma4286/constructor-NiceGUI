from nicegui import ui, app

from schemes_and_models import Params, MyModel

class LeftPanel(MyModel):
    def setup(self):
        super().setup()
        with ui.card().style(
                f'background-color: {self.background_color}; width: {self.length}px; position: fixed; left: 0; top: 0; bottom: 0; border-radius: 0;'):
            pass



class TopPanel(MyModel):
    def setup(self):
        super().setup()
        with ui.card().style(
                f'background-color: {self.background_color}; height: {self.length}px; position: fixed; left: 0; top: 0; right: 0; border-radius: 0;'):
            pass


@ui.page('/')
def main_page():
    p = Params(background_color='#30d5c8', active_tab_color='#30d5c8', length=100, tabs=[])
    manager = LeftPanel(p)
    manager.setup()

app.on_startup(main_page)
ui.run()
