CREATE TABLE IF NOT EXISTS 'emails_to_invite' (
    id TEXT PRIMARY KEY,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    phase TEXT NOT NULL,
    status INTEGER 
);