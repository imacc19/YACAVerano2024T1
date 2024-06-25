def obtener_fr(fa):

  fr = []
  for elemento in fa:
      
    fr.append(elemento / sum(fa)*100)
      
  return fr
