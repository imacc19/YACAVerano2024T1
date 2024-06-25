import pandas as pd

def imptabla(clases_sorted, fa_sorted, fr_relativa, fr_acum):

    # Create the DataFrame with column headers
    data = {'Clases': clases_sorted,
            'F absoluta': fa_sorted,
            'F relativa': fr_relativa,
            'F acumulada': fr_acum}
    
    df = pd.DataFrame(data)
    return df
    