def calcular_rendimento(valor_inicial, meses):
    taxa_admin = 0.005
    imposto = 0.225
    
    valor_liquido = valor_inicial
    for i in range(meses):
        juros = valor_liquido * 0.01
        valor_liquido += juros
        valor_liquido -= (valor_liquido * taxa_admin)
    
    lucro_bruto = valor_liquido - valor_inicial
    imposto_devido = lucro_bruto * imposto
    lucro_liquido = lucro_bruto - imposto_devido
    
    return lucro_liquido

if __name__ == "__main__":
    entrada = input("Valor inicial (ex: 1000): ")
    meses = int(input("Prazo em meses (ex: 12): "))
    
    resultado = calcular_rendimento(float(entrada), meses)
    print(f"Lucro líquido: {resultado:.2f}")