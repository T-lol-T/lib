/*
 Navicat Premium Data Transfer

 Source Server         : 753
 Source Server Type    : MySQL
 Source Server Version : 50562
 Source Host           : localhost:3306
 Source Schema         : student

 Target Server Type    : MySQL
 Target Server Version : 50562
 File Encoding         : 65001

 Date: 04/12/2023 00:24:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `cid` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `course_name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacher` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `classroom` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `credit` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`cid`) USING BTREE,
  INDEX `cid`(`cid`) USING BTREE,
  INDEX `teacher`(`teacher`) USING BTREE,
  INDEX `course_name`(`course_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('c1', '数据结构', '李北', '周二3-5', '1-112', '2');
INSERT INTO `course` VALUES ('c2', '计算机原理', '宏岗', '周四7-8', '2-321', '2');
INSERT INTO `course` VALUES ('c3', '数据库原理', '黄莉莉', '周五9-10', '1-202', '2');
INSERT INTO `course` VALUES ('c4', '离散数学', '孙兴', '周一3-5', '1-310', '2');
INSERT INTO `course` VALUES ('c5', 'Linux系统', '祝霆锋', '周一6-8', '2-221', '2');
INSERT INTO `course` VALUES ('c6', '计算机网络', '孙兴', '周五8-10', '5-321', '1');

-- ----------------------------
-- Table structure for dept_info
-- ----------------------------
DROP TABLE IF EXISTS `dept_info`;
CREATE TABLE `dept_info`  (
  `dept_name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `major_name` char(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  INDEX `dept_name`(`dept_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of dept_info
-- ----------------------------
INSERT INTO `dept_info` VALUES ('信息工程学院', '计算机科学,软件工程,物联网工程');
INSERT INTO `dept_info` VALUES ('艺术学院', '音乐,舞蹈,美术');
INSERT INTO `dept_info` VALUES ('经济与管理学院', '会计学,工商管理,对外贸易,电子商务');
INSERT INTO `dept_info` VALUES ('教育学院', '学前教育,小学教育,教育学');
INSERT INTO `dept_info` VALUES ('法学院', '经济法,行政管理法,刑法学');

-- ----------------------------
-- Table structure for exam_makeup
-- ----------------------------
DROP TABLE IF EXISTS `exam_makeup`;
CREATE TABLE `exam_makeup`  (
  `sid` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `stu_name` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cid` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `course_name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  INDEX `exam_sid`(`sid`) USING BTREE,
  CONSTRAINT `exam_sid` FOREIGN KEY (`sid`) REFERENCES `student_info` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of exam_makeup
-- ----------------------------
INSERT INTO `exam_makeup` VALUES ('s2', '刘晓鸣', 'c2', '计算机原理', '63');

-- ----------------------------
-- Table structure for student_course
-- ----------------------------
DROP TABLE IF EXISTS `student_course`;
CREATE TABLE `student_course`  (
  `sid` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_name` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cid` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `course_name` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  INDEX `cid`(`cid`) USING BTREE,
  INDEX `stu_name`(`stu_name`) USING BTREE,
  INDEX `sid`(`sid`) USING BTREE,
  INDEX `course_name`(`course_name`) USING BTREE,
  CONSTRAINT `cid` FOREIGN KEY (`cid`) REFERENCES `course` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sid` FOREIGN KEY (`sid`) REFERENCES `student_info` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of student_course
-- ----------------------------
INSERT INTO `student_course` VALUES ('s3', '李明', 'c3', '数据库原理', NULL);
INSERT INTO `student_course` VALUES ('s4', '张鹰', 'c1', '数据结构', NULL);
INSERT INTO `student_course` VALUES ('s5', '刘竞静', 'c1', '数据结构', NULL);
INSERT INTO `student_course` VALUES ('s5', '刘竞静', 'c2', '计算机原理', NULL);
INSERT INTO `student_course` VALUES ('s2', '刘晓鸣', 'c3', '数据库原理', NULL);
INSERT INTO `student_course` VALUES ('s1', '刘强', 'c5', 'Linux系统', '63');
INSERT INTO `student_course` VALUES ('s1', '刘强', 'c3', '数据库原理', NULL);
INSERT INTO `student_course` VALUES ('s3', '李明', 'c1', '数据结构', NULL);
INSERT INTO `student_course` VALUES ('s11', '文件时', 'c1', '数据结构', NULL);
INSERT INTO `student_course` VALUES ('s10', '隆冬强', 'c1', '数据结构', NULL);
INSERT INTO `student_course` VALUES ('s6', '刘成刚', 'c3', '数据库原理', NULL);
INSERT INTO `student_course` VALUES ('s7', '王铭', 'c5', 'Linux系统', NULL);
INSERT INTO `student_course` VALUES ('s8', '宣明尼', 'c2', '计算机原理', NULL);
INSERT INTO `student_course` VALUES ('s9', '夏惠清', 'c6', '计算机网络', NULL);
INSERT INTO `student_course` VALUES ('s4', '张鹰', 'c6', '计算机网络', NULL);
INSERT INTO `student_course` VALUES ('s11', '文件时', 'c2', '计算机原理', NULL);
INSERT INTO `student_course` VALUES ('s11', '文件时', 'c3', '数据库原理', NULL);
INSERT INTO `student_course` VALUES ('s11', '文件时', 'c4', '离散数学', NULL);

-- ----------------------------
-- Table structure for student_info
-- ----------------------------
DROP TABLE IF EXISTS `student_info`;
CREATE TABLE `student_info`  (
  `sid` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `age` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_name` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`sid`) USING BTREE,
  INDEX `login_sid`(`sid`) USING BTREE,
  INDEX `depart_name`(`dept_name`) USING BTREE,
  CONSTRAINT `depart_name` FOREIGN KEY (`dept_name`) REFERENCES `dept_info` (`dept_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `student_num` FOREIGN KEY (`sid`) REFERENCES `user_info_student` (`user_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of student_info
-- ----------------------------
INSERT INTO `student_info` VALUES ('s1', '刘强', '男', '19', '信息工程学院');
INSERT INTO `student_info` VALUES ('s10', '隆冬强', '男', '20', '信息工程学院');
INSERT INTO `student_info` VALUES ('s11', '文件时', '男', '22', '信息工程学院');
INSERT INTO `student_info` VALUES ('s2', '刘晓鸣', '男', '20', '信息工程学院');
INSERT INTO `student_info` VALUES ('s3', '李明', '男', '22', '信息工程学院');
INSERT INTO `student_info` VALUES ('s4', '张鹰', '男', '21', '信息工程学院');
INSERT INTO `student_info` VALUES ('s5', '刘竞静', '男', '22', '信息工程学院');
INSERT INTO `student_info` VALUES ('s6', '刘成刚', '男', '21', '信息工程学院');
INSERT INTO `student_info` VALUES ('s7', '王铭', '女', '22', '信息工程学院');
INSERT INTO `student_info` VALUES ('s8', '宣明尼', '女', '18', '信息工程学院');
INSERT INTO `student_info` VALUES ('s9', '夏惠清', '女', '19', '信息工程学院');

-- ----------------------------
-- Table structure for teacher_info
-- ----------------------------
DROP TABLE IF EXISTS `teacher_info`;
CREATE TABLE `teacher_info`  (
  `tid` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `age` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pro_title` char(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_name` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tid`) USING BTREE,
  INDEX `name`(`name`) USING BTREE,
  INDEX `login_tid`(`tid`) USING BTREE,
  CONSTRAINT `teacher_num` FOREIGN KEY (`tid`) REFERENCES `user_info_teacher` (`user_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of teacher_info
-- ----------------------------
INSERT INTO `teacher_info` VALUES ('t1', '祝霆锋', '男', '39', '教授', '信息工程学院');
INSERT INTO `teacher_info` VALUES ('t2', '孙兴', '男', '40', '副教授', '信息工程学院');
INSERT INTO `teacher_info` VALUES ('t3', '黄莉莉', '女', '42', '讲师', '信息工程学院');
INSERT INTO `teacher_info` VALUES ('t4', '宏岗', '男', '61', '讲师', '信息工程学院');
INSERT INTO `teacher_info` VALUES ('t5', '李北', '男', '58', '助教', '信息工程学院');

-- ----------------------------
-- Table structure for user_info_student
-- ----------------------------
DROP TABLE IF EXISTS `user_info_student`;
CREATE TABLE `user_info_student`  (
  `user_name` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  INDEX `user_name`(`user_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_info_student
-- ----------------------------
INSERT INTO `user_info_student` VALUES ('s1', '1');
INSERT INTO `user_info_student` VALUES ('s10', '10');
INSERT INTO `user_info_student` VALUES ('s11', '11');
INSERT INTO `user_info_student` VALUES ('s2', '2');
INSERT INTO `user_info_student` VALUES ('s3', '3');
INSERT INTO `user_info_student` VALUES ('s4', '4');
INSERT INTO `user_info_student` VALUES ('s5', '5');
INSERT INTO `user_info_student` VALUES ('s6', '6');
INSERT INTO `user_info_student` VALUES ('s7', '7');
INSERT INTO `user_info_student` VALUES ('s8', '8');
INSERT INTO `user_info_student` VALUES ('s9', '9');

-- ----------------------------
-- Table structure for user_info_teacher
-- ----------------------------
DROP TABLE IF EXISTS `user_info_teacher`;
CREATE TABLE `user_info_teacher`  (
  `user_name` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  INDEX `user_name`(`user_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_info_teacher
-- ----------------------------
INSERT INTO `user_info_teacher` VALUES ('t1', '11');
INSERT INTO `user_info_teacher` VALUES ('t2', '12');
INSERT INTO `user_info_teacher` VALUES ('t3', '13');
INSERT INTO `user_info_teacher` VALUES ('t4', '14');
INSERT INTO `user_info_teacher` VALUES ('t5', '15');

SET FOREIGN_KEY_CHECKS = 1;
