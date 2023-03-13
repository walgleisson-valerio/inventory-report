from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        products = []

        if (path.endswith(".csv")):
            products = CsvImporter.import_data(path)

        elif (path.endswith(".json")):
            products = JsonImporter.import_data(path)

        elif (path.endswith(".xml")):
            products = XmlImporter.import_data(path)

        return Inventory.generate_report_by_type(products, report_type)

    @staticmethod
    def generate_report_by_type(products, report_type):
        if report_type == "simples":
            return SimpleReport.generate(products)
        else:
            return CompleteReport.generate(products)
