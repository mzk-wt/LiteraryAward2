CREATE TABLE `books` (
  `id` int(19) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `idx` varchar(50) DEFAULT NULL COMMENT '索引',
  `title` varchar(200) DEFAULT NULL COMMENT 'タイトル',
  `kana` varchar(200) DEFAULT NULL COMMENT 'カナ',
  `overview` text COMMENT '概要',
  `isbn` varchar(30) DEFAULT NULL COMMENT 'ISBN',
  `publication_date` varchar(20) DEFAULT NULL COMMENT '発売日',
  `img_url` text COMMENT '画像URL',
  `amazon_url` text COMMENT 'AmazonアフィリエイトURL',
  `kindle_url` text COMMENT 'KindleアフィリエイトURL',
  `rakuten_url` text COMMENT '楽天アフィリエイトURL',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8