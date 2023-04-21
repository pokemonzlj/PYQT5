/*
Navicat MySQL Data Transfer

Source Server         : pokemon
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : small_game

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-12-04 17:56:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `weapon_info`
-- ----------------------------
DROP TABLE IF EXISTS `weapon_info`;
CREATE TABLE `weapon_info` (
  `name` varchar(255) NOT NULL,
  `leixing` int(11) DEFAULT NULL COMMENT '1武器，2防具',
  `pinzhi` int(11) DEFAULT NULL COMMENT '1普通，2附魔，3神器',
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of weapon_info
-- ----------------------------
INSERT INTO `weapon_info` VALUES ('代达罗斯之殇', '1', '3', null);
INSERT INTO `weapon_info` VALUES ('众神圣铠', '2', '3', null);
INSERT INTO `weapon_info` VALUES ('反射盾', '2', '3', null);
INSERT INTO `weapon_info` VALUES ('均衡外套', '2', '1', '300');
INSERT INTO `weapon_info` VALUES ('希瓦之守护', '2', '3', null);
INSERT INTO `weapon_info` VALUES ('撒旦之邪力', '1', '3', null);
INSERT INTO `weapon_info` VALUES ('武士刃', '1', '1', '300');
INSERT INTO `weapon_info` VALUES ('法杖', '1', '1', '300');
INSERT INTO `weapon_info` VALUES ('燃烧之书', '1', '1', '300');
INSERT INTO `weapon_info` VALUES ('虚无法杖', '1', '3', null);
INSERT INTO `weapon_info` VALUES ('蝴蝶短刃', '1', '3', null);
INSERT INTO `weapon_info` VALUES ('达贡之神力', '1', '3', null);
INSERT INTO `weapon_info` VALUES ('重剑', '1', '1', '300');
INSERT INTO `weapon_info` VALUES ('重盾', '2', '1', '300');
INSERT INTO `weapon_info` VALUES ('金箍棒', '1', '3', null);
INSERT INTO `weapon_info` VALUES ('雷神之锤', '1', '3', null);
INSERT INTO `weapon_info` VALUES ('魔法结晶盾', '2', '1', '300');
INSERT INTO `weapon_info` VALUES ('魔法铠甲', '2', '1', '300');
