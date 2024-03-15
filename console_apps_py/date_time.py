from datetime import datetime


def get_current_time() -> str:
    CURRENT_TIME = datetime.now()
    return (
        f"The date is: {CURRENT_TIME.strftime('%A')} "
        f"the {format_date(CURRENT_TIME.day)} "
        f"of { CURRENT_TIME.strftime('%B')} "
        f"{CURRENT_TIME.year}"
    )


def format_date(day: int) -> str:
    output: str = ""
    match day:
        case 1 | 21 | 31:
            output = f"{day}st"
        case 2 | 22:
            output = f"{day}nd"
        case 3 | 23:
            output = f"{day}rd"
        case _:
            output = f"{day}th"
    return output
