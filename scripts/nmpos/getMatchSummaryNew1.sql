CREATE OR REPLACE FUNCTION getMatchSummaryNew(
    req_name TEXT,
    req_phone TEXT,
    req_email TEXT,
    req_address TEXT,
    req_city TEXT,
    req_state TEXT,
    req_zip TEXT,
    req_dob DATE,
    req_id_type TEXT,
    req_id_value TEXT
)
RETURNS TABLE (
    user_id INT,
    name_score FLOAT,
    phone_score FLOAT,
    email_score FLOAT,
    address_score FLOAT,
    dob_score FLOAT,
    id_score FLOAT
) AS $$
DECLARE
    request_id INT;
BEGIN
    -- Insert into requests table
    INSERT INTO requests (
        request_name, request_phone, request_email, request_address, request_dob, request_id_type, request_id_value
    ) VALUES (
        req_name, req_phone, req_email, req_address, req_dob, req_id_type, req_id_value
    ) RETURNING request_id INTO request_id;

    -- Perform the match and populate the responses table
    RETURN QUERY
    WITH matches AS (
        SELECT 
            u.user_id,
            compare_names(u.name, req_name) AS name_score,
            compare_phone_numbers(u.phone, req_phone) AS phone_score,
            compare_emails(u.email, req_email) AS email_score,
            compare_addresses_advanced(
                u.address, u.city, u.state, u.zip, 
                req_address, req_city, req_state, req_zip
            ) AS address_score,
            compare_dob(u.date_of_birth, req_dob) AS dob_score,
            CASE
                WHEN req_id_type = 'SSN' THEN compare_ids(u.ssn_value, req_id_value)
                WHEN req_id_type = 'Passport' THEN compare_ids(u.pp_value, req_id_value)
                WHEN req_id_type = 'Driving License' THEN compare_ids(u.dl_value, req_id_value)
                WHEN req_id_type = 'Others' THEN compare_ids(u.other_id_value, req_id_value)
                ELSE 0.0
            END AS id_score
        FROM nmpos_users u
        WHERE 
            compare_names(u.name, req_name) > 40.0 AND
            compare_phone_numbers(u.phone, req_phone) > 40.0 AND
            compare_emails(u.email, req_email) > 40.0 AND
            compare_addresses_advanced(
                u.address, u.city, u.state, u.zip, 
                req_address, req_city, req_state, req_zip
            ) > 40.0 OR
            compare_dob(u.date_of_birth, req_dob) > 40.0 AND
            (
                (req_id_type = 'SSN' AND compare_ids(u.ssn_value, req_id_value) > 40.0) OR
                (req_id_type = 'Passport' AND compare_ids(u.pp_value, req_id_value) > 40.0) OR
                (req_id_type = 'Driving License' AND compare_ids(u.dl_value, req_id_value) > 40.0) OR
                (req_id_type = 'Others' AND compare_ids(u.other_id_value, req_id_value) > 40.0)
            )
    )
    INSERT INTO responses (
        request_id, matched_user_id, matching_name, name_score, 
        matching_address, address_score, matching_email, email_score, 
        matching_phone, phone_score, matching_dob, dob_score, 
        matching_id_value, id_score
    )
    SELECT
        request_id, user_id, u.name, name_score,
        u.address, address_score, u.email, email_score,
        u.phone, phone_score, u.date_of_birth, dob_score,
        CASE
            WHEN req_id_type = 'SSN' THEN u.ssn_value
            WHEN req_id_type = 'Passport' THEN u.pp_value
            WHEN req_id_type = 'Driving License' THEN u.dl_value
            WHEN req_id_type = 'Others' THEN u.other_id_value
            ELSE NULL
        END, id_score
    FROM matches;
END;
$$ LANGUAGE plpgsql;
