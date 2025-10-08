--
-- PostgreSQL database dump
--

\restrict anH1NESiLQ2ExmbBaS9hqPtvpfgjzs9xXYiolgpZNj684TjPvp9GlEdWBV01NHj

-- Dumped from database version 14.12 (Debian 14.12-1.pgdg120+1)
-- Dumped by pg_dump version 14.19 (Ubuntu 14.19-0ubuntu0.22.04.1)

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
-- Name: co2_autonomous; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.co2_autonomous (
    id uuid NOT NULL,
    "locationSeawaterIntake" character varying,
    "depthSeawaterIntake" character varying,
    equilibrator character varying,
    "gasDetector" character varying,
    "waterVaporCorrection" character varying,
    "temperatureCorrectionMethod" character varying,
    "co2ReportTemperature" character varying
);


ALTER TABLE public.co2_autonomous OWNER TO dash_user;

--
-- Name: co2_discrete; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.co2_discrete (
    id uuid NOT NULL,
    "storageMethod" character varying,
    "seawaterVolume" character varying,
    "headspaceVolume" character varying,
    "measurementTemperature" character varying,
    "gasDetector" character varying,
    "waterVaporCorrection" character varying,
    "temperatureCorrectionMethod" character varying,
    "co2ReportTemperature" character varying
);


ALTER TABLE public.co2_discrete OWNER TO dash_user;

--
-- Name: co2_variable; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.co2_variable (
    id uuid NOT NULL,
    "gasDetector" character varying,
    "waterVaporCorrection" character varying,
    "temperatureCorrectionMethod" character varying,
    "co2ReportTemperature" character varying
);


ALTER TABLE public.co2_variable OWNER TO dash_user;

--
-- Name: metadata; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.metadata (
    id uuid NOT NULL
);


ALTER TABLE public.metadata OWNER TO dash_user;

--
-- Name: metadata_document; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.metadata_document (
    id uuid NOT NULL,
    submit_time timestamp without time zone,
    responsible_party_id uuid NOT NULL,
    data_submitter_id uuid NOT NULL
);


ALTER TABLE public.metadata_document OWNER TO dash_user;

--
-- Name: organization_instance; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.organization_instance (
    id uuid NOT NULL,
    name character varying,
    description character varying,
    metadata_document_id uuid,
    "PID" character varying,
    object_id character varying
);


ALTER TABLE public.organization_instance OWNER TO dash_user;

--
-- Name: organization_ref; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.organization_ref (
    id uuid NOT NULL,
    description character varying,
    role character varying,
    object_id character varying
);


ALTER TABLE public.organization_ref OWNER TO dash_user;

--
-- Name: person_instance; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.person_instance (
    id uuid NOT NULL,
    first_name character varying,
    last_name character varying,
    address character varying,
    organization_id uuid NOT NULL,
    metadata_document_id uuid,
    "PID" character varying,
    object_id character varying
);


ALTER TABLE public.person_instance OWNER TO dash_user;

--
-- Name: person_ref; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.person_ref (
    id uuid NOT NULL,
    metadata_document_id uuid,
    description character varying,
    role character varying,
    object_id character varying
);


ALTER TABLE public.person_ref OWNER TO dash_user;

--
-- Name: ph_variable; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.ph_variable (
    id uuid NOT NULL,
    "phScale" character varying,
    measurement_temperature character varying,
    temperature_correction_method character varying,
    ph_report_temperature character varying
);


ALTER TABLE public.ph_variable OWNER TO dash_user;

--
-- Name: ta_variable; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.ta_variable (
    id uuid NOT NULL,
    "cellType" character varying,
    "curveFitting" character varying,
    "blankCorrection" character varying
);


ALTER TABLE public.ta_variable OWNER TO dash_user;

--
-- Name: variable; Type: TABLE; Schema: public; Owner: dash_user
--

CREATE TABLE public.variable (
    id uuid NOT NULL,
    name character varying,
    standard_name character varying,
    description character varying,
    dataset_variable_name character varying,
    units character varying,
    metadata_document_id uuid,
    variable_type character varying NOT NULL
);


ALTER TABLE public.variable OWNER TO dash_user;

--
-- Name: co2_autonomous co2_autonomous_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.co2_autonomous
    ADD CONSTRAINT co2_autonomous_pkey PRIMARY KEY (id);


--
-- Name: co2_discrete co2_discrete_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.co2_discrete
    ADD CONSTRAINT co2_discrete_pkey PRIMARY KEY (id);


--
-- Name: co2_variable co2_variable_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.co2_variable
    ADD CONSTRAINT co2_variable_pkey PRIMARY KEY (id);


--
-- Name: metadata_document metadata_document_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.metadata_document
    ADD CONSTRAINT metadata_document_pkey PRIMARY KEY (id);


--
-- Name: metadata metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT metadata_pkey PRIMARY KEY (id);


--
-- Name: organization_instance organization_instance_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.organization_instance
    ADD CONSTRAINT organization_instance_pkey PRIMARY KEY (id);


--
-- Name: organization_ref organization_ref_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.organization_ref
    ADD CONSTRAINT organization_ref_pkey PRIMARY KEY (id);


--
-- Name: person_instance person_instance_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_instance
    ADD CONSTRAINT person_instance_pkey PRIMARY KEY (id);


--
-- Name: person_ref person_ref_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_ref
    ADD CONSTRAINT person_ref_pkey PRIMARY KEY (id);


--
-- Name: ph_variable ph_variable_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.ph_variable
    ADD CONSTRAINT ph_variable_pkey PRIMARY KEY (id);


--
-- Name: ta_variable ta_variable_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.ta_variable
    ADD CONSTRAINT ta_variable_pkey PRIMARY KEY (id);


--
-- Name: variable variable_pkey; Type: CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.variable
    ADD CONSTRAINT variable_pkey PRIMARY KEY (id);


--
-- Name: co2_autonomous co2_autonomous_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.co2_autonomous
    ADD CONSTRAINT co2_autonomous_id_fkey FOREIGN KEY (id) REFERENCES public.variable(id);


--
-- Name: co2_discrete co2_discrete_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.co2_discrete
    ADD CONSTRAINT co2_discrete_id_fkey FOREIGN KEY (id) REFERENCES public.variable(id);


--
-- Name: co2_variable co2_variable_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.co2_variable
    ADD CONSTRAINT co2_variable_id_fkey FOREIGN KEY (id) REFERENCES public.variable(id);


--
-- Name: metadata_document metadata_document_data_submitter_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.metadata_document
    ADD CONSTRAINT metadata_document_data_submitter_id_fkey FOREIGN KEY (data_submitter_id) REFERENCES public.person_ref(id);


--
-- Name: metadata_document metadata_document_responsible_party_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.metadata_document
    ADD CONSTRAINT metadata_document_responsible_party_id_fkey FOREIGN KEY (responsible_party_id) REFERENCES public.organization_ref(id);


--
-- Name: organization_instance organization_instance_metadata_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.organization_instance
    ADD CONSTRAINT organization_instance_metadata_document_id_fkey FOREIGN KEY (metadata_document_id) REFERENCES public.metadata_document(id);


--
-- Name: person_instance person_instance_metadata_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_instance
    ADD CONSTRAINT person_instance_metadata_document_id_fkey FOREIGN KEY (metadata_document_id) REFERENCES public.metadata_document(id);


--
-- Name: person_instance person_instance_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_instance
    ADD CONSTRAINT person_instance_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES public.organization_ref(id);


--
-- Name: person_ref person_ref_metadata_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.person_ref
    ADD CONSTRAINT person_ref_metadata_document_id_fkey FOREIGN KEY (metadata_document_id) REFERENCES public.metadata_document(id);


--
-- Name: ph_variable ph_variable_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.ph_variable
    ADD CONSTRAINT ph_variable_id_fkey FOREIGN KEY (id) REFERENCES public.variable(id);


--
-- Name: ta_variable ta_variable_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.ta_variable
    ADD CONSTRAINT ta_variable_id_fkey FOREIGN KEY (id) REFERENCES public.variable(id);


--
-- Name: variable variable_metadata_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dash_user
--

ALTER TABLE ONLY public.variable
    ADD CONSTRAINT variable_metadata_document_id_fkey FOREIGN KEY (metadata_document_id) REFERENCES public.metadata_document(id);


--
-- PostgreSQL database dump complete
--

\unrestrict anH1NESiLQ2ExmbBaS9hqPtvpfgjzs9xXYiolgpZNj684TjPvp9GlEdWBV01NHj

