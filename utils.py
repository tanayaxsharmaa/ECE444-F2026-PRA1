class utils:
    @staticmethod
    def reversed(number: int) -> int:
        """Return the digits of number in reverse order, keeping its sign."""
        sign = -1 if number < 0 else 1
        return sign * int(str(abs(number))[::-1])

    @staticmethod
    def formatter(number: int) -> tuple[str, str]:
        """Return number as (binary, octal) strings."""
        return format(number, "b"), format(number, "o")
