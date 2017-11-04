--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.2
-- Dumped by pg_dump version 9.6.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: problems; Type: TABLE; Schema: public; Owner: tdobbins
--

CREATE TABLE problems (
    id integer NOT NULL,
    term1 integer,
    term2 integer,
    answer integer,
    submitted_answer integer,
    grade integer,
    operation character varying(60),
    dateof bigint
);


ALTER TABLE problems OWNER TO tdobbins;

--
-- Name: problems_id_seq; Type: SEQUENCE; Schema: public; Owner: tdobbins
--

CREATE SEQUENCE problems_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE problems_id_seq OWNER TO tdobbins;

--
-- Name: problems_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tdobbins
--

ALTER SEQUENCE problems_id_seq OWNED BY problems.id;


--
-- Name: problems id; Type: DEFAULT; Schema: public; Owner: tdobbins
--

ALTER TABLE ONLY problems ALTER COLUMN id SET DEFAULT nextval('problems_id_seq'::regclass);


--
-- Name: problems problems_pkey; Type: CONSTRAINT; Schema: public; Owner: tdobbins
--

ALTER TABLE ONLY problems
    ADD CONSTRAINT problems_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--