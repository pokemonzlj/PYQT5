/*
Navicat MySQL Data Transfer

Source Server         : pokemon
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : small_game

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-12-04 17:56:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `weapon_shuxing`
-- ----------------------------
DROP TABLE IF EXISTS `weapon_shuxing`;
CREATE TABLE `weapon_shuxing` (
  `name` varchar(11) NOT NULL,
  `wugong` int(255) DEFAULT NULL,
  `wugong_chengzhang` int(11) DEFAULT NULL,
  `wufang` int(11) DEFAULT NULL,
  `wufang_chengzhang` int(11) DEFAULT NULL,
  `fagong` int(11) DEFAULT NULL,
  `fagong_chengzhang` int(11) DEFAULT NULL,
  `fafang` int(11) DEFAULT NULL,
  `fafang_chengzhang` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of weapon_shuxing
-- ----------------------------
INSERT INTO `weapon_shuxing` VALUES ('均衡外套', '1', '2', '4', '6', '1', '2', '4', '6');
INSERT INTO `weapon_shuxing` VALUES ('武士刃', '4', '8', '2', '5', '0', '0', '2', '3');
INSERT INTO `weapon_shuxing` VALUES ('法杖', '0', '0', '1', '3', '5', '8', '2', '5');
INSERT INTO `weapon_shuxing` VALUES ('燃烧之书', '0', '0', '0', '0', '6', '10', '1', '4');
INSERT INTO `weapon_shuxing` VALUES ('重剑', '6', '10', '1', '4', '0', '0', '0', '0');
INSERT INTO `weapon_shuxing` VALUES ('重盾', '2', '2', '6', '10', '0', '0', '0', '0');
INSERT INTO `weapon_shuxing` VALUES ('魔法结晶盾', '0', '0', '0', '0', '2', '2', '6', '10');
INSERT INTO `weapon_shuxing` VALUES ('魔法铠甲', '0', '0', '1', '3', '3', '4', '4', '8');
