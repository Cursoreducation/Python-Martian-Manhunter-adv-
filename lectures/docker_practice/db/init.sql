
CREATE DATABASE knights;
use knights;

CREATE TABLE kingdom_colors (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO kingdom_colors
  (name, color)
VALUES
  ('London', 'Green'),
  ('Berlin', 'Orange');