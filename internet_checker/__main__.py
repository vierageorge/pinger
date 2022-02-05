from internet_checker import app
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(name)s - %(message)s')
    app.run()