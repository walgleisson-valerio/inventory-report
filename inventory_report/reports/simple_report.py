from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        companies = []
        manufacturing_dates = []
        expiration_dates = []

        for product in list:
            companies.append(product["nome_da_empresa"])
            most_common_company = Counter(companies).most_common()[0][0]
            manufacturing_dates.append(product["data_de_fabricacao"])

            expiration_date = product["data_de_validade"]
            date_format = datetime.strptime(expiration_date, "%Y-%m-%d")
            if datetime.now() < date_format:
                expiration_dates.append(product["data_de_validade"])

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_dates)}\n"
            f"Data de validade mais próxima: {min(expiration_dates)}\n"
            f"Empresa com mais produtos: {most_common_company}"
        )
