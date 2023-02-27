CREATE TABLE if not EXISTS Source(
    id integer PRIMARY KEY autoincrement,
    name text not null
    CHECK(
        typeof("name") = "text" AND
        length("name") <= 25
    ),
    source_id INTEGER,
    FOREIGN key (source_id) REFERENCES Source(id) on DELETE set null
);

CREATE table Task(
	id integer PRIMARY KEY autoincrement,
	name text not null
	CHECK(
        typeof("name") = "text" AND
        length("name") <= 25
    ),
	description text not null,
	deadline date,
	hard_deadline int not null default 0,
	source_id integer,
	FOREIGN key (source_id) REFERENCES Source(id) on DELETE set null
)