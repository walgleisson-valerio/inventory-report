from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if (path.endswith(".csv")):
            with open(path, "r") as file:
                return [row for row in csv.DictReader(file)]
        raise ValueError("Arquivo inválido")
