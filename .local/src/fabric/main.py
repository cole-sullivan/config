from imports import *
from widgets.bar import StatusBar
from widgets.island import Island

if __name__ == "__main__":
    bar = StatusBar()
    island = Island()
    bar.island = island
    app = Application("bar", bar)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))

    app.run()
