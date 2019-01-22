-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customers` (
  `idCustomers` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `phone` INT NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `ZIP` INT NULL,
  PRIMARY KEY (`idCustomers`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoices` (
  `idInvoices` INT NOT NULL,
  `date` VARCHAR(45) NULL,
  `car` VARCHAR(45) NULL,
  `customer` VARCHAR(45) NULL,
  `salesperson` VARCHAR(45) NULL,
  `Customers_idCustomers` INT NOT NULL,
  PRIMARY KEY (`idInvoices`, `Customers_idCustomers`),
  INDEX `fk_Invoices_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `mydb`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cars` (
  `VIN` INT NOT NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` INT NULL,
  `Color` VARCHAR(45) NULL,
  `Invoices_idInvoices` INT NOT NULL,
  PRIMARY KEY (`VIN`, `Invoices_idInvoices`),
  INDEX `fk_Cars_Invoices1_idx` (`Invoices_idInvoices` ASC) VISIBLE,
  CONSTRAINT `fk_Cars_Invoices1`
    FOREIGN KEY (`Invoices_idInvoices`)
    REFERENCES `mydb`.`Invoices` (`idInvoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Salespersons` (
  `idSalespersons` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  PRIMARY KEY (`idSalespersons`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cars_have_Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cars_have_Salespersons` (
  `CarshaveSalespersons_id` INT NOT NULL,
  `Cars_VIN` INT NOT NULL,
  `Salespersons_idSalespersons` INT NOT NULL,
  PRIMARY KEY (`CarshaveSalespersons_id`, `Cars_VIN`, `Salespersons_idSalespersons`),
  INDEX `fk_table1_Cars_idx` (`Cars_VIN` ASC) VISIBLE,
  INDEX `fk_table1_Salespersons1_idx` (`Salespersons_idSalespersons` ASC) VISIBLE,
  CONSTRAINT `fk_table1_Cars`
    FOREIGN KEY (`Cars_VIN`)
    REFERENCES `mydb`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_table1_Salespersons1`
    FOREIGN KEY (`Salespersons_idSalespersons`)
    REFERENCES `mydb`.`Salespersons` (`idSalespersons`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customers_have_salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customers_have_salespersons` (
  `idCustomers_have_salespersons` INT NOT NULL,
  `Salespersons_idSalespersons` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  PRIMARY KEY (`idCustomers_have_salespersons`, `Salespersons_idSalespersons`, `Customers_idCustomers`),
  INDEX `fk_Customers_have_salespersons_Salespersons1_idx` (`Salespersons_idSalespersons` ASC) VISIBLE,
  INDEX `fk_Customers_have_salespersons_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_have_salespersons_Salespersons1`
    FOREIGN KEY (`Salespersons_idSalespersons`)
    REFERENCES `mydb`.`Salespersons` (`idSalespersons`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_have_salespersons_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `mydb`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customers_have_cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customers_have_cars` (
  `idCustomers_have_cars` INT NOT NULL,
  `Cars_VIN` INT NOT NULL,
  `Cars_Invoices_idInvoices` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  PRIMARY KEY (`idCustomers_have_cars`, `Cars_VIN`, `Cars_Invoices_idInvoices`, `Customers_idCustomers`),
  INDEX `fk_Customers_have_cars_Cars1_idx` (`Cars_VIN` ASC, `Cars_Invoices_idInvoices` ASC) VISIBLE,
  INDEX `fk_Customers_have_cars_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_have_cars_Cars1`
    FOREIGN KEY (`Cars_VIN`)
    REFERENCES `mydb`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_have_cars_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `mydb`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
