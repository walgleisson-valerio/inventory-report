from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Product 01",
        nome_da_empresa="Empresa 01",
        data_de_fabricacao="2023-03-13",
        data_de_validade="2024-03-13",
        numero_de_serie="12345678",
        instrucoes_de_armazenamento="Cuidado ao armazenar"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Product 01"
    assert product.nome_da_empresa == "Empresa 01"
    assert product.data_de_fabricacao == "2023-03-13"
    assert product.data_de_validade == "2024-03-13"
    assert product.numero_de_serie == "12345678"
    assert product.instrucoes_de_armazenamento == "Cuidado ao armazenar"
