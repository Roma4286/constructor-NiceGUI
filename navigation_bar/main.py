from nicegui import ui, app

from schemes_and_models import Params, Tabs, MyModel


class LeftPanel(MyModel):
    def main_page(self):
        super().main_page()

        with ui.card().style(
                f'background-color: {self.background_color}; width: {self.length}px; position: fixed; left: 0; top: 0; bottom: 0; border-radius: 0; display: flex; flex-direction: column; padding: 0; margin: 0; gap: 2px'):
            for panel in self.tabs:
                color = self.background_color
                if panel.is_active:
                    color = self.active_tab_color
                with ui.link(target=panel.url):
                    with ui.card().style(
                            f'background-color: {color}; width: {self.length}px; height: 40px; padding: 0; border-radius: 2px; box-shadow: none;'):
                        with ui.row().style('display: flex; align-items: center; position: absolute; top: 0; left: 4px; bottom: 0; right: 0;'):
                            ui.icon(panel.icon_name, color=panel.icon_color).classes('text-2xl')
                            ui.label(panel.name)


class TopPanel(MyModel):
    def main_page(self):
        super().main_page()
        with ui.card().style(
                f'background-color: {self.background_color}; height: {self.length}px; position: fixed; left: 0; top: 0; right: 0; border-radius: 0;'):
            pass


@ui.page('/')
def main_page():
    url = 'http://127.0.0.1:8080/'
    t1 = Tabs(name='first', icon_name='home', icon_color='#FFFFFF', is_active=False, url=url)
    t2 = Tabs(name='second', icon_name='ti-car', is_active=True, url=url)
    t3 = Tabs(name='third', icon_name='ti-window', icon_color='#990000', is_active=False, url=url)
    p = Params(background_color='#30d5c8', active_tab_color='#7FFFD4', length=130, tabs=[t1, t2, t3])
    manager = LeftPanel(p)
    manager.main_page()

app.on_startup(main_page)
ui.run()
