from dataModel import DataModel
from gui import Gui
from controller import Controller


def main():
    data = DataModel()
    main_controller = Controller(data)
    main_gui = Gui(800, 800, main_controller)
    data.set_view(main_gui)
    main_gui.start()


if __name__ == "__main__":
    main()
