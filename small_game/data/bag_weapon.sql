/*
Navicat MySQL Data Transfer

Source Server         : pokemon
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : small_game

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-12-04 17:56:19
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `bag_weapon`
-- ----------------------------
DROP TABLE IF EXISTS `bag_weapon`;
CREATE TABLE `bag_weapon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `equiped` int(2) DEFAULT '0' COMMENT '1装备，0未装备',
  `naijiu` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `effect` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bag_weapon
-- ----------------------------
INSERT INTO `bag_weapon` VALUES ('3', '20201121143746Zet', '法杖', '1', '16', '0', null);
INSERT INTO `bag_weapon` VALUES ('4', '20201121143746Zet', '均衡外套', '1', '7', '0', null);
INSERT INTO `bag_weapon` VALUES ('5', '20201121143746Zet', '武士刃', '0', '20', '2', null);
INSERT INTO `bag_weapon` VALUES ('9', '20201121143746Zet', '燃烧之书', '0', '20', '7', null);
