CREATE OR REPLACE FUNCTION compare_phone_numbers(phone1 TEXT, phone2 TEXT)
RETURNS FLOAT AS $$
DECLARE
    similarity_score FLOAT;
DECLARE
    normalized_phone1 TEXT := regexp_replace(phone1, '\\D', '', 'g'); -- Remove non-numeric characters
    normalized_phone2 TEXT := regexp_replace(phone2, '\\D', '', 'g'); -- Remove non-numeric characters
BEGIN
    -- Exact match
    IF normalized_phone1 = normalized_phone2 THEN
        RETURN 100.0;
    END IF;

    -- Use Jaro-Winkler similarity for partial matches
    similarity_score :=  similarity(normalized_phone1, normalized_phone2);
	RETURN round(similarity_score::NUMERIC * 100, 2);
END;
$$ LANGUAGE plpgsql;