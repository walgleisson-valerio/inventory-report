from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        companies = []
        for product in list:
            companies.append(product["nome_da_empresa"])

        companies_stock = Counter(companies)
        report = ""
        for company in companies_stock:
            report += f"- {company}: {companies_stock[company]}\n"

        return (
            f"{SimpleReport.generate(list)}\n"
            f"Produtos estocados por empresa:\n"
            f"{report}"
        )
