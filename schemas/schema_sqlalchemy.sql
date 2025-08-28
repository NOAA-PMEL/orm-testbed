--
-- PostgreSQL database dump
--

-- Dumped from database version 14.12 (Debian 14.12-1.pgdg120+1)
-- Dumped by pg_dump version 14.18 (Ubuntu 14.18-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: address; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.address (
    id integer NOT NULL,
    delivery_points character varying[],
    city character varying,
    administrative_area character varying,
    postal_code character varying,
    country character varying,
    contact_information_id integer
);


ALTER TABLE public.address OWNER TO dash_user;

--
-- Name: address_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.address_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.address_id_seq OWNER TO dash_user;

--
-- Name: address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.address_id_seq OWNED BY public.address.id;


--
-- Name: contact_information; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.contact_information (
    id integer NOT NULL,
    phone character varying,
    email character varying NOT NULL,
    link character varying,
    person_id integer
);


ALTER TABLE public.contact_information OWNER TO dash_user;

--
-- Name: contact_information_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.contact_information_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contact_information_id_seq OWNER TO dash_user;

--
-- Name: contact_information_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.contact_information_id_seq OWNED BY public.contact_information.id;


--
-- Name: dashboard_user; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.dashboard_user (
    id integer NOT NULL,
    active boolean,
    email character varying NOT NULL
);


ALTER TABLE public.dashboard_user OWNER TO dash_user;

--
-- Name: dashboard_user_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.dashboard_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_user_id_seq OWNER TO dash_user;

--
-- Name: dashboard_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.dashboard_user_id_seq OWNED BY public.dashboard_user.id;


--
-- Name: dashboard_user_people; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.dashboard_user_people (
    dashboard_user_id integer NOT NULL,
    person_id integer NOT NULL
);


ALTER TABLE public.dashboard_user_people OWNER TO dash_user;

--
-- Name: file; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.file (
    id integer NOT NULL,
    filename character varying NOT NULL,
    category character varying NOT NULL,
    mime character varying NOT NULL,
    created timestamp without time zone DEFAULT now() NOT NULL,
    modified timestamp without time zone DEFAULT now() NOT NULL,
    submission_id integer NOT NULL
);


ALTER TABLE public.file OWNER TO dash_user;

--
-- Name: file_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.file_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.file_id_seq OWNER TO dash_user;

--
-- Name: file_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.file_id_seq OWNED BY public.file.id;


--
-- Name: metadata_role; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.metadata_role (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.metadata_role OWNER TO dash_user;

--
-- Name: metadata_role_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.metadata_role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.metadata_role_id_seq OWNER TO dash_user;

--
-- Name: metadata_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.metadata_role_id_seq OWNED BY public.metadata_role.id;


--
-- Name: oads_metadata; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.oads_metadata (
    id integer NOT NULL,
    submission_date timestamp without time zone,
    title character varying NOT NULL,
    abstract character varying NOT NULL,
    use_limitation character varying,
    purpose character varying,
    data_license character varying NOT NULL,
    submission_id integer NOT NULL
);


ALTER TABLE public.oads_metadata OWNER TO dash_user;

--
-- Name: oads_metadata_data_submitter; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.oads_metadata_data_submitter (
    oads_metadata_id integer NOT NULL,
    person_id integer NOT NULL
);


ALTER TABLE public.oads_metadata_data_submitter OWNER TO dash_user;

--
-- Name: oads_metadata_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.oads_metadata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oads_metadata_id_seq OWNER TO dash_user;

--
-- Name: oads_metadata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.oads_metadata_id_seq OWNED BY public.oads_metadata.id;


--
-- Name: oads_metadata_investigators; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.oads_metadata_investigators (
    oads_metadata_id integer NOT NULL,
    person_id integer NOT NULL
);


ALTER TABLE public.oads_metadata_investigators OWNER TO dash_user;

--
-- Name: organization; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.organization (
    id integer NOT NULL,
    ror_id character varying,
    name character varying NOT NULL,
    person_id integer
);


ALTER TABLE public.organization OWNER TO dash_user;

--
-- Name: organization_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organization_id_seq OWNER TO dash_user;

--
-- Name: organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.organization_id_seq OWNED BY public.organization.id;


--
-- Name: person; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.person (
    id integer NOT NULL,
    title character varying,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL
);


ALTER TABLE public.person OWNER TO dash_user;

--
-- Name: person_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.person_id_seq OWNER TO dash_user;

--
-- Name: person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.person_id_seq OWNED BY public.person.id;


--
-- Name: person_metadata_roles; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.person_metadata_roles (
    person_id integer NOT NULL,
    role_id integer NOT NULL
);


ALTER TABLE public.person_metadata_roles OWNER TO dash_user;

--
-- Name: related_dataset; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.related_dataset (
    id integer NOT NULL,
    dataset character varying NOT NULL,
    link character varying NOT NULL,
    oads_metadata_id integer
);


ALTER TABLE public.related_dataset OWNER TO dash_user;

--
-- Name: related_dataset_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.related_dataset_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.related_dataset_id_seq OWNER TO dash_user;

--
-- Name: related_dataset_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.related_dataset_id_seq OWNED BY public.related_dataset.id;


--
-- Name: research_organization; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.research_organization (
    id character varying NOT NULL,
    display_name character varying NOT NULL
);


ALTER TABLE public.research_organization OWNER TO dash_user;

--
-- Name: submission; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.submission (
    id integer NOT NULL,
    submitted_to_ncei boolean,
    date_submitted_to_ncei timestamp without time zone,
    created timestamp without time zone DEFAULT now() NOT NULL,
    modified timestamp without time zone DEFAULT now() NOT NULL,
    dashboard_user_id integer NOT NULL
);


ALTER TABLE public.submission OWNER TO dash_user;

--
-- Name: submission_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public.submission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.submission_id_seq OWNER TO dash_user;

--
-- Name: submission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public.submission_id_seq OWNED BY public.submission.id;


--
-- Name: address id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.address ALTER COLUMN id SET DEFAULT nextval('public.address_id_seq'::regclass);


--
-- Name: contact_information id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.contact_information ALTER COLUMN id SET DEFAULT nextval('public.contact_information_id_seq'::regclass);


--
-- Name: dashboard_user id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.dashboard_user ALTER COLUMN id SET DEFAULT nextval('public.dashboard_user_id_seq'::regclass);


--
-- Name: file id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.file ALTER COLUMN id SET DEFAULT nextval('public.file_id_seq'::regclass);


--
-- Name: metadata_role id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.metadata_role ALTER COLUMN id SET DEFAULT nextval('public.metadata_role_id_seq'::regclass);


--
-- Name: oads_metadata id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata ALTER COLUMN id SET DEFAULT nextval('public.oads_metadata_id_seq'::regclass);


--
-- Name: organization id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.organization ALTER COLUMN id SET DEFAULT nextval('public.organization_id_seq'::regclass);


--
-- Name: person id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person ALTER COLUMN id SET DEFAULT nextval('public.person_id_seq'::regclass);


--
-- Name: related_dataset id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.related_dataset ALTER COLUMN id SET DEFAULT nextval('public.related_dataset_id_seq'::regclass);


--
-- Name: submission id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.submission ALTER COLUMN id SET DEFAULT nextval('public.submission_id_seq'::regclass);


--
-- Name: address address_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (id);


--
-- Name: contact_information contact_information_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.contact_information
    ADD CONSTRAINT contact_information_pkey PRIMARY KEY (id);


--
-- Name: dashboard_user_people dashboard_user_people_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.dashboard_user_people
    ADD CONSTRAINT dashboard_user_people_pkey PRIMARY KEY (dashboard_user_id, person_id);


--
-- Name: dashboard_user dashboard_user_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.dashboard_user
    ADD CONSTRAINT dashboard_user_pkey PRIMARY KEY (id);


--
-- Name: file file_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.file
    ADD CONSTRAINT file_pkey PRIMARY KEY (id);


--
-- Name: metadata_role metadata_role_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.metadata_role
    ADD CONSTRAINT metadata_role_pkey PRIMARY KEY (id);


--
-- Name: oads_metadata_data_submitter oads_metadata_data_submitter_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata_data_submitter
    ADD CONSTRAINT oads_metadata_data_submitter_pkey PRIMARY KEY (oads_metadata_id, person_id);


--
-- Name: oads_metadata_investigators oads_metadata_investigators_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata_investigators
    ADD CONSTRAINT oads_metadata_investigators_pkey PRIMARY KEY (oads_metadata_id, person_id);


--
-- Name: oads_metadata oads_metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata
    ADD CONSTRAINT oads_metadata_pkey PRIMARY KEY (id);


--
-- Name: organization organization_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (id);


--
-- Name: person_metadata_roles person_metadata_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_metadata_roles
    ADD CONSTRAINT person_metadata_roles_pkey PRIMARY KEY (person_id, role_id);


--
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id);


--
-- Name: related_dataset related_dataset_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.related_dataset
    ADD CONSTRAINT related_dataset_pkey PRIMARY KEY (id);


--
-- Name: research_organization research_organization_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.research_organization
    ADD CONSTRAINT research_organization_pkey PRIMARY KEY (id);


--
-- Name: submission submission_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.submission
    ADD CONSTRAINT submission_pkey PRIMARY KEY (id);


--
-- Name: address address_contact_information_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_contact_information_id_fkey FOREIGN KEY (contact_information_id) REFERENCES public.contact_information(id);


--
-- Name: contact_information contact_information_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.contact_information
    ADD CONSTRAINT contact_information_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- Name: dashboard_user_people dashboard_user_people_dashboard_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.dashboard_user_people
    ADD CONSTRAINT dashboard_user_people_dashboard_user_id_fkey FOREIGN KEY (dashboard_user_id) REFERENCES public.dashboard_user(id);


--
-- Name: dashboard_user_people dashboard_user_people_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.dashboard_user_people
    ADD CONSTRAINT dashboard_user_people_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- Name: file file_submission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.file
    ADD CONSTRAINT file_submission_id_fkey FOREIGN KEY (submission_id) REFERENCES public.submission(id);


--
-- Name: oads_metadata_data_submitter oads_metadata_data_submitter_oads_metadata_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata_data_submitter
    ADD CONSTRAINT oads_metadata_data_submitter_oads_metadata_id_fkey FOREIGN KEY (oads_metadata_id) REFERENCES public.oads_metadata(id);


--
-- Name: oads_metadata_data_submitter oads_metadata_data_submitter_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata_data_submitter
    ADD CONSTRAINT oads_metadata_data_submitter_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- Name: oads_metadata_investigators oads_metadata_investigators_oads_metadata_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata_investigators
    ADD CONSTRAINT oads_metadata_investigators_oads_metadata_id_fkey FOREIGN KEY (oads_metadata_id) REFERENCES public.oads_metadata(id);


--
-- Name: oads_metadata_investigators oads_metadata_investigators_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata_investigators
    ADD CONSTRAINT oads_metadata_investigators_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- Name: oads_metadata oads_metadata_submission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.oads_metadata
    ADD CONSTRAINT oads_metadata_submission_id_fkey FOREIGN KEY (submission_id) REFERENCES public.submission(id);


--
-- Name: organization organization_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- Name: person_metadata_roles person_metadata_roles_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_metadata_roles
    ADD CONSTRAINT person_metadata_roles_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- Name: person_metadata_roles person_metadata_roles_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_metadata_roles
    ADD CONSTRAINT person_metadata_roles_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.metadata_role(id);


--
-- Name: related_dataset related_dataset_oads_metadata_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.related_dataset
    ADD CONSTRAINT related_dataset_oads_metadata_id_fkey FOREIGN KEY (oads_metadata_id) REFERENCES public.oads_metadata(id);


--
-- Name: submission submission_dashboard_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.submission
    ADD CONSTRAINT submission_dashboard_user_id_fkey FOREIGN KEY (dashboard_user_id) REFERENCES public.dashboard_user(id);


--
-- PostgreSQL database dump complete
--

