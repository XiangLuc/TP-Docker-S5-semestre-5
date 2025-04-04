CREATE TABLE IF NOT EXISTS hello (
    id SERIAL PRIMARY KEY,
    message VARCHAR(256)
);

INSERT INTO hello (message) VALUES ('Hello world.');
INSERT INTO hello (message) VALUES ('Deuxième message.');
INSERT INTO hello (message) VALUES ('Trosième message.');
