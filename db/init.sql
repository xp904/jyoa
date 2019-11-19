create DATABASE jyoa CHARSET utf8;
use jyoa;

-- 创建系统用户表
CREATE  TABLE sys_user(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) UNIQUE NOT NULL ,
  auth_string VARCHAR(100) NOT NULL ,
  email VARCHAR(50),
  phone VARCHAR(50)
);

-- 创建角色表
CREATE TABLE  sys_role(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE ,
  code VARCHAR(20) NOT NULL UNIQUE
);

-- 创建用户角色表
create TABLE  sys_user_role(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_id INTEGER,
  role_id INTEGER
);

-- 插入初始管理系统的数据
INSERT INTO sys_user(name, auth_string) VALUES
  ('admin', 'admin'),
  ('disen', 'disen');

INSERT INTO sys_role(name, code) VALUES
  ('超级管理员', 'admin'),
  ('管理员', 'common');

INSERT INTO sys_user_role(user_id, role_id) VALUES
  (1, 1),
  (2, 2);


-- 查询用户名和对应的角色信息
select
  u.name as user_name,
  r.name as role_name,
  r.code as role_code
from sys_user u
JOIN sys_user_role ur ON (u.id = ur.user_id)
JOIN sys_role r ON (r.id = ur.role_id);
