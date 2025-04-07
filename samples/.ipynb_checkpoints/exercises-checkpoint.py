# Una función que cuente las vocales de una cadena

contar_vocales = lambda cadena: sum(1 for c in cadena.lower() if c in 'aeiou')

# Una función que obtenga el enésimo número más grande de una lista

enesimo_mas_grande = lambda lista, n: sorted(lista, reverse=True)[n-1] if n <= len(sorted(lista, reverse=True)) else None
    
# Una función que encuentra la palabra más larga de una cadena

palabra_mas_larga = lambda cadena: max(cadena.split(), key=len) if cadena.split() else None


