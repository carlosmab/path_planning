from space.space import Space
from ui.app import App


if __name__ == "__main__":
    
    space: Space = Space()
    app: App = App(space=space)
    
    app.mainloop()


