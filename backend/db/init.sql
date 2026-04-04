-- MCDA Local Database Initialisation
-- Run against a fresh PostgreSQL database:
--   psql -U postgres -d mcda -f backend/db/init.sql
--
-- All statements are idempotent (IF NOT EXISTS), so it is safe to re-run.

CREATE TABLE IF NOT EXISTS users (
    user_id     SERIAL          PRIMARY KEY,
    first_name  VARCHAR(35)     NOT NULL,
    last_name   VARCHAR(35)     NOT NULL,
    email       VARCHAR(255)    NOT NULL UNIQUE,
    password    VARCHAR(128)    NOT NULL,
    created_at  TIMESTAMP,
    updated_at  TIMESTAMP
);

CREATE TABLE IF NOT EXISTS projects (
    project_id      SERIAL          PRIMARY KEY,
    project_name    VARCHAR(70)     NOT NULL,
    visibility      BOOLEAN         NOT NULL,
    collaborators   TEXT[]          DEFAULT '{}',
    owner           INTEGER         NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    created_at      TIMESTAMP,
    updated_at      TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_projects_owner ON projects(owner);

CREATE TABLE IF NOT EXISTS tasks (
    task_id         SERIAL          PRIMARY KEY,
    task_name       VARCHAR(70)     NOT NULL,
    method          VARCHAR(70),
    decision_matrix BYTEA,
    project_id      INTEGER         NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    created_at      TIMESTAMP,
    updated_at      TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_tasks_project_id ON tasks(project_id);

CREATE TABLE IF NOT EXISTS criteria (
    criterion_id            SERIAL          PRIMARY KEY,
    criterion_name          VARCHAR(80)     NOT NULL,
    criterion_type          VARCHAR(80)     NOT NULL,
    min_max                 VARCHAR(3)      NOT NULL,
    alternatives_values     NUMERIC[],
    alternatives_values_raw NUMERIC[],
    description             VARCHAR(500),
    preference_function     VARCHAR(80),
    q_value                 NUMERIC,
    p_value                 NUMERIC,
    task_id                 INTEGER         NOT NULL REFERENCES tasks(task_id) ON DELETE CASCADE,
    created_at              TIMESTAMP,
    updated_at              TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_criteria_task_id ON criteria(task_id);

CREATE TABLE IF NOT EXISTS alternatives (
    alternative_id      SERIAL          PRIMARY KEY,
    alternative_name    VARCHAR(80)     NOT NULL,
    description         VARCHAR(500),
    task_id             INTEGER         NOT NULL REFERENCES tasks(task_id) ON DELETE CASCADE,
    created_at          TIMESTAMP,
    updated_at          TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_alternatives_task_id ON alternatives(task_id);

CREATE TABLE IF NOT EXISTS trade_offs (
    trade_off_id            SERIAL          PRIMARY KEY,
    criteria_weights        REAL[],
    criteria_weights_raw    NUMERIC[],
    decision_method         VARCHAR(80),
    normalization_method    VARCHAR(80),
    task_id                 INTEGER         NOT NULL REFERENCES tasks(task_id) ON DELETE CASCADE,
    created_at              TIMESTAMP,
    updated_at              TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_trade_offs_task_id ON trade_offs(task_id);

CREATE TABLE IF NOT EXISTS decision_matrix (
    matrix_id               SERIAL          PRIMARY KEY,
    criteria                INTEGER[],
    alternatives            INTEGER[],
    normalization_method    VARCHAR(80),
    created_at              TIMESTAMP,
    updated_at              TIMESTAMP
);
