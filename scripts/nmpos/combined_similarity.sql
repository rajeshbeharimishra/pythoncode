CREATE OR REPLACE FUNCTION combined_similarity(value1 TEXT, value2 TEXT)
RETURNS FLOAT AS $$
DECLARE
    normalized_value1 TEXT := lower(trim(value1));
    normalized_value2 TEXT := lower(trim(value2));
    jaro_score FLOAT;
    levenshtein_score FLOAT;
    combined_score FLOAT;
BEGIN
    -- Handle cases where either value is NULL or empty
    IF normalized_value1 IS NULL OR normalized_value2 IS NULL OR 
       normalized_value1 = '' OR normalized_value2 = '' THEN
        RETURN 0.0;
    END IF;

    -- Calculate Jaro-Winkler similarity
    jaro_score := similarity(normalized_value1, normalized_value2);

    -- Calculate Levenshtein similarity
    levenshtein_score := 1 - (levenshtein(normalized_value1, normalized_value2)::FLOAT / GREATEST(length(normalized_value1), length(normalized_value2)));

    -- Combine the scores with weights
    combined_score := 0.3 * jaro_score + 0.7 * levenshtein_score;

    RETURN combined_score;
END;
$$ LANGUAGE plpgsql;