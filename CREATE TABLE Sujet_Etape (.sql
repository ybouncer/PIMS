CREATE TABLE Sujet_Etape (
    idSujet_Etape INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    idSujet INT NOT NULL,
    idEtape INT NOT NULL,
    debut DATE NOT NULL,
    FOREIGN KEY (idSujet) REFERENCES Sujet(idSujet),
    FOREIGN KEY (idEtape) REFERENCES Etape(idEtape)
);

INSERT INTO Sujet_Etape (idSujet, idEtape, debut)
  VALUES (1,1,'2023-01-01'), 
  (2,2,'2024-01-01');


CREATE OR REPLACE VIEW vue_historique AS
SELECT 
    S.titre AS Titre_Sujet,
    SE.debut AS Start_Date,
    E.delai AS End_Date
FROM 
    Sujet S
JOIN 
    Sujet_Etape SE ON S.idSujet = SE.idSujet
JOIN 
    Etape E ON SE.idEtape = E.idEtape
;

SELECT * vue_historique; 
