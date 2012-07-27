-- DB name: EleccionesPeru

CREATE SCHEMA congreso_2011;

CREATE TYPE place_type AS ENUM ( 'mesa', 'centro de votacion', 'distrito', 'provincia', 'region');

CREATE TABLE congreso_2011.post_codes (
       id    SERIAL PRIMARY KEY,
       name  text NOT NULL,
       post_code text NOT NULL,
       localidad place_type NOT NULL,
       parent integer,
       FOREIGN KEY (parent) REFERENCES congreso_2011.post_codes(id)
);

INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Amazonas', '010000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Ancash', '020000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Apurimac', '030000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Arequipa', '040000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Ayacucho', '050000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Cajamarca', '060000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Callao', '240000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Cusco', '070000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Huancavelica', '080000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Huanuco', '090000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Ica', '100000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Junin', '110000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('La Libertad', '120000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Lambayeque', '130000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Lima', '140000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Loreto', '150000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('La Libertad', '160000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Moquegua', '170000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Pasco', '180000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Piura', '190000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Puno', '200000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('San Martin', '210000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Tacna', '220000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Tumbes', '230000', 'region');
INSERT INTO congreso_2011.post_codes (name, post_code, localidad) VALUES ('Ucayali', '250000', 'region');


/*
CREATE TABLE congreso_2011.actas_electorales (
       numero_de_mesa integer,
       centro_votacion_id varchar(130),
       Estado del acta charac
       votos_totales integer,
       votos_validos integer,
       votos_blancos integer,
       votos_nulos integer,
);

CREATE TABLE voto_pormenorizado (
       party text,
       num_mesa text,
       1 integer,
       2
       3
       .
       .
       .
       36
)

*/
