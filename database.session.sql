SELECT 
    Pe.annee AS Annee_Academique,
    C.nom AS Nom_Cours,
    S.titre AS Titre_Sujet,
    S.descriptif AS Description_Sujet,
    P1.nom || ' ' || P1.prenom AS Nom_Complet_Etudiant,
    P2.nom || ' ' || P2.prenom AS Nom_Complet_Professeur
FROM 
    Cours C
JOIN 
    Sujet S ON C.idCours = S.idCours
JOIN 
    Etudiant E ON S.idSujet = E.idSujet
JOIN 
    Personne P1 ON E.idPersonne = P1.idPersonne
JOIN 
    Professeur Pr ON S.idProf = Pr.idProf
JOIN 
    Personne P2 ON Pr.idPersonne = P2.idPersonne
JOIN  
    Periode Pe ON S.idPeriode = Pe.idPeriode
ORDER BY 
    Pe.annee, C.nom;
