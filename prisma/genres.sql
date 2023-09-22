TRUNCATE TABLE genres CASCADE;
DO $$
DECLARE
    seq_name TEXT;
BEGIN
    SELECT pg_get_serial_sequence('employees', 'id') INTO seq_name;
    EXECUTE 'ALTER SEQUENCE ' || seq_name || ' RESTART WITH 1';
END
$$;
INSERT INTO genres (id, name) VALUES (1,'Rock');
INSERT INTO genres (id, name) VALUES (2,'Jazz');
INSERT INTO genres (id, name) VALUES (3,'Metal');
INSERT INTO genres (id, name) VALUES (4,'Alternative & Punk');
INSERT INTO genres (id, name) VALUES (5,'Rock And Roll');
INSERT INTO genres (id, name) VALUES (6,'Blues');
INSERT INTO genres (id, name) VALUES (7,'Latin');
INSERT INTO genres (id, name) VALUES (8,'Reggae');
INSERT INTO genres (id, name) VALUES (9,'Pop');
INSERT INTO genres (id, name) VALUES (10,'Soundtrack');
INSERT INTO genres (id, name) VALUES (11,'Bossa Nova');
INSERT INTO genres (id, name) VALUES (12,'Easy Listening');
INSERT INTO genres (id, name) VALUES (13,'Heavy Metal');
INSERT INTO genres (id, name) VALUES (14,'R&B/Soul');
INSERT INTO genres (id, name) VALUES (15,'Electronica/Dance');
INSERT INTO genres (id, name) VALUES (16,'World');
INSERT INTO genres (id, name) VALUES (17,'Hip Hop/Rap');
INSERT INTO genres (id, name) VALUES (18,'Science Fiction');
INSERT INTO genres (id, name) VALUES (19,'TV Shows');
INSERT INTO genres (id, name) VALUES (20,'Sci Fi & Fantasy');
INSERT INTO genres (id, name) VALUES (21,'Drama');
INSERT INTO genres (id, name) VALUES (22,'Comedy');
INSERT INTO genres (id, name) VALUES (23,'Alternative');
INSERT INTO genres (id, name) VALUES (24,'Classical');
INSERT INTO genres (id, name) VALUES (25,'Opera');
--- update sequence on table genres
SELECT setval(pg_get_serial_sequence('genres', 'id'), coalesce(max(id)+1, 1), false) FROM genres;
