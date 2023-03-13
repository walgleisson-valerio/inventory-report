from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        products = []

        if (path.endswith(".csv")):
            products = Inventory.csv_reader(path)

        elif (path.endswith(".json")):
            products = Inventory.json_reader(path)

        elif (path.endswith(".xml")):
            products = Inventory.xml_reader(path)

        return Inventory.generate_report_by_type(products, report_type)

    @staticmethod
    def csv_reader(path):
        with open(path, "r") as file:
            return [row for row in csv.DictReader(file)]

    @staticmethod
    def json_reader(path):
        with open(path, "r") as file:
            return json.loads(file.read())

    @staticmethod
    def xml_reader(path):
        with open(path, "r") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @staticmethod
    def generate_report_by_type(products, report_type):
        if report_type == "simples":
            return SimpleReport.generate(products)
        else:
            return CompleteReport.generate(products)
