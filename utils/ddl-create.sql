/*Roles table*/
DROP TABLE roles;
CREATE TABLE roles (
	id SERIAL PRIMARY KEY,
	role_name VARCHAR(125) NOT NULL,
	role_description VARCHAR(250) NOT NULL,
	created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	created_by VARCHAR(125),
	modified_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,	
	modified_by	VARCHAR(125),
	active_flag SMALLINT NOT NULL
);

/*Users table*/
DROP TABLE users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	user_first_name VARCHAR(125) NOT NULL,
	user_last_name VARCHAR(125) NOT NULL,
	user_e_mail_id VARCHAR(125),
	user_phone_number VARCHAR(125),
	user_login_id VARCHAR(125) NOT NULL,
	user_password VARCHAR(250) NOT NULL,
	client_id INTEGER NOT NULL,
	created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	created_by VARCHAR(125),
	modified_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,	
	modified_by	VARCHAR(125),
	active_flag SMALLINT NOT null
);


/*User Role Mapping table*/
DROP TABLE user_roles;
CREATE TABLE user_roles (
	id SERIAL PRIMARY KEY,
	user_id INTEGER NOT NULL,
	role_id INTEGER NOT NULL,
	created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	created_by VARCHAR(125),
	modified_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,	
	modified_by	VARCHAR(125),
	active_flag SMALLINT NOT null,
	CONSTRAINT fk_user_roles_1 FOREIGN KEY (user_id) REFERENCES users(id),
	CONSTRAINT fk_user_roles_2 FOREIGN KEY (role_id) REFERENCES roles(id)
);


CREATE TABLE user_tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    token TEXT NOT NULL,
	created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	created_by VARCHAR(125),
	modified_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,	
	modified_by	VARCHAR(125),
	active_flag SMALLINT NOT null,
    CONSTRAINT fk_user_tokens_user_id FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);	

DROP TABLE authroles;
CREATE TABLE auth_roles (
	id SERIAL PRIMARY KEY,
	role_name VARCHAR(125) NOT NULL,
	role_description VARCHAR(250) NOT NULL,
	created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	created_by VARCHAR(125),
	modified_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,	
	modified_by	VARCHAR(125),
	active_flag SMALLINT NOT NULL
);
