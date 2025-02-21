
INSERT INTO roles
(id, role_name, role_description, created_on, created_by, modified_on, modified_by, active_flag)
VALUES(nextval('roles_id_seq'::regclass), 'ADMIN', '', CURRENT_TIMESTAMP,'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1),
(nextval('roles_id_seq'::regclass), 'TEACHER', '', CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1),
(nextval('roles_id_seq'::regclass), 'STUDENT', '', CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1);


--TRUNCATE TABLE users RESTART IDENTITY CASCADE;
INSERT INTO users
(id, user_first_name, user_last_name, user_e_mail_id, user_phone_number, user_login_id, user_password, client_id, created_on, created_by, modified_on, modified_by, active_flag)
VALUES(
(nextval('users_id_seq'::regclass), 'bhagavan', 'prasad', 'bhagavan', '9700983456', 'bhagavan', 
'jnjnuh', 1, CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1),

(nextval('users_id_seq'::regclass), 'sudhakar', 'p', 'sudhakar', '9700983456', 'bhagavan', 
'jnjnuh', 1, CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1),

(nextval('users_id_seq'::regclass), 'saketh', 'ram', 'saketh', '6301123456', 'saketh', 
'jnjnuh', 1, CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1));



INSERT INTO user_roles
(id, user_id, role_id, created_on, created_by, modified_on, modified_by, active_flag)
VALUES(nextval('user_roles_id_seq'::regclass), 1, 1, CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1),
(nextval('user_roles_id_seq'::regclass), 1, 1, CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1),
(nextval('user_roles_id_seq'::regclass), 2, 2, CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1),
(nextval('user_roles_id_seq'::regclass), 3, 3, CURRENT_TIMESTAMP, 'bhagavan', CURRENT_TIMESTAMP, 'bhagavan', 1);
