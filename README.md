System Design: https://go.gliffy.com/go/publish/12885630
UI Design: https://app.moqups.com/OwenT/N07oYnmbfb/view/page/ad64222d5

Database Schema:

CREATE TABLE `Location` (  
  `ID` INT NOT NULL,  
  `Country` INT NOT NULL,  
  `Name` VARCHAR(255) NOT NULL,  
  `Lon` DECIMAL NOT NULL,  
  `Lat` DECIMAL NOT NULL,  
  PRIMARY KEY (`ID`)  
);  

CREATE TABLE `WeatherRecord` (  
  `ID` INT NOT NULL AUTO_INCREMENT,  
  `Date` DATE NOT NULL,  
  `Location` INT NOT NULL,  
  `Temp` FLOAT NOT NULL,  
  PRIMARY KEY (`ID`)  

  More fields depending on API....  

);  

CREATE TABLE `Countries` (  
  `Id` INT NOT NULL AUTO_INCREMENT,  
  `Name` VARCHAR(255) NOT NULL,  
  PRIMARY KEY (`Id`)  
);  
