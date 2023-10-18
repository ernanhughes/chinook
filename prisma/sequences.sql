CREATE TEMPORARY TABLE kvstore (     
    table_name  TEXT PRIMARY KEY,
    pk_field  TEXT, 
    seq_name  TEXT,
    skip   BOOLEAN default false 
);

INSERT into kvstore values ('password_resets', '', '', TRUE); -- skip
INSERT into kvstore values ('permission_role', '', '', TRUE); -- skip 
INSERT into kvstore values ('role_user', '', '', TRUE); -- skip
INSERT into kvstore values ('another_table', 'id', 'custom_seq_name', FALSE); -- won't skip

DROP FUNCTION if exists alter_seq(text, text,text);
CREATE or REPLACE function alter_seq(table_name text, pk_field text, seq_name text) returns text as $$
DECLARE
  next_pk_value integer;
  q text;
BEGIN
  q := format('select coalesce(max(%s), 0) + 1 from "%s"', pk_field, table_name);
  EXECUTE q into next_pk_value;
  q := format('ALTER SEQUENCE %s RESTART WITH %s', seq_name, next_pk_value);
  EXECUTE q;
  RETURN q;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION if exists change_table_seq();
CREATE or REPLACE function change_table_seq() returns void as $$
DECLARE
  tbl text;
  q text;
  pk_field text;
  seq_name text;
  skip BOOLEAN;
BEGIN
  FOR tbl IN SELECT table_name FROM information_schema.tables WHERE  table_schema = 'public' ORDER  BY 1
  LOOP
    q := format('SELECT pk_field, seq_name, skip from kvstore where table_name = %L', tbl);
    EXECUTE q into pk_field, seq_name, skip;
    CONTINUE when skip = true;

    pk_field = COALESCE(pk_field, 'id');
    seq_name = COALESCE(seq_name, tbl || '_id_seq');
    PERFORM alter_seq(tbl, pk_field, seq_name);
    END LOOP;
END;
$$ LANGUAGE plpgsql;

select change_table_seq();
