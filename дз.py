CREATE DATABASE AnimalKingdom;

USE AnimalKingdom;

CREATE TABLE Animals
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Назва_звіра VARCHAR(50),
    Тип_звіра VARCHAR(50)

INSERT INTO Animals (Назва_звіра, Тип_звіра) VALUES
('Лев', 'Ссавець'),
('Крокодил', 'Плазун'),
('Орел', 'Птах'),
('Морська черепаха', 'Плазун'),
('Мавпа', 'Ссавець');

UPDATE Animals
SET Назва_звіра = 'Сокіл'
WHERE Назва_звіра = 'Орел';

SELECT * FROM Animals
WHERE Тип_звіра = 'Ссавець';

SELECT * FROM Animals;






















