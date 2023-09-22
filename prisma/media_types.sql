TRUNCATE TABLE media_types CASCADE;
DO $$
DECLARE
    seq_name TEXT;
BEGIN
    SELECT pg_get_serial_sequence('media_types', 'id') INTO seq_name;
    EXECUTE 'ALTER SEQUENCE ' || seq_name || ' RESTART WITH 1';
END
$$;
INSERT INTO media_types (id, name) VALUES (1,'MPEG audio file');
INSERT INTO media_types (id, name) VALUES (2,'Protected AAC audio file');
INSERT INTO media_types (id, name) VALUES (3,'Protected MPEG-4 video file');
INSERT INTO media_types (id, name) VALUES (4,'Purchased AAC audio file');
INSERT INTO media_types (id, name) VALUES (5,'AAC audio file');
--- update sequence on table media_types
SELECT setval(pg_get_serial_sequence('media_types', 'id'), coalesce(max(id)+1, 1), false) FROM media_types;
