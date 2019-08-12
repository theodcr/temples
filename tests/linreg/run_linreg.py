import logging

from linreg import clean_data, create_raw_data, model
from temples import main_runner

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main_runner(
        create_raw_data.create_regression,
        clean_data.clean,
        model.train_linear_regression,
    )()
