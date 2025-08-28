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

--
-- Name: OrganizationIdentifierTypeEnum; Type: TYPE; Schema: public; Owner: dash_user
--

CREATE TYPE public."OrganizationIdentifierTypeEnum" AS ENUM (
    'ror',
    'gcmd'
);


ALTER TYPE public."OrganizationIdentifierTypeEnum" OWNER TO dash_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Address; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."Address" (
    id integer NOT NULL,
    city text,
    administrative_area text,
    postal_code text,
    country text,
    "ContactInformation_id" integer
);


ALTER TABLE public."Address" OWNER TO dash_user;

--
-- Name: Address_delivery_points; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."Address_delivery_points" (
    "Address_id" integer NOT NULL,
    delivery_points text NOT NULL
);


ALTER TABLE public."Address_delivery_points" OWNER TO dash_user;

--
-- Name: Address_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."Address_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Address_id_seq" OWNER TO dash_user;

--
-- Name: Address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."Address_id_seq" OWNED BY public."Address".id;


--
-- Name: ContactInformation; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."ContactInformation" (
    id integer NOT NULL,
    phone text,
    email text,
    link text,
    "Person_id" integer
);


ALTER TABLE public."ContactInformation" OWNER TO dash_user;

--
-- Name: ContactInformation_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."ContactInformation_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ContactInformation_id_seq" OWNER TO dash_user;

--
-- Name: ContactInformation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."ContactInformation_id_seq" OWNED BY public."ContactInformation".id;


--
-- Name: DashboardUser; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."DashboardUser" (
    id integer NOT NULL,
    active boolean,
    email text
);


ALTER TABLE public."DashboardUser" OWNER TO dash_user;

--
-- Name: DashboardUser_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."DashboardUser_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."DashboardUser_id_seq" OWNER TO dash_user;

--
-- Name: DashboardUser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."DashboardUser_id_seq" OWNED BY public."DashboardUser".id;


--
-- Name: File; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."File" (
    id integer NOT NULL,
    filename text,
    category text,
    mime text,
    created timestamp without time zone,
    modified timestamp without time zone,
    "Submission_id" integer
);


ALTER TABLE public."File" OWNER TO dash_user;

--
-- Name: File_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."File_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."File_id_seq" OWNER TO dash_user;

--
-- Name: File_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."File_id_seq" OWNED BY public."File".id;


--
-- Name: MetadataRole; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."MetadataRole" (
    id integer NOT NULL,
    name text
);


ALTER TABLE public."MetadataRole" OWNER TO dash_user;

--
-- Name: MetadataRole_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."MetadataRole_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."MetadataRole_id_seq" OWNER TO dash_user;

--
-- Name: MetadataRole_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."MetadataRole_id_seq" OWNED BY public."MetadataRole".id;


--
-- Name: OadsMetadata; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."OadsMetadata" (
    id integer NOT NULL,
    title text,
    submission_date timestamp without time zone,
    abstract text,
    use_limitation text,
    purpose text,
    data_license text,
    "Submission_id" integer
);


ALTER TABLE public."OadsMetadata" OWNER TO dash_user;

--
-- Name: OadsMetadata_data_submitters; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."OadsMetadata_data_submitters" (
    "OadsMetadata_id" integer NOT NULL,
    data_submitters_id integer NOT NULL
);


ALTER TABLE public."OadsMetadata_data_submitters" OWNER TO dash_user;

--
-- Name: OadsMetadata_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."OadsMetadata_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."OadsMetadata_id_seq" OWNER TO dash_user;

--
-- Name: OadsMetadata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."OadsMetadata_id_seq" OWNED BY public."OadsMetadata".id;


--
-- Name: OadsMetadata_investigators; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."OadsMetadata_investigators" (
    "OadsMetadata_id" integer NOT NULL,
    investigators_id integer NOT NULL
);


ALTER TABLE public."OadsMetadata_investigators" OWNER TO dash_user;

--
-- Name: Organization; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."Organization" (
    id integer NOT NULL,
    name text,
    organization_identifier text,
    organization_identifier_type public."OrganizationIdentifierTypeEnum",
    "Person_id" integer
);


ALTER TABLE public."Organization" OWNER TO dash_user;

--
-- Name: Organization_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."Organization_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Organization_id_seq" OWNER TO dash_user;

--
-- Name: Organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."Organization_id_seq" OWNED BY public."Organization".id;


--
-- Name: Person; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."Person" (
    id integer NOT NULL,
    title text,
    first_name text NOT NULL,
    last_name text NOT NULL,
    "DashboardUser_id" integer
);


ALTER TABLE public."Person" OWNER TO dash_user;

--
-- Name: Person_data_submitter_person; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."Person_data_submitter_person" (
    "Person_id" integer NOT NULL,
    data_submitter_person_id integer NOT NULL
);


ALTER TABLE public."Person_data_submitter_person" OWNER TO dash_user;

--
-- Name: Person_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."Person_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Person_id_seq" OWNER TO dash_user;

--
-- Name: Person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."Person_id_seq" OWNED BY public."Person".id;


--
-- Name: Person_metadata_role; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."Person_metadata_role" (
    "Person_id" integer NOT NULL,
    metadata_role_id integer NOT NULL
);


ALTER TABLE public."Person_metadata_role" OWNER TO dash_user;

--
-- Name: RelatedDataset; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."RelatedDataset" (
    id integer NOT NULL,
    dataset text,
    link text,
    "OadsMetadata_id" integer
);


ALTER TABLE public."RelatedDataset" OWNER TO dash_user;

--
-- Name: RelatedDataset_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."RelatedDataset_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."RelatedDataset_id_seq" OWNER TO dash_user;

--
-- Name: RelatedDataset_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."RelatedDataset_id_seq" OWNED BY public."RelatedDataset".id;


--
-- Name: ResearchOrganization; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."ResearchOrganization" (
    id integer NOT NULL,
    url text,
    display_name text
);


ALTER TABLE public."ResearchOrganization" OWNER TO dash_user;

--
-- Name: ResearchOrganization_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."ResearchOrganization_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ResearchOrganization_id_seq" OWNER TO dash_user;

--
-- Name: ResearchOrganization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."ResearchOrganization_id_seq" OWNED BY public."ResearchOrganization".id;


--
-- Name: Submission; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public."Submission" (
    id integer NOT NULL,
    submitted_to_ncei boolean,
    date_submitted_to_ncei timestamp without time zone,
    created timestamp without time zone,
    modified timestamp without time zone,
    "DashboardUser_id" integer
);


ALTER TABLE public."Submission" OWNER TO dash_user;

--
-- Name: Submission_id_seq; Type: SEQUENCE; Schema: public; Owner: dash_user
--

CREATE SEQUENCE public."Submission_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Submission_id_seq" OWNER TO dash_user;

--
-- Name: Submission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dash_user
--

ALTER SEQUENCE public."Submission_id_seq" OWNED BY public."Submission".id;


--
-- Name: Address id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Address" ALTER COLUMN id SET DEFAULT nextval('public."Address_id_seq"'::regclass);


--
-- Name: ContactInformation id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."ContactInformation" ALTER COLUMN id SET DEFAULT nextval('public."ContactInformation_id_seq"'::regclass);


--
-- Name: DashboardUser id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."DashboardUser" ALTER COLUMN id SET DEFAULT nextval('public."DashboardUser_id_seq"'::regclass);


--
-- Name: File id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."File" ALTER COLUMN id SET DEFAULT nextval('public."File_id_seq"'::regclass);


--
-- Name: MetadataRole id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."MetadataRole" ALTER COLUMN id SET DEFAULT nextval('public."MetadataRole_id_seq"'::regclass);


--
-- Name: OadsMetadata id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata" ALTER COLUMN id SET DEFAULT nextval('public."OadsMetadata_id_seq"'::regclass);


--
-- Name: Organization id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Organization" ALTER COLUMN id SET DEFAULT nextval('public."Organization_id_seq"'::regclass);


--
-- Name: Person id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person" ALTER COLUMN id SET DEFAULT nextval('public."Person_id_seq"'::regclass);


--
-- Name: RelatedDataset id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."RelatedDataset" ALTER COLUMN id SET DEFAULT nextval('public."RelatedDataset_id_seq"'::regclass);


--
-- Name: ResearchOrganization id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."ResearchOrganization" ALTER COLUMN id SET DEFAULT nextval('public."ResearchOrganization_id_seq"'::regclass);


--
-- Name: Submission id; Type: DEFAULT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Submission" ALTER COLUMN id SET DEFAULT nextval('public."Submission_id_seq"'::regclass);


--
-- Name: Address_delivery_points Address_delivery_points_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Address_delivery_points"
    ADD CONSTRAINT "Address_delivery_points_pkey" PRIMARY KEY ("Address_id", delivery_points);


--
-- Name: Address Address_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Address"
    ADD CONSTRAINT "Address_pkey" PRIMARY KEY (id);


--
-- Name: ContactInformation ContactInformation_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."ContactInformation"
    ADD CONSTRAINT "ContactInformation_pkey" PRIMARY KEY (id);


--
-- Name: DashboardUser DashboardUser_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."DashboardUser"
    ADD CONSTRAINT "DashboardUser_pkey" PRIMARY KEY (id);


--
-- Name: File File_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."File"
    ADD CONSTRAINT "File_pkey" PRIMARY KEY (id);


--
-- Name: MetadataRole MetadataRole_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."MetadataRole"
    ADD CONSTRAINT "MetadataRole_pkey" PRIMARY KEY (id);


--
-- Name: OadsMetadata_data_submitters OadsMetadata_data_submitters_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata_data_submitters"
    ADD CONSTRAINT "OadsMetadata_data_submitters_pkey" PRIMARY KEY ("OadsMetadata_id", data_submitters_id);


--
-- Name: OadsMetadata_investigators OadsMetadata_investigators_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata_investigators"
    ADD CONSTRAINT "OadsMetadata_investigators_pkey" PRIMARY KEY ("OadsMetadata_id", investigators_id);


--
-- Name: OadsMetadata OadsMetadata_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata"
    ADD CONSTRAINT "OadsMetadata_pkey" PRIMARY KEY (id);


--
-- Name: Organization Organization_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Organization"
    ADD CONSTRAINT "Organization_pkey" PRIMARY KEY (id);


--
-- Name: Person_data_submitter_person Person_data_submitter_person_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person_data_submitter_person"
    ADD CONSTRAINT "Person_data_submitter_person_pkey" PRIMARY KEY ("Person_id", data_submitter_person_id);


--
-- Name: Person_metadata_role Person_metadata_role_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person_metadata_role"
    ADD CONSTRAINT "Person_metadata_role_pkey" PRIMARY KEY ("Person_id", metadata_role_id);


--
-- Name: Person Person_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person"
    ADD CONSTRAINT "Person_pkey" PRIMARY KEY (id);


--
-- Name: RelatedDataset RelatedDataset_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."RelatedDataset"
    ADD CONSTRAINT "RelatedDataset_pkey" PRIMARY KEY (id);


--
-- Name: ResearchOrganization ResearchOrganization_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."ResearchOrganization"
    ADD CONSTRAINT "ResearchOrganization_pkey" PRIMARY KEY (id);


--
-- Name: Submission Submission_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Submission"
    ADD CONSTRAINT "Submission_pkey" PRIMARY KEY (id);


--
-- Name: Address Address_ContactInformation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Address"
    ADD CONSTRAINT "Address_ContactInformation_id_fkey" FOREIGN KEY ("ContactInformation_id") REFERENCES public."ContactInformation"(id);


--
-- Name: Address_delivery_points Address_delivery_points_Address_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Address_delivery_points"
    ADD CONSTRAINT "Address_delivery_points_Address_id_fkey" FOREIGN KEY ("Address_id") REFERENCES public."Address"(id);


--
-- Name: ContactInformation ContactInformation_Person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."ContactInformation"
    ADD CONSTRAINT "ContactInformation_Person_id_fkey" FOREIGN KEY ("Person_id") REFERENCES public."Person"(id);


--
-- Name: File File_Submission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."File"
    ADD CONSTRAINT "File_Submission_id_fkey" FOREIGN KEY ("Submission_id") REFERENCES public."Submission"(id);


--
-- Name: OadsMetadata OadsMetadata_Submission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata"
    ADD CONSTRAINT "OadsMetadata_Submission_id_fkey" FOREIGN KEY ("Submission_id") REFERENCES public."Submission"(id);


--
-- Name: OadsMetadata_data_submitters OadsMetadata_data_submitters_OadsMetadata_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata_data_submitters"
    ADD CONSTRAINT "OadsMetadata_data_submitters_OadsMetadata_id_fkey" FOREIGN KEY ("OadsMetadata_id") REFERENCES public."OadsMetadata"(id);


--
-- Name: OadsMetadata_data_submitters OadsMetadata_data_submitters_data_submitters_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata_data_submitters"
    ADD CONSTRAINT "OadsMetadata_data_submitters_data_submitters_id_fkey" FOREIGN KEY (data_submitters_id) REFERENCES public."Person"(id);


--
-- Name: OadsMetadata_investigators OadsMetadata_investigators_OadsMetadata_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata_investigators"
    ADD CONSTRAINT "OadsMetadata_investigators_OadsMetadata_id_fkey" FOREIGN KEY ("OadsMetadata_id") REFERENCES public."OadsMetadata"(id);


--
-- Name: OadsMetadata_investigators OadsMetadata_investigators_investigators_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."OadsMetadata_investigators"
    ADD CONSTRAINT "OadsMetadata_investigators_investigators_id_fkey" FOREIGN KEY (investigators_id) REFERENCES public."Person"(id);


--
-- Name: Organization Organization_Person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Organization"
    ADD CONSTRAINT "Organization_Person_id_fkey" FOREIGN KEY ("Person_id") REFERENCES public."Person"(id);


--
-- Name: Person Person_DashboardUser_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person"
    ADD CONSTRAINT "Person_DashboardUser_id_fkey" FOREIGN KEY ("DashboardUser_id") REFERENCES public."DashboardUser"(id);


--
-- Name: Person_data_submitter_person Person_data_submitter_person_Person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person_data_submitter_person"
    ADD CONSTRAINT "Person_data_submitter_person_Person_id_fkey" FOREIGN KEY ("Person_id") REFERENCES public."Person"(id);


--
-- Name: Person_data_submitter_person Person_data_submitter_person_data_submitter_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person_data_submitter_person"
    ADD CONSTRAINT "Person_data_submitter_person_data_submitter_person_id_fkey" FOREIGN KEY (data_submitter_person_id) REFERENCES public."OadsMetadata"(id);


--
-- Name: Person_metadata_role Person_metadata_role_Person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person_metadata_role"
    ADD CONSTRAINT "Person_metadata_role_Person_id_fkey" FOREIGN KEY ("Person_id") REFERENCES public."Person"(id);


--
-- Name: Person_metadata_role Person_metadata_role_metadata_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Person_metadata_role"
    ADD CONSTRAINT "Person_metadata_role_metadata_role_id_fkey" FOREIGN KEY (metadata_role_id) REFERENCES public."MetadataRole"(id);


--
-- Name: RelatedDataset RelatedDataset_OadsMetadata_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."RelatedDataset"
    ADD CONSTRAINT "RelatedDataset_OadsMetadata_id_fkey" FOREIGN KEY ("OadsMetadata_id") REFERENCES public."OadsMetadata"(id);


--
-- Name: Submission Submission_DashboardUser_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public."Submission"
    ADD CONSTRAINT "Submission_DashboardUser_id_fkey" FOREIGN KEY ("DashboardUser_id") REFERENCES public."DashboardUser"(id);


--
-- PostgreSQL database dump complete
--

