from controller import Controller
from interface import Interface

if __name__ == "__main__":
    app = Controller(Interface())
    app.start()