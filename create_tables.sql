USE fdb;

CREATE TABLE user (
    userId INTEGER  NOT NULL,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(40) NOT NULL,
    PRIMARY KEY (userId)
);
CREATE TABLE admin (
    adminId INTEGER  NOT NULL,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(40) NOT NULL,
    PRIMARY KEY (adminId)
);
CREATE TABLE brand (
    brandId INTEGER  NOT NULL,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (brandId)
);
CREATE TABLE tag (
    tagId INTEGER  NOT NULL,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (tagId)
);
CREATE TABLE car (
    carId INTEGER NOT NULL,
    brand INTEGER,
    tag INTEGER,
    photoUrl VARCHAR(200),
    status TINYINT NOT NULL,
    PRIMARY KEY (carId),
    FOREIGN KEY (brand) REFERENCES brand (brandId)  ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (tag) REFERENCES tag (tagId)  ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE rent (
    rentId INTEGER NOT NULL,
    carId INTEGER NOT NULL,
    startT datetime NOT NULL,
    endT datetime NOT NULL,
    status TINYINT NOT NULL,
    PRIMARY KEY (rentId),
    FOREIGN KEY (carId) REFERENCES car (carId)  ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO user
VALUES (2,'Liz','liz@gmail.com', '12345');

INSERT INTO brand
VALUES (2,'BMW');

INSERT INTO tag
VALUES (2,'bmws');
