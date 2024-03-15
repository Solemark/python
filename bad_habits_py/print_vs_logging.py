import logging


def bad_print_vs_logging():
    print("debug info")
    print("just some info")
    print("horrific error!")


def proper_print_vs_logging() -> None:
    logging.debug("debug info")
    logging.info("just some info")
    logging.error("yet another horrific error!")


def main():
    level = logging.DEBUG
    fmt = "[%(levelname)s] %(asctime)s - %(message)s"
    logging.basicConfig(level=level, format=fmt)
