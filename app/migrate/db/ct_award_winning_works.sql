CREATE TABLE `award_winning_works` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `award_id` int(10) NOT NULL COMMENT '文学賞ID',
  `times` int(10) NOT NULL COMMENT '文学賞回数',
  `award_date` varchar(20) DEFAULT NULL COMMENT '受賞年月',
  `book_id` int(19) DEFAULT NULL COMMENT '書籍ID',
  `author_id` int(10) DEFAULT NULL COMMENT '著者ID',
  `tw_count` int(10) DEFAULT NULL COMMENT 'ツイート回数',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `idx_001` (`award_id`),
  KEY `idx_002` (`book_id`),
  KEY `idx_003` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8