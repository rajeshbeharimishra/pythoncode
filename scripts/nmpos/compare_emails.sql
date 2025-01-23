CREATE OR REPLACE FUNCTION compare_emails(email1 TEXT, email2 TEXT)
RETURNS FLOAT AS $$
DECLARE
    similarity_score FLOAT;
DECLARE
    normalized_email1 TEXT := lower(trim(email1));
    normalized_email2 TEXT := lower(trim(email2));
BEGIN
    -- Exact match
    IF normalized_email1 = normalized_email2 THEN
        RETURN 100.0;
    END IF;

    -- Use Jaro-Winkler similarity for partial matches
    similarity_score :=  similarity(normalized_email1, normalized_email2);
	RETURN round(similarity_score::NUMERIC * 100, 2);
END;
$$ LANGUAGE plpgsql;