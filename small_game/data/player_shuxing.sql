/*
Navicat MySQL Data Transfer

Source Server         : pokemon
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : small_game

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-12-04 17:56:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `player_shuxing`
-- ----------------------------
DROP TABLE IF EXISTS `player_shuxing`;
CREATE TABLE `player_shuxing` (
  `id` varchar(255) NOT NULL,
  `current_hp` int(11) DEFAULT NULL,
  `hp` int(11) DEFAULT NULL,
  `liliang` int(11) DEFAULT NULL,
  `fali` int(11) DEFAULT NULL,
  `minjie` int(11) DEFAULT NULL,
  `xingyun` int(11) DEFAULT NULL,
  `jiqiao` int(11) DEFAULT NULL,
  `yili` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of player_shuxing
-- ----------------------------
INSERT INTO `player_shuxing` VALUES ('20201121143223tSH', '10', '10', '0', '0', '0', '0', '0', '0');
INSERT INTO `player_shuxing` VALUES ('20201121143746Zet', '10', '11', '0', '10', '7', '4', '2', '1');
INSERT INTO `player_shuxing` VALUES ('20201121150129AXs', '5', '11', '1', '3', '6', '2', '0', '0');
INSERT INTO `player_shuxing` VALUES ('20201121163602nqb', '0', '15', '1', '0', '0', '3', '0', '4');
INSERT INTO `player_shuxing` VALUES ('20201121172232USB', '0', '11', '4', '0', '5', '0', '0', '0');
INSERT INTO `player_shuxing` VALUES ('20201123095131Srq', '1', '10', '0', '5', '5', '0', '0', '0');
INSERT INTO `player_shuxing` VALUES ('20201123100541Qmk', '4', '13', '2', '0', '5', '1', '1', '1');
INSERT INTO `player_shuxing` VALUES ('20201123100610wRe', '4', '14', '1', '0', '4', '0', '4', '0');
INSERT INTO `player_shuxing` VALUES ('20201123100914KAO', '4', '13', '2', '2', '1', '0', '5', '0');
INSERT INTO `player_shuxing` VALUES ('20201123134508bby', '4', '14', '0', '2', '0', '2', '2', '3');
INSERT INTO `player_shuxing` VALUES ('20201123135014Uuc', '4', '10', '1', '2', '4', '4', '0', '2');
INSERT INTO `player_shuxing` VALUES ('20201123135051WJY', '4', '12', '1', '0', '3', '2', '1', '4');
INSERT INTO `player_shuxing` VALUES ('20201123135538FXf', '4', '10', '3', '0', '5', '0', '1', '4');
INSERT INTO `player_shuxing` VALUES ('20201123154631GME', '4', '14', '2', '0', '1', '4', '2', '0');
INSERT INTO `player_shuxing` VALUES ('20201123185741NcE', '10', '10', '2', '7', '0', '4', '0', '0');
INSERT INTO `player_shuxing` VALUES ('20201123190416Uuh', '12', '12', '2', '0', '0', '5', '4', '0');
INSERT INTO `player_shuxing` VALUES ('20201123190718gjM', '10', '10', '1', '0', '5', '4', '0', '0');
INSERT INTO `player_shuxing` VALUES ('20201123191004GDK', '10', '10', '5', '0', '5', '0', '0', '0');
INSERT INTO `player_shuxing` VALUES ('20201125181431igq', '13', '13', '1', '1', '1', '0', '7', '0');
