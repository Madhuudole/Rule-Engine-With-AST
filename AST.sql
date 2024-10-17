CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

CREATE TABLE ast_nodes (
    id SERIAL PRIMARY KEY,
    rule_id INT REFERENCES rules(id),
    node_type VARCHAR(10),
    left_child INT REFERENCES ast_nodes(id),
    right_child INT REFERENCES ast_nodes(id),
    value VARCHAR(255)
);
