from datetime import datetime, timedelta

from cryptogainanalyzer.constants import DOLAR_VALUE_IN_BRL


class FileManager:

    def __init__(self, file_content: str):
        self.currencies_to_consult = self.parse_content(file_content)

    @classmethod
    def parse_content(cls, file_content: str):
        lines = file_content.split("\n")
        result = []

        for line in lines:
            investment, currency, time_str = line.split(" ")
            result.append(
                {
                    "currency": currency,
                    "time": cls.parse_time(time_str),
                    "investment": float(investment) * DOLAR_VALUE_IN_BRL,
                }
            )

        return result

    @classmethod
    def parse_time(cls, time_content: str):
        """
        Convert time of Brazil to UTC
        Return string text in ISO 8601 format
        """
        time_format = "%H:%M-%d/%m/%Y"
        time_obj = datetime.strptime(time_content, time_format) - timedelta(hours=3)
        return time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
