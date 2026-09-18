""" Pipeline ETL - Fluxo de execução """

from setup_dw import configurar_dw
from extract_erp import extrair_erp
from extract_ibge import extrair_ibge
from extract_excel import extrair_excel
from silver import processar_silver
from gold import processar_gold

def main():
    # Garantindo existencia das camadas
    configurar_dw()

    # Extrair dados (E)
    extrair_erp()
    extrair_ibge()
    extrair_excel()

    # Transformar dados (T)
    processar_silver()

    # Carregar dados (L)
    processar_gold()

    print("Pipeline ETL concluído.")


if __name__ == "__main__":
    main()
