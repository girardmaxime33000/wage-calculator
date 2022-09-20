Les salaires disponibles sont des offres de Pole Emploi qui sont récupérés tous les jours. 
Ici tu as un historique depuis 6 mois à peu près, le fichier ne se met pas à jour tous les jours (comme il s'agit d'un test)

Remarques : 
- Il y a des erreurs dans les offres, on a mis des filtres mais il est possible que tu voies des valeurs un peu bizarres de temps en temps. 
Tu ne devrais pas voir de salaire en dessous du SMIC 
- NaN = pas de valeur 

Tu as ta disposition différents indicateurs pour les offres : 
- min salaire
- max salaire
- median salaire 
- moyenne salaire 
- écart-type salaire : (plus l'écart est grand plus on s'éloigne du salaire moyen, donc ça veut dire qu'il y a beaucoup de variances entre les salaires)
- Nombre d'offres avec un salaire
- Nombre d'offres sans salaire : ici tu peux estimer que pour certains jobs le salaire n'est jamais donné donc soit les entreprises ne veulent pas communiquer dessus soit elles ne savent pas du tout ou ce situer sur les salaires


A installer :
pip install streamlit 
pip install pandas 
pip install numpy 
pip install pysqlite3
