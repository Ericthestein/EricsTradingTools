from EricsTradingTools import EricsTradingTools
import time


if __name__ == "__main__":
    print("Initializing...")
    curr_time = time.time()
    main = EricsTradingTools()
    load_time = time.time() - curr_time
    print("Ready to go! (loaded in " + str(load_time) + " seconds)")
    main.main_loop()