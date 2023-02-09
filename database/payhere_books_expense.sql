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
-- Table structure for table `books_expense`
--

DROP TABLE IF EXISTS `books_expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_expense` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `amount` int(10) unsigned NOT NULL,
  `memo` longtext,
  `book_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_expense_book_id_b1853a6c_fk_books_book_id` (`book_id`),
  CONSTRAINT `books_expense_book_id_b1853a6c_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_expense`
--

LOCK TABLES `books_expense` WRITE;
/*!40000 ALTER TABLE `books_expense` DISABLE KEYS */;
INSERT INTO `books_expense` VALUES (1,'2023-01-03',9000,'1월 과자',1),(2,'2023-01-03',4000,'1월 수영',1),(3,'2023-01-03',10000,'1월 감자',1),(4,'2023-01-05',65000,'1월 감자',1),(5,'2023-01-06',65000,'1월 감자',1),(6,'2023-01-09',65000,'1월 감자',1),(7,'2023-01-21',65000,'1월 감자',1),(8,'2023-01-22',65000,'1월 감자',1),(9,'2023-02-01',65000,'1월 감자',1),(10,'2023-01-30',65000,'1월 감자',2),(11,'2023-01-30',65000,'2월 감자',2),(12,'2023-01-30',10000,'1월 감자',2),(13,'2023-01-30',10000,'1월 감자',2),(14,'2023-01-30',10000,'1월 감자',2),(15,'2023-01-31',65000,'1월 감자',2);
/*!40000 ALTER TABLE `books_expense` ENABLE KEYS */;
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
