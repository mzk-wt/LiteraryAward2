CREATE TABLE `awards` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `kana` varchar(200) DEFAULT NULL,
  `url` text,
  `country_id` int(10) DEFAULT NULL,
  `start_year` int(4) DEFAULT NULL,
  `end_year` int(4) DEFAULT NULL,
  `overview` text,
  `frequency` varchar(50) DEFAULT NULL,
  `frequency_month` varchar(50) DEFAULT NULL,
  `award_type` varchar(20) DEFAULT NULL,
  `wikipedia_url` text,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8