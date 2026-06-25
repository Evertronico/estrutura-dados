CREATE DATABASE IF NOT EXISTS `secretaria_saude` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `secretaria_saude`;



CREATE TABLE `pacientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `pacientes` VALUES 
(1,'João Silva','111.111.111-11','1970-05-10','32999990001','Centro'),
(2,'Maria Souza','222.222.222-22','1965-03-12','32999990002','Rosário'),
(3,'Pedro Lima','333.333.333-33','1988-09-20','32999990003','Industrial'),
(4,'Ana Costa','444.444.444-44','1992-11-11','32999990004','Centro'),
(5,'Carlos Mendes','555.555.555-55','1955-07-01','32999990005','São José'),
(6,'Fernanda Rocha','666.666.666-66','2000-02-15','32999990006','Boa Vista'),
(7,'Ricardo Alves','777.777.777-77','1980-12-22','32999990007','Centro'),
(8,'Juliana Martins','888.888.888-88','1997-06-08','32999990008','Rosário'),
(9,'Lucas Oliveira','999.999.999-99','1978-10-05','32999990009','Industrial'),
(10,'Patrícia Gomes','101.101.101-10','1985-04-30','32999990010','São Pedro');

CREATE TABLE `solicitacoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `paciente_id` int DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  `gravidade` int DEFAULT NULL,
  `urgencia` int DEFAULT NULL,
  `data_solicitacao` datetime DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `paciente_id` (`paciente_id`),
  CONSTRAINT `solicitacoes_ibfk_1` FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `historico_movimentacoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `solicitacao_id` int DEFAULT NULL,
  `data_movimentacao` datetime DEFAULT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `solicitacao_id` (`solicitacao_id`),
  CONSTRAINT `historico_movimentacoes_ibfk_1` FOREIGN KEY (`solicitacao_id`) REFERENCES `solicitacoes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `solicitacoes` VALUES (101,1,'CONSULTA','Cardiologia',5,5,'2026-03-01 08:00:00','CONCLUIDO')
,(102,2,'EXAME','Hemograma',2,1,'2026-03-01 08:05:00','AGUARDANDO')
,(103,3,'MEDICAMENTO','Insulina',5,5,'2026-03-01 08:10:00','AGUARDANDO')
,(104,4,'CONSULTA','Ortopedia',3,2,'2026-03-01 08:15:00','AGUARDANDO'),
(105,5,'EXAME','Tomografia',4,4,'2026-03-01 08:20:00','AGUARDANDO'),
(106,6,'MEDICAMENTO','Losartana',2,2,'2026-03-01 08:25:00','AGUARDANDO'),
(107,7,'CONSULTA','Neurologia',5,4,'2026-03-01 08:30:00','AGUARDANDO'),
(108,8,'EXAME','Ultrassom',2,1,'2026-03-01 08:35:00','AGUARDANDO')
,(109,9,'MEDICAMENTO','Metformina',3,2,'2026-03-01 08:40:00','AGUARDANDO'),
(110,10,'CONSULTA','Dermatologia',1,1,'2026-03-01 08:45:00','AGUARDANDO')
,(111,1,'EXAME','Ressonancia',5,5,'2026-03-01 09:00:00','AGUARDANDO'),
(112,2,'CONSULTA','Pediatria',3,3,'2026-03-01 09:05:00','AGUARDANDO'),
(113,3,'MEDICAMENTO','Amoxicilina',2,2,'2026-03-01 09:10:00','AGUARDANDO'),
(114,4,'CONSULTA','Geriatria',4,4,'2026-03-01 09:15:00','AGUARDANDO'),
(115,5,'EXAME','Raio-X',2,2,'2026-03-01 09:20:00','AGUARDANDO'),
(116,6,'MEDICAMENTO','Dipirona',1,1,'2026-03-01 09:25:00','AGUARDANDO'),
(117,7,'CONSULTA','Oftalmologia',3,3,'2026-03-01 09:30:00','AGUARDANDO'),
(118,8,'EXAME','Colonoscopia',5,4,'2026-03-01 09:35:00','AGUARDANDO'),
(119,9,'MEDICAMENTO','AAS',2,1,'2026-03-01 09:40:00','AGUARDANDO'),
(120,10,'CONSULTA','Psiquiatria',4,5,'2026-03-01 09:45:00','AGUARDANDO'),
(121,1,'EXAME','Mamografia',4,3,'2026-03-01 10:00:00','AGUARDANDO'),
(122,2,'MEDICAMENTO','Omeprazol',1,1,'2026-03-01 10:05:00','AGUARDANDO'),
(123,3,'CONSULTA','Endocrinologia',5,4,'2026-03-01 10:10:00','AGUARDANDO'),
(124,4,'EXAME','Ecocardiograma',5,5,'2026-03-01 10:15:00','AGUARDANDO'),
(125,5,'MEDICAMENTO','Insulina',5,5,'2026-03-01 10:20:00','AGUARDANDO')
,(126,6,'CONSULTA','Cardiologia',4,5,'2026-03-01 10:25:00','AGUARDANDO'),
(127,7,'EXAME','Hemograma',1,1,'2026-03-01 10:30:00','AGUARDANDO')
,(128,8,'MEDICAMENTO','Metformina',3,2,'2026-03-01 10:35:00','AGUARDANDO'),
(129,9,'CONSULTA','Ortopedia',2,2,'2026-03-01 10:40:00','AGUARDANDO'),
(130,10,'EXAME','Tomografia',5,4,'2026-03-01 10:45:00','AGUARDANDO'),
(131,1,'MEDICAMENTO','Losartana',2,2,'2026-03-01 11:00:00','AGUARDANDO'),
(132,2,'CONSULTA','Neurologia',5,5,'2026-03-01 11:05:00','AGUARDANDO'),
(133,3,'EXAME','Ultrassom',2,1,'2026-03-01 11:10:00','AGUARDANDO'),
(134,4,'MEDICAMENTO','Dipirona',1,1,'2026-03-01 11:15:00','AGUARDANDO'),
(135,5,'CONSULTA','Dermatologia',1,1,'2026-03-01 11:20:00','AGUARDANDO'),
(136,6,'EXAME','Ressonancia',5,5,'2026-03-01 11:25:00','AGUARDANDO'),
(137,7,'MEDICAMENTO','Amoxicilina',3,2,'2026-03-01 11:30:00','AGUARDANDO'),
(138,8,'CONSULTA','Pediatria',2,3,'2026-03-01 11:35:00','AGUARDANDO'),
(139,9,'EXAME','Raio-X',2,1,'2026-03-01 11:40:00','AGUARDANDO'),
(140,10,'MEDICAMENTO','AAS',1,1,'2026-03-01 11:45:00','AGUARDANDO'),
(141,1,'CONSULTA','Cardiologia',5,5,'2026-03-01 12:00:00','AGUARDANDO'),
(142,2,'EXAME','Ecocardiograma',5,4,'2026-03-01 12:05:00','AGUARDANDO'),
(143,3,'MEDICAMENTO','Insulina',5,5,'2026-03-01 12:10:00','AGUARDANDO'),
(144,4,'CONSULTA','Psiquiatria',3,3,'2026-03-01 12:15:00','AGUARDANDO'),
(145,5,'EXAME','Colonoscopia',4,4,'2026-03-01 12:20:00','AGUARDANDO'),
(146,6,'MEDICAMENTO','Omeprazol',1,1,'2026-03-01 12:25:00','AGUARDANDO'),
(147,7,'CONSULTA','Endocrinologia',4,5,'2026-03-01 12:30:00','AGUARDANDO'),
(148,8,'EXAME','Mamografia',3,3,'2026-03-01 12:35:00','AGUARDANDO'),
(149,9,'MEDICAMENTO','Metformina',2,2,'2026-03-01 12:40:00','AGUARDANDO'),
(150,10,'CONSULTA','Geriatria',4,4,'2026-03-01 12:45:00','AGUARDANDO');