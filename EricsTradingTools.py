from StopLossCalculator import StopLossCalculator


class EricsTradingTools:
    def __init__(self):
        self.options = {
            "A": {
                "name": "Stop Loss Calculator",
                "description": "Suggests stop loss prices given maximum risk",
                "function": self.stop_loss_calculator
            }
        }
        self.stop_loss_calculator = StopLossCalculator()

    # Main Menu Handling Methods

    def main_loop(self):
        while True:
            self.show_main_menu()
            selection = self.get_selection()
            self.process_menu_selection(selection)

    def show_main_menu(self):
        print("-- Main Menu --")
        for option in self.options:
            option_data = self.options[option]
            self.show_option(option, option_data)

    @staticmethod
    def show_option(option, option_data):
        print(option + ": " + option_data["name"])
        print("- " + option_data["description"])

    @staticmethod
    def get_selection():
        return input("Selection: ")

    def process_menu_selection(self, selection):
        try:
            selected_option_data = self.options[selection.upper()]
            print("")
            print("-- " + selected_option_data["name"] + " --")
            selected_option_data["function"]()
        except KeyError:
            print("Invalid option")

    # Individual Functions

    def stop_loss_calculator(self):
        self.stop_loss_calculator.run()
        print("")