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
    brand INTEGER,
    tag INTEGER,
    photoUrl VARCHAR(200),
    status TINYINT NOT NULL,
    PRIMARY KEY (carId),
    FOREIGN KEY (brand) REFERENCES brand (brandId),
    FOREIGN KEY (tag) REFERENCES tag (tagId)
);
CREATE TABLE rent (
    rentId INTEGER NOT NULL AUTO_INCREMENT,
    carId INTEGER NOT NULL,
    startT datetime NOT NULL,
    endT datetime NOT NULL,
    status TINYINT NOT NULL,
    PRIMARY KEY (rentId),
    FOREIGN KEY (carId) REFERENCES car (carId)
);
