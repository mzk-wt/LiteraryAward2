CREATE TABLE `countries` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `code2` varchar(10) DEFAULT NULL,
  `code3` varchar(10) DEFAULT NULL,
  `name_jp` varchar(100) DEFAULT NULL,
  `name_en` varchar(100) DEFAULT NULL,
  `img_file_name` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8