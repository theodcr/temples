import logging

from linreg import create_data

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    create_data.main()
