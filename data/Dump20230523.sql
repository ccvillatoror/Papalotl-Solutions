-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: micheladasatucasa
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.2

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
-- Table structure for table `agrega`
--

DROP TABLE IF EXISTS `agrega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agrega` (
  `id_usuario` int NOT NULL,
  `id_producto` int NOT NULL,
  `fecha` date DEFAULT NULL,
  `cantidad` int NOT NULL,
  KEY `id_usuario` (`id_usuario`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `agrega_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`idUsuario`),
  CONSTRAINT `agrega_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`idProducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agrega`
--

LOCK TABLES `agrega` WRITE;
/*!40000 ALTER TABLE `agrega` DISABLE KEYS */;
/*!40000 ALTER TABLE `agrega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atiende`
--

DROP TABLE IF EXISTS `atiende`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atiende` (
  `id_pedido` int NOT NULL,
  `id_usuario` int NOT NULL,
  KEY `id_pedido` (`id_pedido`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `atiende_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`idPedido`),
  CONSTRAINT `atiende_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atiende`
--

LOCK TABLES `atiende` WRITE;
/*!40000 ALTER TABLE `atiende` DISABLE KEYS */;
/*!40000 ALTER TABLE `atiende` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conforma`
--

DROP TABLE IF EXISTS `conforma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conforma` (
  `id_pedido` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` varchar(45) NOT NULL,
  KEY `id_pedido` (`id_pedido`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `conforma_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`idPedido`),
  CONSTRAINT `conforma_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`idProducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conforma`
--

LOCK TABLES `conforma` WRITE;
/*!40000 ALTER TABLE `conforma` DISABLE KEYS */;
/*!40000 ALTER TABLE `conforma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consume`
--

DROP TABLE IF EXISTS `consume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consume` (
  `id_producto` int NOT NULL,
  `id_insumo` int NOT NULL,
  KEY `id_producto` (`id_producto`),
  KEY `id_insumo` (`id_insumo`),
  CONSTRAINT `consume_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`idProducto`),
  CONSTRAINT `consume_ibfk_2` FOREIGN KEY (`id_insumo`) REFERENCES `insumo` (`idInsumo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consume`
--

LOCK TABLES `consume` WRITE;
/*!40000 ALTER TABLE `consume` DISABLE KEYS */;
/*!40000 ALTER TABLE `consume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insumo`
--

DROP TABLE IF EXISTS `insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insumo` (
  `idInsumo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) DEFAULT NULL,
  `cantidad` int NOT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`idInsumo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insumo`
--

LOCK TABLES `insumo` WRITE;
/*!40000 ALTER TABLE `insumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordena`
--

DROP TABLE IF EXISTS `ordena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordena` (
  `id_pedido` int NOT NULL,
  `id_usuario` int NOT NULL,
  KEY `id_pedido` (`id_pedido`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `ordena_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`idPedido`),
  CONSTRAINT `ordena_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordena`
--

LOCK TABLES `ordena` WRITE;
/*!40000 ALTER TABLE `ordena` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `idPedido` int NOT NULL AUTO_INCREMENT,
  `total` decimal(6,2) NOT NULL DEFAULT '9999.99',
  `estatus` tinyint(1) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`idPedido`)
) ENGINE=InnoDB AUTO_INCREMENT=203 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
INSERT INTO `pedido` VALUES (3,430.76,0,'2021-05-26'),(4,225.41,0,'2021-12-07'),(5,717.77,0,'2022-04-02'),(6,937.88,0,'2021-05-19'),(7,346.15,0,'2022-01-22'),(8,828.50,0,'2021-10-03'),(9,242.96,0,'2021-12-07'),(10,125.91,0,'2022-07-28'),(11,358.31,0,'2021-05-17'),(12,311.36,0,'2023-02-06'),(13,312.63,0,'2021-09-24'),(14,106.72,0,'2022-09-12'),(15,127.70,0,'2022-11-01'),(16,675.33,0,'2021-10-14'),(17,396.57,0,'2021-11-11'),(18,743.90,0,'2021-08-25'),(19,970.66,0,'2023-02-10'),(20,187.82,0,'2022-03-15'),(21,462.94,0,'2021-08-31'),(22,997.46,0,'2023-01-20'),(23,124.57,0,'2021-10-16'),(24,870.65,0,'2023-01-14'),(25,504.33,0,'2023-03-16'),(26,142.04,0,'2022-07-21'),(27,713.15,0,'2022-03-28'),(28,83.97,0,'2022-10-17'),(29,466.13,0,'2021-10-26'),(30,303.97,0,'2022-07-16'),(31,556.41,0,'2022-09-15'),(32,778.76,0,'2022-09-30'),(33,716.15,0,'2021-08-05'),(34,398.93,0,'2021-10-22'),(35,942.26,0,'2023-03-03'),(36,643.71,0,'2022-07-06'),(37,179.60,0,'2023-03-12'),(38,233.35,0,'2021-12-30'),(39,422.12,0,'2022-11-23'),(40,323.18,0,'2023-02-08'),(41,510.01,0,'2022-05-24'),(42,209.04,0,'2022-11-30'),(43,373.36,0,'2022-10-06'),(44,632.20,0,'2022-08-11'),(45,204.60,0,'2021-07-17'),(46,669.89,0,'2021-08-15'),(47,618.65,0,'2023-01-12'),(48,121.24,0,'2021-09-17'),(49,433.05,0,'2022-08-19'),(50,913.56,0,'2021-08-27'),(51,601.80,0,'2023-03-28'),(52,930.39,0,'2021-05-18'),(53,598.15,0,'2022-06-16'),(54,569.47,0,'2023-02-13'),(55,575.63,0,'2021-11-13'),(56,865.91,0,'2022-04-15'),(57,127.13,0,'2022-05-03'),(58,421.79,0,'2021-06-26'),(59,877.56,0,'2023-04-08'),(60,570.66,0,'2023-03-13'),(61,141.26,0,'2021-06-20'),(62,135.46,0,'2023-02-19'),(63,197.26,0,'2021-05-30'),(64,882.96,0,'2022-10-27'),(65,567.39,0,'2022-06-19'),(66,990.94,0,'2023-02-05'),(67,128.40,0,'2022-10-10'),(68,832.96,0,'2021-11-11'),(69,564.49,0,'2021-06-25'),(70,163.88,0,'2023-03-15'),(71,830.82,0,'2021-06-03'),(72,943.81,0,'2022-04-18'),(73,764.20,0,'2022-05-07'),(74,492.50,0,'2021-11-23'),(75,346.04,0,'2022-10-12'),(76,976.59,0,'2021-11-16'),(77,508.42,0,'2023-01-14'),(78,656.49,0,'2023-03-20'),(79,863.08,0,'2022-09-22'),(80,986.56,0,'2022-03-04'),(81,300.26,0,'2021-12-18'),(82,90.89,0,'2022-01-15'),(83,259.26,0,'2021-08-05'),(84,789.67,0,'2022-02-14'),(85,446.36,0,'2022-02-25'),(86,914.15,0,'2022-07-07'),(87,548.82,0,'2022-12-17'),(88,503.01,0,'2022-11-09'),(89,967.07,0,'2021-06-25'),(90,118.14,0,'2022-03-08'),(91,725.00,0,'2022-08-23'),(92,163.52,0,'2021-06-14'),(93,484.40,0,'2022-05-02'),(94,592.28,0,'2022-03-29'),(95,453.70,0,'2022-12-24'),(96,449.93,0,'2022-09-03'),(97,813.74,0,'2023-03-13'),(98,626.21,0,'2022-04-08'),(99,175.31,0,'2022-11-26'),(100,996.26,0,'2021-12-15'),(101,884.78,0,'2022-04-05'),(102,739.14,0,'2022-12-13'),(103,119.10,0,'2023-04-09'),(104,143.75,0,'2022-06-15'),(105,660.45,0,'2021-12-31'),(106,669.95,0,'2021-05-15'),(107,517.23,0,'2022-09-27'),(108,876.99,0,'2021-12-21'),(109,301.67,0,'2023-02-03'),(110,792.79,0,'2022-10-31'),(111,822.67,0,'2022-11-30'),(112,287.73,0,'2021-08-08'),(113,812.29,0,'2023-01-25'),(114,403.27,0,'2023-05-06'),(115,621.89,0,'2022-09-09'),(116,128.97,0,'2021-05-15'),(117,905.55,0,'2021-12-08'),(118,639.05,0,'2023-04-21'),(119,262.51,0,'2022-03-12'),(120,513.35,0,'2023-04-04'),(121,125.05,0,'2022-04-29'),(122,313.01,0,'2021-07-24'),(123,674.03,0,'2023-05-03'),(124,687.97,0,'2022-05-01'),(125,370.73,0,'2022-06-08'),(126,895.85,0,'2023-05-08'),(127,814.26,0,'2022-05-13'),(128,990.83,0,'2022-03-26'),(129,194.34,0,'2021-07-28'),(130,475.84,0,'2022-04-23'),(131,691.23,0,'2022-04-11'),(132,712.28,0,'2023-01-31'),(133,250.59,0,'2022-05-09'),(134,281.47,0,'2021-07-07'),(135,744.17,0,'2021-06-09'),(136,479.40,0,'2021-12-30'),(137,718.73,0,'2023-01-24'),(138,902.32,0,'2021-07-02'),(139,693.24,0,'2022-05-10'),(140,556.93,0,'2022-09-18'),(141,87.10,0,'2023-04-24'),(142,93.58,0,'2022-02-16'),(143,125.41,0,'2023-04-06'),(144,647.36,0,'2022-01-26'),(145,382.16,0,'2021-05-26'),(146,403.92,0,'2023-05-09'),(147,750.41,0,'2022-08-31'),(148,579.75,0,'2022-02-13'),(149,313.79,0,'2023-02-28'),(150,178.96,0,'2022-06-08'),(151,882.98,0,'2021-11-26'),(152,381.72,0,'2022-10-24'),(153,269.53,0,'2022-07-17'),(154,596.31,0,'2022-11-24'),(155,678.76,0,'2023-02-01'),(156,919.25,0,'2022-09-11'),(157,690.64,0,'2022-02-08'),(158,91.85,0,'2023-04-24'),(159,749.84,0,'2021-08-24'),(160,983.95,0,'2022-06-20'),(161,499.17,0,'2022-11-26'),(162,619.31,0,'2022-07-08'),(163,478.45,0,'2022-09-17'),(164,469.29,0,'2022-12-15'),(165,282.56,0,'2022-03-18'),(166,168.65,0,'2021-11-17'),(167,355.27,0,'2022-07-28'),(168,737.70,0,'2022-06-30'),(169,500.30,0,'2022-03-07'),(170,837.46,0,'2021-09-08'),(171,954.70,0,'2022-11-13'),(172,106.35,0,'2022-01-27'),(173,164.37,0,'2021-07-21'),(174,533.97,0,'2021-11-13'),(175,631.55,0,'2021-12-03'),(176,295.87,0,'2021-12-17'),(177,495.29,0,'2021-06-11'),(178,974.87,0,'2022-12-21'),(179,885.35,0,'2021-08-10'),(180,336.60,0,'2021-12-25'),(181,479.26,0,'2023-01-21'),(182,717.94,0,'2021-05-24'),(183,108.20,0,'2021-12-08'),(184,330.94,0,'2022-05-31'),(185,461.87,0,'2023-01-21'),(186,369.51,0,'2022-09-30'),(187,391.56,0,'2022-09-23'),(188,439.14,0,'2021-11-03'),(189,211.24,0,'2023-02-07'),(190,133.44,0,'2022-08-18'),(191,962.60,0,'2022-11-13'),(192,246.29,0,'2023-03-08'),(193,634.28,1,'2021-07-11'),(194,982.81,1,'2022-12-20'),(195,119.39,1,'2022-05-26'),(196,653.68,1,'2022-12-04'),(197,807.23,1,'2021-09-24'),(198,737.02,1,'2023-03-22'),(199,336.42,1,'2021-11-15'),(200,182.06,1,'2022-12-24'),(201,204.86,1,'2021-08-14'),(202,317.76,1,'2022-10-05');
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `idProducto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `precio` decimal(6,2) NOT NULL DEFAULT '9999.99',
  `cantidadInventario` int NOT NULL,
  PRIMARY KEY (`idProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Michelada natural','Cerveza, jugo de limón, picante y sal, y agregando salsas sazonadoras.',80.00,5),(2,'Gomichelada','Michelada con panditas rojos dentro.',90.00,2),(3,'Licuachela','Micheladas que se sirven en vasos de licuadoras con diversos toppings.',200.00,2),(4,'Michelada de mango','Michelada con pulpa de mango y chile.',80.00,4),(5,'Botana surtida','Paquete con botanas de distintos tipos.',50.00,20),(6,'producto 32','djlwksnl',99.99,3);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registra`
--

DROP TABLE IF EXISTS `registra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registra` (
  `id_insumo` int NOT NULL,
  `id_usuario` int NOT NULL,
  KEY `id_usuario` (`id_usuario`),
  KEY `id_insumo` (`id_insumo`),
  CONSTRAINT `registra_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`idUsuario`),
  CONSTRAINT `registra_ibfk_2` FOREIGN KEY (`id_insumo`) REFERENCES `insumo` (`idInsumo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registra`
--

LOCK TABLES `registra` WRITE;
/*!40000 ALTER TABLE `registra` DISABLE KEYS */;
/*!40000 ALTER TABLE `registra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(20) DEFAULT NULL,
  `apellidoPaterno` varchar(15) DEFAULT NULL,
  `apellidoMaterno` varchar(15) DEFAULT NULL,
  `correo` varchar(30) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `contrasena` varchar(25) DEFAULT NULL,
  `calle` varchar(20) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `cp` int DEFAULT NULL,
  `colonia` varchar(20) DEFAULT NULL,
  `ciudad` varchar(25) DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `tipoUsuario` varchar(15) NOT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Alberto','Reyes','Gutierrez','alberto.r@ciencias.unam.mx','1999-10-21','1234','Aztecas',1,21210,'Ajusco','Coyoazán','CDMX','cliente'),(2,'Cecilia','Villatoro','Ramos','cc@ciencias.unam.mx','2000-02-10','1234','jndsjn',2,52560,'ksjdsn','kqjsnlk','ksjnwlkn','cliente'),(3,'Laureen','Lillford','Gatus','lgatus0@skyrock.com','1950-07-05','9699961161','Iowa',2808,55555,'Ryan','San Isidro','Mexico','cliente'),(4,'Mozelle','Woolaston','Benadette','mbenadette0@diigo.com','1954-04-14','6921428372','Graedel',89,3696,'Westridge','San Sebastian','Mexico','cliente'),(6,'Ulises','Tunder','Bowlands','ubowlands0@fema.gov','1963-11-21','146387634','Heath',3,80778,'Artisan','Santa Cruz','Mexico','cliente'),(7,'Angy','Marron','Spillman','aspillman2@boston.com','1957-03-22','532765599','Bay',83,94732,'Macpherson','El Potrero','Mexico','cliente'),(8,'Sherwin','McQuode','Haggidon','shaggidon3@tiny.cc','1984-02-29','9269820782','Montana',72,18900,'Helena','Santiago','Mexico','cliente'),(9,'Osbourn','Delany','Garwood','ogarwood4@vkontakte.ru','1967-08-08','2754914400','Forest Dale',8864,30987,'Harper','Buenavista','Mexico','cliente'),(10,'Rustie','Lovekin','Abramin','rabramin5@shop-pro.jp','1960-09-01','929771813','Fallview',86,42952,'Myrtle','El Capulin','Mexico','cliente'),(11,'Genia','McAuslan','Dreini','gdreini6@prnewswire.com','1955-05-19','2066417256','Merry',409,87281,'Bultman','Santa Clara','Mexico','cliente'),(12,'Trent','Springell','Moscrop','tmoscrop7@sohu.com','1971-03-01','2036296923','Little Fleur',41,75986,'Oakridge','Santa Cruz','Mexico','cliente'),(13,'Dorella','Stampfer','Merrigans','dmerrigans8@mac.com','1960-05-26','9847296369','Westerfield',1,64813,'Mariners Cove','Morelos','Mexico','cliente'),(14,'Eartha','Mc Ilwrick','Coolican','ecoolican9@naver.com','1970-03-21','5806593213','Northfield',93,52878,'Prairieview','San Martin','Mexico','cliente'),(15,'Gerrie','Brislan','Fonzone','gfonzonea@nba.com','1979-08-06','7927959375','Loftsgordon',7,74140,'Forest Run','Emiliano Zapata','Mexico','cliente'),(16,'Farlee','Rewcassell','Guillet','fguilletb@reference.com','1983-12-14','3255463771','Heath',56,4525,'Cherokee','Santo Tomas','Mexico','cliente'),(17,'Margery','Janek','Jeremaes','mjeremaesc@nhs.uk','1952-05-09','8808108854','Dapin',5,14681,'American Ash','Buenavista','Mexico','cliente'),(18,'Fernanda','Andrus','Polley','fpolleyd@globo.com','1953-02-08','6619538458','Pine View',9,70250,'Ridgeview','Emiliano Zapata','Mexico','cliente'),(19,'Cahra','Powton','Yude','cyudee@photobucket.com','1994-10-08','4569466795','5th',645,63544,'Atwood','Santa Maria','Mexico','cliente'),(20,'Jeannette','Renneke','Bache','jbachef@slideshare.net','1989-01-11','1444716530','Nancy',96,45652,'Fulton','San Miguel','Mexico','cliente'),(21,'Breena','Leake','Lanyon','blanyong@bandcamp.com','1998-11-19','9146875876','Gateway',1876,93669,'Warbler','San Martin','Mexico','cliente'),(22,'Rosemonde','Livermore','Moohan','rmoohanh@flavors.me','1961-02-08','4026195950','3rd',42871,37651,'Russell','La Mesa','Mexico','cliente'),(23,'Shermie','Quilkin','Andres','sandresi@forbes.com','1954-10-06','6347027273','Mallory',22,46494,'Park Meadow','Santa Maria','Mexico','cliente'),(24,'Rosemonde','Bezley','Curman','rcurmanj@nifty.com','1969-10-09','2146244325','Logan',19,61607,'4th','La Virgen','Mexico','cliente'),(25,'Ethelred','Dixcey','Ballefant','eballefantk@huffingtonpost.com','1987-06-04','236136555','Graceland',339,4245,'Mayfield','La Palma','Mexico','cliente'),(26,'Janeta','Brash','Geroldini','jgeroldinil@unc.edu','1984-04-19','340786380','Gulseth',20,57175,'Transport','Santiago','Mexico','cliente'),(27,'Audry','Kemmis','Levinge','alevingem@skyrock.com','1997-01-30','4622864140','Mosinee',1,29434,'Springview','Emiliano Zapata','Mexico','cliente'),(28,'Ilise','Ahern','Eteen','ieteenn@wikia.com','1984-08-01','7468005650','Corscot',985,23108,'Surrey','Morelos','Mexico','cliente'),(29,'Julissa','Kings','Dureden','jduredeno@mediafire.com','1968-01-13','2437716277','Longview',2,20212,'Dixon','Santo Tomas','Mexico','cliente'),(30,'Tremayne','McAulay','Aslin','taslinp@webnode.com','1963-05-04','1680421212','Anderson',18010,7147,'Westridge','El Capulin','Mexico','cliente'),(31,'Brittaney','Goldsby','Girardet','bgirardetq@delicious.com','1972-03-28','886163639','Morrow',794,29543,'Leroy','El Carmen','Mexico','cliente'),(32,'Allene','Slaughter','Yuryatin','ayuryatinr@quantcast.com','1973-01-20','6882145991','Bobwhite',284,67275,'Scott','Pueblo Nuevo','Mexico','cliente'),(33,'Merci','Foucher','Loadman','mloadmans@sbwire.com','1966-01-06','8751347028','Del Sol',6,93003,'Northland','San Miguel','Mexico','cliente'),(34,'Van','Albert','Niblock','vniblockt@icq.com','1998-02-16','4388697712','American Ash',49886,25342,'Forest Dale','Hidalgo','Mexico','cliente'),(35,'Hilda','McAteer','Abramovitz','habramovitzu@wufoo.com','1990-08-10','548946641','Golf View',899,1687,'Florence','El Mirador','Mexico','cliente'),(36,'Dru','Ivashin','Stoney','dstoneyv@opensource.org','1990-02-09','9314472056','Stuart',9,35787,'Kingsford','San Miguel','Mexico','cliente'),(37,'Helsa','Gauford','Gippes','hgippesw@boston.com','1968-02-23','1500971211','Washington',7427,2541,'Dexter','San Juan','Mexico','cliente'),(38,'Michelle','Mackleden','Fifield','mfifieldx@npr.org','1982-08-01','3314716160','Loeprich',77798,29251,'Golf Course','San Lorenzo','Mexico','cliente'),(39,'Dillie','Deener','Petraitis','dpetraitisy@geocities.com','1979-11-21','2714008255','Twin Pines',1359,19941,'Lawn','San Lorenzo','Mexico','cliente'),(40,'Ingmar','Idel','Ames','iamesz@japanpost.jp','1969-03-02','7863485243','John Wall',985,26341,'Westend','Emiliano Zapata','Mexico','cliente'),(41,'Bernadina','Gripton','Strathearn','bstrathearn10@rediff.com','1961-11-26','7226549973','Esch',75,7260,'Carioca','Morelos','Mexico','cliente'),(42,'Klement','Bowdery','Gildersleeve','kgildersleeve11@yahoo.co.jp','1962-04-18','5297689915','Johnson',22655,45713,'Magdeline','Santiago','Mexico','cliente'),(43,'Katine','Baildon','MacHarg','kmacharg12@buzzfeed.com','1966-06-07','5766052900','Blackbird',7,33782,'Dawn','San Miguel','Mexico','cliente'),(44,'Lida','Buchanan','Lambertazzi','llambertazzi13@uiuc.edu','1994-11-22','4770936687','Dwight',553,44749,'Montana','Isidro Fabela','Mexico','cliente'),(45,'Channa','Fitzroy','Matyushkin','cmatyushkin14@360.cn','1984-03-22','1545164595','Reindahl',558,80416,'Waywood','San Martin','Mexico','cliente'),(46,'Susi','Slowgrove','Beetham','sbeetham15@alexa.com','1974-08-06','5581293491','Farmco',88,48782,'Bluestem','Santa Cruz','Mexico','cliente'),(47,'Elisabet','Tzar','Gleadhall','egleadhall16@51.la','1999-10-27','4698176375','Hagan',42,46515,'Kinsman','San Sebastian','Mexico','cliente'),(48,'Halsy','Conor','Waterland','hwaterland17@thetimes.co.uk','1966-10-14','2807343996','Maywood',38227,5860,'High Crossing','Pueblo Nuevo','Mexico','cliente'),(49,'Alfy','Kleine','Blackater','ablackater18@theatlantic.com','1975-01-08','4432386994','Green',8,82027,'Myrtle','Adolfo Lopez Mateos','Mexico','cliente'),(50,'Karina','Tabord','Le Barre','klebarre19@nsw.gov.au','1989-01-18','477409738','Norway Maple',624,20619,'Little Fleur','San Pedro','Mexico','cliente'),(51,'Chantalle','Keune','Breeton','cbreeton1a@soup.io','1957-07-06','2147021629','Darwin',44180,27650,'Westerfield','Adolfo Lopez Mateos','Mexico','cliente'),(52,'Grover','Young','Fitzsymons','gfitzsymons1b@newsvine.com','1963-02-07','683454701','Pankratz',7,35601,'Reindahl','Pueblo Nuevo','Mexico','cliente'),(53,'Lazaro','Otto','Everiss','leveriss1c@amazon.com','1976-03-14','164936233','Everett',6663,84323,'Weeping Birch','El Capulin','Mexico','cliente'),(54,'Nick','Ussher','Mouget','nmouget1d@storify.com','1975-08-13','244107594','Longview',3,79945,'Daystar','Guadalupe','Mexico','cliente'),(55,'Madison','Whooley','Stive','mstive1e@wunderground.com','1961-10-17','4889813597','Loeprich',7410,23583,'Lakeland','Guadalupe','Mexico','cliente'),(56,'Marybelle','Cordall','Hatrick','mhatrick1f@mozilla.org','1990-03-15','2876858784','Coleman',6,42919,'Welch','Emiliano Zapata','Mexico','cliente'),(57,'Fionnula','Petrelluzzi','Dyball','fdyball1g@ovh.net','1990-09-12','9429911935','David',416,25165,'Marquette','Morelos','Mexico','cliente'),(58,'Jaclyn','Bladon','Wigzell','jwigzell1h@dyndns.org','1969-10-12','1801254749','Mosinee',3338,90564,'Arizona','Emiliano Zapata','Mexico','cliente'),(59,'Madalyn','Dudden','Emmins','memmins1i@apache.org','1996-06-19','5714606928','Northport',901,40014,'Sycamore','El Mirador','Mexico','cliente'),(60,'Bettye','Lemar','Feacham','bfeacham1j@apache.org','1964-03-02','8438661198','Manley',99836,16832,'Bonner','Buenavista','Mexico','cliente'),(61,'Annaliese','Howlin','Roland','aroland1k@biglobe.ne.jp','1988-10-30','4579715905','Logan',6,29260,'Crescent Oaks','Emiliano Zapata','Mexico','cliente'),(62,'Remy','Klouz','Jenckes','rjenckes1l@sitemeter.com','1968-11-20','8698597428','Doe Crossing',1,91644,'Roth','Ojo de Agua','Mexico','cliente'),(63,'Mikey','Priddie','Dominici','mdominici1m@jigsy.com','1968-09-08','6942224331','Iowa',36,20207,'Dahle','La Palma','Mexico','cliente'),(64,'Zorah','Willgoss','Volk','zvolk1n@msu.edu','1999-07-04','2302498341','Lawn',332,30086,'Walton','Isidro Fabela','Mexico','cliente'),(65,'Sarena','Touhig','Dearman','sdearman1o@hhs.gov','1985-06-15','3908186021','North',18772,16506,'Kenwood','La Cañada','Mexico','cliente'),(66,'Kacie','Sneller','Defont','kdefont1p@indiegogo.com','1996-06-01','1722017842','Mallory',3,91644,'Luster','El Potrero','Mexico','cliente'),(67,'Prue','Meneghelli','Poel','ppoel1q@intel.com','1978-09-19','2980668693','Eastlawn',95700,97881,'Cottonwood','La Cañada','Mexico','cliente'),(68,'Clementia','Coomber','Flade','cflade1r@bravesites.com','1995-06-19','8171572157','Porter',94,47753,'Prairieview','San Sebastian','Mexico','cliente'),(69,'Jo','Liger','Hudspeth','jhudspeth1s@yellowpages.com','1954-01-09','7459126441','Tennyson',886,48618,'Johnson','San Juan','Mexico','cliente'),(70,'Malissa','Offa','Kliemke','mkliemke1t@japanpost.jp','2000-01-23','2682419422','Artisan',9129,72286,'Shasta','Isidro Fabela','Mexico','cliente'),(71,'Gennifer','Dahlberg','Baggett','gbaggett1u@webmd.com','1977-01-21','1433460115','Lakewood Gardens',6,28780,'Loomis','La Palma','Mexico','cliente'),(72,'Morten','Pieracci','Tapsell','mtapsell1v@posterous.com','1972-11-16','6386199852','Fisk',6,32872,'Shelley','El Capulin','Mexico','cliente'),(73,'Seline','O\'Shiel','Simon','ssimon1w@statcounter.com','1984-12-18','9904911193','Hoffman',72646,68271,'Di Loreto','La Mesa','Mexico','cliente'),(74,'Darelle','Foxten','Kroger','dkroger1x@princeton.edu','1995-06-21','8230696451','Arapahoe',6,64744,'Evergreen','Isidro Fabela','Mexico','cliente'),(75,'Ethelred','Hoyte','Gulliford','egulliford1y@facebook.com','1981-08-16','561326331','Meadow Ridge',5581,94145,'Rigney','Ojo de Agua','Mexico','cliente'),(76,'Valera','Faulconer','Gooch','vgooch1z@businesswire.com','1977-04-07','6797320424','Orin',85123,63236,'Warrior','Independencia','Mexico','cliente'),(77,'Rafe','Carnalan','McNeill','rmcneill20@sogou.com','1990-02-04','1757851709','Saint Paul',3,42772,'Forest Run','Buenavista','Mexico','cliente'),(78,'Flint','Strangeways','Lammas','flammas21@hc360.com','1960-03-11','698107857','Schlimgen',518,26846,'Barnett','San Juan','Mexico','cliente'),(79,'Dierdre','Rampage','Gummer','dgummer22@exblog.jp','1984-09-27','1970740287','Hanson',5998,33417,'Derek','La Laguna','Mexico','cliente'),(80,'Aldon','Connett','Shorland','ashorland23@answers.com','1969-02-24','7932669712','Hoard',1015,64253,'Meadow Valley','San Miguel','Mexico','cliente'),(81,'Mart','Sarfas','Swaile','mswaile24@jimdo.com','1991-04-24','7491905122','Londonderry',135,44059,'Crescent Oaks','Pueblo Nuevo','Mexico','cliente'),(82,'Darby','Kellegher','Ribbon','dribbon25@gov.uk','1955-10-17','3724882116','Red Cloud',9,88207,'Manitowish','La Mesa','Mexico','cliente'),(83,'Gabbi','Chasteau','Mankor','gmankor26@phpbb.com','1997-05-31','1090867105','Steensland',4,9650,'Westend','Adolfo Lopez Mateos','Mexico','cliente'),(84,'Axel','Garcia','Beltran','axel.G@gmail.com','2000-01-01','1234',NULL,NULL,NULL,NULL,NULL,NULL,'Cliente'),(85,'Alondra','Ramírez','Urquiza','alondra.r@ciencias.unam.mx','1999-04-07','1234',NULL,NULL,NULL,NULL,NULL,NULL,'Cliente'),(86,'Carlos','Garcia','Urquiza','hola@gmail.com','2023-05-11','123',NULL,NULL,NULL,NULL,NULL,NULL,'Cliente');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-23 12:49:09
