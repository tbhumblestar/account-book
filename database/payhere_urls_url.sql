-- MySQL dump 10.13  Distrib 5.7.41, for Win64 (x86_64)
--
-- Host: localhost    Database: payhere
-- ------------------------------------------------------
-- Server version	5.7.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `urls_url`
--

DROP TABLE IF EXISTS `urls_url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `urls_url` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL,
  `expired_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `urls_url`
--

LOCK TABLES `urls_url` WRITE;
/*!40000 ALTER TABLE `urls_url` DISABLE KEYS */;
INSERT INTO `urls_url` VALUES (1,'http://127.0.0.1:8000/admin/test','2023-02-11 16:28:45.699522'),(2,'http://127.0.0.1:8000/admin/test','2023-02-11 16:29:19.327347'),(3,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 07:36:49.692635'),(4,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:29.655446'),(5,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:42.506443'),(6,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:43.108648'),(7,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:43.708512'),(8,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:44.238878'),(9,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:44.842844'),(10,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:45.390218'),(11,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:45.946588'),(12,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:46.525976'),(13,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:47.068905'),(14,'http://127.0.0.1:8000/admin/urls/aab','2023-02-12 08:38:47.647737');
/*!40000 ALTER TABLE `urls_url` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-09 18:12:55
