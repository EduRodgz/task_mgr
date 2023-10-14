-- Create database table__
CREATE TABLE task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

--Generate dummy data--
INSERT INTO task (
    summary,
    description
) VALUES
    (
    "Do dishes",
    "Use dish soap and do the dishes."
    ),
    (
    "Feed dog",
    "Feed the dog some kibble."
    ),
    (
    "Wash car",
    "Refill gas and wash car."
    )
;
