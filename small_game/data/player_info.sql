/*
Navicat MySQL Data Transfer

Source Server         : pokemon
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : small_game

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-12-04 17:56:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `player_info`
-- ----------------------------
DROP TABLE IF EXISTS `player_info`;
CREATE TABLE `player_info` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `gold` int(11) DEFAULT NULL,
  `jingyan` float DEFAULT NULL,
  `level` int(11) DEFAULT '0',
  `xingdongli` int(11) DEFAULT '200',
  `shuxingdian` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of player_info
-- ----------------------------
INSERT INTO `player_info` VALUES ('20201121143223tSH', '20201121143223tSH', '1000', '0', '0', '200', '10');
INSERT INTO `player_info` VALUES ('20201121143746Zet', 'zhu', '0', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201121150129AXs', '20201121150129AXs', '500', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201121163602nqb', 'qqq', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201121172232USB', '20201121172232USB', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123095131Srq', '20201123095131Srq', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123100541Qmk', 'dadiao', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123100610wRe', 'sunhuiyuan', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123100914KAO', 'caiji', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123134508bby', '20201123134508bby', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123135014Uuc', '20201123135014Uuc', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123135051WJY', '20201123135051WJY', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123135538FXf', '20201123135538FXf', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123154631GME', 'aaaa', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123185741NcE', 'test', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123190416Uuh', 'ttyyy', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123190718gjM', '20201123190718gjM', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201123191004GDK', '20201123191004GDK', '1000', '0', '0', '200', '0');
INSERT INTO `player_info` VALUES ('20201125181431igq', 'tangqingqing', '1000', '0', '1', '200', '0');
