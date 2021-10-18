CREATE TABLE `authors` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `idx` varchar(10) NOT NULL COMMENT '索引',
  `name` varchar(200) NOT NULL COMMENT '名前',
  `kana` varchar(200) DEFAULT NULL COMMENT 'カナ',
  `born_date` varchar(20) DEFAULT NULL COMMENT '生年月日',
  `dead_date` varchar(20) DEFAULT NULL COMMENT '没年月日',
  `nationality_id` int(10) DEFAULT NULL COMMENT '国籍ID',
  `overview` text COMMENT '概要',
  `wikipedia_url` text COMMENT 'WIkipedia URL',
  `img_url` text COMMENT '画像URL',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `idx_01` (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='著者テーブル'