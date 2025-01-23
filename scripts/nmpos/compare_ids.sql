CREATE OR REPLACE FUNCTION compare_ids(id1 TEXT, id2 TEXT)
RETURNS FLOAT AS $$
DECLARE
    combined_score FLOAT;
BEGIN
    -- Call the combined_similarity function
    combined_score := combined_similarity(id1, id2);

    -- Return the score rounded to 2 decimal places
    RETURN round(combined_score * 100, 2);
END;
$$ LANGUAGE plpgsql;