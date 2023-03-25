CREATE TABLE `crocosoftcr`.`customer` (
  `Customer_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(50) NOT NULL,
  `Phone_Number` INT(11) NOT NULL,
  `Address` VARCHAR(225) NOT NULL,
  PRIMARY KEY (`Customer_ID`));
  
  CREATE TABLE `crocosoftcr`.`vehicle` (
  `Vehicle_ID` INT NOT NULL AUTO_INCREMENT,
  `Vehicle_Type` VARCHAR(50) NOT NULL,
  `Availability` TINYINT NOT NULL,
  PRIMARY KEY (`Vehicle_ID`));
  
  CREATE TABLE `crocosoftcr`.`booking` (
  `Booking_ID` INT NOT NULL AUTO_INCREMENT,
  `Customer_ID` INT NOT NULL,
  `Vehicle_ID` INT NOT NULL,
  `Hire_Date` DATE NOT NULL,
  `Return_Date` DATE NOT NULL,
  PRIMARY KEY (`Booking_ID`),
  CONSTRAINT `Customer_ID`
    FOREIGN KEY (`Customer_ID`)
    REFERENCES `crocosoftcr`.`customer` (`Customer_ID`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `Vehicle_ID`
    FOREIGN KEY (`Vehicle_ID`)
    REFERENCES `crocosoftcr`.`vehicle` (`Vehicle_ID`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
CONSTRAINT chk_Booking_Date
      CHECK (DATEDIFF(Return_Date, Hire_Date) <= 7)
);
DROP TRIGGER IF EXISTS `crocosoftcr`.`check_booking_availability`;

DELIMITER $$
USE `crocosoftcr`$$
CREATE DEFINER = CURRENT_USER TRIGGER `crocosoftcr`.`check_booking_availability` BEFORE INSERT ON `Booking` FOR EACH ROW
BEGIN
	DECLARE availability BOOLEAN;

    SELECT Availability INTO availability
    FROM Vehicle
    WHERE Vehicle_ID = NEW.Vehicle_ID;

    IF availability = FALSE THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Vehicle not available on selected dates';
    ELSEIF NEW.Hire_Date < CURDATE() THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Hire date cannot be in the past';
    ELSEIF DATEDIFF(NEW.Return_Date, NEW.Hire_Date) > 7 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Booking cannot be longer than a week';
    END IF;
END$$
DELIMITER ;