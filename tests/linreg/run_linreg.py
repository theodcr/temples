import logging

from linreg import create_data, model

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    create_data.create_regression()
    model.train_linear_regression()
