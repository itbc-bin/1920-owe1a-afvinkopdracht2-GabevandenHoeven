
seq = "GGGGGGACTTAGCTCCAAAGCTGGCGCTTGGAAGTTAGGGACAGCGTCGCCGACTTGGTAGCCGCCGCAGCATTCGCCGCGGATAAAGCCGGGGTCTACCATACCCACTGATTAACTATGGAAGACTATACCAAAATAGAGAAAATTGGAGAAGGTACCTATGGAGTTGTGTATAAGGGTAGACACAAAACTACAGGCCAAGTGGTAGCCATGAAGAAAATCAGACTAGAAAGTGAAGAGGAAGGGGTTCCTAGTACTGCAATTCGGGAAATATCTCTATTAAAAGAGCTTCGTCATCCAAATATAGTCAGTCTTCAAGATGTGCTTATGCAGGATTCCAGGTTGTATCTCATCTTTGAATTCCTTTCCATGGATCTCAAGAAATACTTGGATTCTATCCCTCCTGGTCAGTTCATGGATTCTTCACTTGTTAAGAGTTATTTGTACCAAATCCTACAAGGGATTGTGTTTTGTCACTCTAGAAGAGTTCTCCACAGGGACTTAAAACCTCAAAATCTATTGATTGATGATAAAGGAACAATTAAGTTGGCAGATTTTGGCCTTGCCAGAGCTTTTGGAATTCCTATTAGAGTATATACACATGAGGTAGTGACACTCTGGTATAGATCTCCAGAAGTATTGCTGGGGTCAGCTGGCTACTCAACTCCAGTGGACATTTGGAGTATAGGTACCATATTTGCTGAATTAGCAACGAAGAAACCACTTTTTCATGGGGATTCAGAAATTGATCAACTCTTCAGAATTTTCAGAGCTTTGGGCACTCCCAATAATGAAGTGTGGCCAGAAGTGGAATCTTTACAGGACTATAAGAGTACATTTCCCAAGTGGAAACCAGGAAGCTTAGCATCCCATGTCAAAAACTTGGATGAAAATGGCTTGGATCTGCTCTCGAAAATGTTAATCTATGATCCTGCCAAACGAATTTCTGGCAAAATGGCACTGAATCATCCGTACTTTAATGATTTGGACAGTCAAATTAAGAAGATGTAGCTTTCTGACAGTTTCCCTGTGTTGTGTCAAGAGCAGATAATTGTACTTTTACTGTTCATCTCTGGTTTTGTCTTGTATATTTTTCTTTTCTTTGTTGTAAAACTTAATCTGTACTTCATCTTCTGATTTCAAAACTAAGTTAAAATGTAAATACTGTTCTATATGAATTTAAATATAATAATTCTGTATATGTTTGTAGATTCCACTGTAACAGCTGTTTGTTACTATAATAAAACTTTATAAATCT"

# De mRNA sequenties worden er als string variabelen in het script gezet.
# Hier moeten wel alle enters en whitespaces uit worden gehaald.

aantal_a = seq.count("A")
aantal_t = seq.count("T")
aantal_c = seq.count("C")
aantal_g = seq.count("G")

# Nu worden er vier variabelen aangemaakt.
# Elk variabel telt het aantal van een van de vier letters die voorkomen in de sequentie.

sequentie = aantal_a + aantal_t + aantal_c + aantal_g

# De totale lengte van de sequentie wordt berekend door alle vier de variabelen die de letters tellen,
# bij elkaar op te tellen

print( sequentie )

# Nu wordt eerst de totale lengte van de sequentie geprint

aantal_gc = aantal_g + aantal_c

gcpercentage = aantal_gc / sequentie * 100

print( gcpercentage )

# Het gc% wordt berekend door eerst het aantal g en het aantal c bij elkaar op te tellen.
# Dan wordt het percentage berekend: deel gedeeld door geheel keer 100%
#  Het gc% wordt geprint
