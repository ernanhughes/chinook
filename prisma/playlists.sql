TRUNCATE TABLE playlists CASCADE;
DO $$
DECLARE
    seq_name TEXT;
BEGIN
    SELECT pg_get_serial_sequence('playlists', 'id') INTO seq_name;
    EXECUTE 'ALTER SEQUENCE ' || seq_name || ' RESTART WITH 1';
END
$$;
INSERT INTO playlists (id, name) VALUES (1,'Music');
INSERT INTO playlists (id, name) VALUES (2,'Movies');
INSERT INTO playlists (id, name) VALUES (3,'TV Shows');
INSERT INTO playlists (id, name) VALUES (4,'Audiobooks');
INSERT INTO playlists (id, name) VALUES (5,'90’s Music');
INSERT INTO playlists (id, name) VALUES (6,'Audiobooks');
INSERT INTO playlists (id, name) VALUES (7,'Movies');
INSERT INTO playlists (id, name) VALUES (8,'Music');
INSERT INTO playlists (id, name) VALUES (9,'Music Videos');
INSERT INTO playlists (id, name) VALUES (10,'TV Shows');
INSERT INTO playlists (id, name) VALUES (11,'Brazilian Music');
INSERT INTO playlists (id, name) VALUES (12,'Classical');
INSERT INTO playlists (id, name) VALUES (13,'Classical 101 - Deep Cuts');
INSERT INTO playlists (id, name) VALUES (14,'Classical 101 - Next Steps');
INSERT INTO playlists (id, name) VALUES (15,'Classical 101 - The Basics');
INSERT INTO playlists (id, name) VALUES (16,'Grunge');
INSERT INTO playlists (id, name) VALUES (17,'Heavy Metal Classic');
INSERT INTO playlists (id, name) VALUES (18,'On-The-Go 1');
--- update sequence on table playlists
SELECT setval(pg_get_serial_sequence('playlists', 'id'), coalesce(max(id)+1, 1), false) FROM playlists;
