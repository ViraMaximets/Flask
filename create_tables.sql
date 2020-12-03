USE fdb;

CREATE TABLE user (
    userId INTEGER  NOT NULL AUTO_INCREMENT,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(40) NOT NULL,
    PRIMARY KEY (userId)
);
CREATE TABLE admin (
    adminId INTEGER  NOT NULL AUTO_INCREMENT,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(40) NOT NULL,

    PRIMARY KEY (adminId)
);
CREATE TABLE brand (
    brandId INTEGER  NOT NULL AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,

    PRIMARY KEY (brandId)
);
CREATE TABLE tag (
    tagId INTEGER  NOT NULL AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,

    PRIMARY KEY (tagId)
);
CREATE TABLE car (
    carId INTEGER NOT NULL AUTO_INCREMENT,

    brand_id INTEGER,
    tag_id INTEGER,
    photoUrl VARCHAR(200),
    status TINYINT NOT NULL,

    PRIMARY KEY (carId),

    FOREIGN KEY (brand_id) REFERENCES brand(brandId),
    FOREIGN KEY (tag_id) REFERENCES tag(tagId)
);
CREATE TABLE rent (
    rentId INTEGER NOT NULL AUTO_INCREMENT,
    car_id INTEGER NOT NULL,
    startT datetime NOT NULL,
    endT datetime NOT NULL,
    status TINYINT NOT NULL,

    PRIMARY KEY (rentId),

    FOREIGN KEY (car_id) REFERENCES car(carId)
);


INSERT INTO user (userId, username, email, password)
VALUES (1,'Liz','liz@gmail.com','12345');

INSERT INTO brand (brandId, name)
VALUES (1, 'bmw')

