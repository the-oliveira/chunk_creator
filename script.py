import pandas as pd

# Definindo a função count_entries()
def count_entries(csv_file, c_size, colname):
    """Retorna um dicionário com contagens de
    ocorrências como valor para cada chave"""
    
    cont_dict = {}

    # Iterando sobre os chunks do arquivo
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterando em cada coluna no DataFrame 
        for entry in chunk[colname]:
            if entry in cont_dict.keys():
                cont_dict[entry] += 1
            else:
                cont_dict[entry] = 1

    # Retorna o dicionario após contar.
    return cont_dict

