import logging

from linreg import create_data, model

from temples import main_runner


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main_runner(create_data.create_regression, model.train_linear_regression)()
