CREATE OR REPLACE FUNCTION compare_addresses(
    addr1 TEXT, 
    city1 TEXT, 
    state1 TEXT, 
    zip1 TEXT, 
    addr2 TEXT, 
    city2 TEXT, 
    state2 TEXT, 
    zip2 TEXT
)
RETURNS FLOAT AS $$
DECLARE
    addr_similarity FLOAT;
    city_similarity FLOAT;
    state_similarity FLOAT;
    zip_similarity FLOAT;
    string_similarity FLOAT;
BEGIN
    -- Compute component-wise similarities
    addr_similarity := combined_similarity(addr1, addr2);
    city_similarity := combined_similarity(city1, city2);
    state_similarity := combined_similarity(state1, state2);

    -- Handle exact match for zip
    IF TRIM(zip1) = TRIM(zip2) THEN
        zip_similarity := 1.0;
    ELSE
        zip_similarity := combined_similarity(zip1, zip2);
    END IF;

    -- Compute the weighted average similarity
    string_similarity := 
        0.4 * addr_similarity +
        0.15 * city_similarity +
        0.15 * state_similarity +
        0.3 * zip_similarity;

    -- Return the computed similarity
	RETURN round(string_similarity ::NUMERIC * 100, 2);
END;
$$ LANGUAGE plpgsql;