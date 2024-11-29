from nicegui import ui, app

from schemes_and_models import Params, Tabs, MyModel


class LeftPanel(MyModel):
    def setup(self):
        super().setup()


        with ui.card().style(
                f'background-color: {self.background_color}; width: {self.length}px; position: fixed; left: 0; top: 0; bottom: 0; border-radius: 0; display: flex; flex-direction: column; padding: 0; margin: 0; gap: 2px'):
            for panel in self.tabs:
                with ui.card().style(
                        f'background-color: {self.background_color}; width: {self.length}px; height: 30px; padding: 0; border-radius: 0; box-shadow: none;'):
                    ui.label(panel.name)


class TopPanel(MyModel):
    def setup(self):
        super().setup()
        with ui.card().style(
                f'background-color: {self.background_color}; height: {self.length}px; position: fixed; left: 0; top: 0; right: 0; border-radius: 0;'):
            pass


@ui.page('/')
def main_page():
    t1 = Tabs(name='first', img='...', url='...')
    t2 = Tabs(name='second', img='...', url='...')
    t3 = Tabs(name='third', img='...', url='...')
    p = Params(background_color='#30d5c8', active_tab_color='#30d5c8', length=100, tabs=[t1, t2, t3])
    manager = LeftPanel(p)
    manager.setup()

app.on_startup(main_page)
ui.run()
