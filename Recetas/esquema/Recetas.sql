-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Recetas
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Recetas` ;

-- -----------------------------------------------------
-- Schema Recetas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Recetas` DEFAULT CHARACTER SET utf8 ;
USE `Recetas` ;

-- -----------------------------------------------------
-- Table `Recetas`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Recetas`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `crear_en` DATETIME NULL DEFAULT now(),
  `actualizar_en` DATETIME NULL DEFAULT now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Recetas`.`Recetas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Recetas`.`Recetas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_receta` VARCHAR(45) NULL,
  `descripcion` VARCHAR(255) NULL,
  `instrucciones` VARCHAR(255) NULL,
  `fecha_creacion_receta` DATETIME NULL,
  `tiempo` TINYINT NULL,
  `creado_en` DATETIME NULL DEFAULT now(),
  `actualizado_en` DATETIME NULL DEFAULT now(),
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Recetas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_Recetas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `Recetas`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
