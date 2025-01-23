CREATE OR REPLACE FUNCTION compare_names(name1 TEXT, name2 TEXT)
RETURNS FLOAT AS $$
DECLARE
    -- Name parts for Name1
    first_name1 TEXT := split_part(name1, ' ', 1);
    middle_name1 TEXT := CASE WHEN array_length(string_to_array(name1, ' '), 1) = 3 THEN split_part(name1, ' ', 2) ELSE '' END;
    last_name1 TEXT := split_part(name1, ' ', array_length(string_to_array(name1, ' '), 1));

    -- Name parts for Name2
    first_name2 TEXT := split_part(name2, ' ', 1);
    middle_name2 TEXT := CASE WHEN array_length(string_to_array(name2, ' '), 1) = 3 THEN split_part(name2, ' ', 2) ELSE '' END;
    last_name2 TEXT := split_part(name2, ' ', array_length(string_to_array(name2, ' '), 1));

    -- Similarity scores
    soundex_score_first BOOLEAN;
    soundex_score_middle BOOLEAN;
    soundex_score_last BOOLEAN;

    jaro_score_first FLOAT;
    jaro_score_middle FLOAT;
    jaro_score_last FLOAT;

    levenshtein_score_first FLOAT;
    levenshtein_score_middle FLOAT;
    levenshtein_score_last FLOAT;

    name_score FLOAT;
BEGIN
    -- Normalize names (convert to lowercase and trim spaces)
    first_name1 := lower(trim(both from first_name1));
    middle_name1 := lower(trim(both from middle_name1));
    last_name1 := lower(trim(both from last_name1));

    first_name2 := lower(trim(both from first_name2));
    middle_name2 := lower(trim(both from middle_name2));
    last_name2 := lower(trim(both from last_name2));

    -- Compute Soundex similarity
    soundex_score_first := soundex(first_name1) = soundex(first_name2);
    soundex_score_middle := soundex(middle_name1) = soundex(middle_name2) AND middle_name1 <> '' AND middle_name2 <> '';
    soundex_score_last := soundex(last_name1) = soundex(last_name2);

    -- Compute Jaro-Winkler similarity
    jaro_score_first := similarity(first_name1, first_name2);
    jaro_score_middle := similarity(middle_name1, middle_name2);
    jaro_score_last := similarity(last_name1, last_name2);

    -- Compute Levenshtein similarity
    levenshtein_score_first := CASE
        WHEN length(first_name1) > 0 AND length(first_name2) > 0 THEN
            1 - (levenshtein(first_name1, first_name2)::FLOAT / GREATEST(length(first_name1), length(first_name2)))
        ELSE 0
    END;

    levenshtein_score_middle := CASE
        WHEN length(middle_name1) > 0 AND length(middle_name2) > 0 THEN
            1 - (levenshtein(middle_name1, middle_name2)::FLOAT / GREATEST(length(middle_name1), length(middle_name2)))
        ELSE 0
    END;

    levenshtein_score_last := CASE
        WHEN length(last_name1) > 0 AND length(last_name2) > 0 THEN
            1 - (levenshtein(last_name1, last_name2)::FLOAT / GREATEST(length(last_name1), length(last_name2)))
        ELSE 0
    END;

    -- Compute the overall name similarity score
    IF middle_name1 <> '' AND middle_name2 <> '' THEN
        name_score := (
            0.3 * (CAST(soundex_score_first AS INT) + jaro_score_first + levenshtein_score_first) / 3 +
            0.15 * (CAST(soundex_score_middle AS INT) + jaro_score_middle + levenshtein_score_middle) / 3 +
            0.55 * (CAST(soundex_score_last AS INT) + jaro_score_last + levenshtein_score_last) / 3
        );
    ELSE
        name_score := (
            0.4 * (CAST(soundex_score_first AS INT) + jaro_score_first + levenshtein_score_first) / 3 +
            0.6 * (CAST(soundex_score_last AS INT) + jaro_score_last + levenshtein_score_last) / 3
        );
    END IF;

    RETURN round(name_score::NUMERIC * 100, 2);
END;
$$ LANGUAGE plpgsql;