-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: localhost    Database: control_egresados
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student_module_estados`
--
USE control_egresados;
DROP TABLE IF EXISTS `student_module_estados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_module_estados` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `clave` varchar(25) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `abrev` varchar(25) DEFAULT NULL,
  `activo` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_module_estados`
--

LOCK TABLES `student_module_estados` WRITE;
/*!40000 ALTER TABLE `student_module_estados` DISABLE KEYS */;
INSERT INTO `student_module_estados` VALUES (1,'01','Aguascalientes','Ags.',1),(2,'02','Baja California','BC',1),(3,'03','Baja California Sur','BCS',1),(4,'04','Campeche','Camp.',1),(5,'05','Coahuila de Zaragoza','Coah.',1),(6,'06','Colima','Col.',1),(7,'07','Chiapas','Chis.',1),(8,'08','Chihuahua','Chih.',1),(9,'09','Ciudad de México','CDMX',1),(10,'10','Durango','Dgo.',1),(11,'11','Guanajuato','Gto.',1),(12,'12','Guerrero','Gro.',1),(13,'13','Hidalgo','Hgo.',1),(14,'14','Jalisco','Jal.',1),(15,'15','México','Mex.',1),(16,'16','Michoacán de Ocampo','Mich.',1),(17,'17','Morelos','Mor.',1),(18,'18','Nayarit','Nay.',1),(19,'19','Nuevo León','NL',1),(20,'20','Oaxaca','Oax.',1),(21,'21','Puebla','Pue.',1),(22,'22','Querétaro','Qro.',1),(23,'23','Quintana Roo','Q. Roo',1),(24,'24','San Luis Potosí','SLP',1),(25,'25','Sinaloa','Sin.',1),(26,'26','Sonora','Son.',1),(27,'27','Tabasco','Tab.',1),(28,'28','Tamaulipas','Tamps.',1),(29,'29','Tlaxcala','Tlax.',1),(30,'30','Veracruz de Ignacio de la Llave','Ver.',1),(31,'31','Yucatán','Yuc.',1),(32,'32','Zacatecas','Zac.',1);
/*!40000 ALTER TABLE `student_module_estados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-16  9:05:07
