CREATE OR REPLACE FUNCTION compare_dob(dob1 DATE, dob2 DATE)
RETURNS FLOAT AS $$
BEGIN
    -- Exact match
    IF dob1 = dob2 THEN
        RETURN 100.0;
    END IF;

    -- Check for transposed month and day
    IF dob1 IS NOT NULL AND dob2 IS NOT NULL THEN
        IF (EXTRACT(YEAR FROM dob1) = EXTRACT(YEAR FROM dob2)) AND
           (EXTRACT(MONTH FROM dob1) = EXTRACT(DAY FROM dob2)) AND
           (EXTRACT(DAY FROM dob1) = EXTRACT(MONTH FROM dob2)) THEN
            RETURN 80.0;
        END IF;

        -- Check year-only match
        IF EXTRACT(YEAR FROM dob1) = EXTRACT(YEAR FROM dob2) THEN
            IF EXTRACT(MONTH FROM dob1) = EXTRACT(MONTH FROM dob2) OR
               EXTRACT(DAY FROM dob1) = EXTRACT(DAY FROM dob2) THEN
                RETURN 60.0; -- Partial match on year and one other component
            END IF;
            RETURN 50.0; -- Partial match on year only
        END IF;

        -- Check if month and day match regardless of year
        IF EXTRACT(MONTH FROM dob1) = EXTRACT(MONTH FROM dob2) AND
           EXTRACT(DAY FROM dob1) = EXTRACT(DAY FROM dob2) THEN
            RETURN 70.0; -- Partial match on month and day
        END IF;
    END IF;

    -- No significant match
    RETURN 0.0;
END;
$$ LANGUAGE plpgsql;