CREATE OR REPLACE FUNCTION getMatchSummary(
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
BEGIN
    RETURN QUERY
    SELECT 
        u.user_id,
        compare_names(u.name, req_name) AS name_score,
        compare_phone_numbers(u.phone, req_phone) AS phone_score,
        compare_emails(u.email, req_email) AS email_score,
        compare_addresses(
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
        -- Ensure at indivisual attribute score is greater than 40.0
        (
            compare_names(u.name, req_name) > 40.0 AND
            compare_phone_numbers(u.phone, req_phone) > 40.0 AND
            compare_emails(u.email, req_email) > 40.0 AND
            compare_addresses(
                u.address, u.city, u.state, u.zip, 
                req_address, req_city, req_state, req_zip
            ) > 40.0 AND
            compare_dob(u.date_of_birth, req_dob) > 40.0 AND
            (
                (req_id_type = 'SSN' AND compare_ids(u.ssn_value, req_id_value) > 40.0) OR
                (req_id_type = 'Passport' AND compare_ids(u.pp_value, req_id_value) > 40.0) OR
                (req_id_type = 'Driving License' AND compare_ids(u.dl_value, req_id_value) > 40.0) OR
                (req_id_type = 'Others' AND compare_ids(u.other_id_value, req_id_value) > 40.0)
            )
        )
    ORDER BY name_score DESC, phone_score DESC;
END;
$$ LANGUAGE plpgsql;
