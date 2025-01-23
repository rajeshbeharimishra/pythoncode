CREATE OR REPLACE FUNCTION getMatchDetails(req_id INT)
RETURNS TABLE (
    request_id INT,
    matched_user_id INT,
    request_name TEXT,
    matching_name TEXT,
    name_score FLOAT,
    request_address TEXT,
    matching_address TEXT,
    address_score FLOAT,
    request_email TEXT,
    matching_email TEXT,
    email_score FLOAT,
    request_phone TEXT,
    matching_phone TEXT,
    phone_score FLOAT,
    request_dob DATE,
    matching_dob DATE,
    dob_score FLOAT,
    request_id_value TEXT,
    matching_id_value TEXT,
    id_score FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        r.request_id,
        res.matched_user_id,
        r.request_name,
        res.matching_name,
        res.name_score,
        r.request_address,
        res.matching_address,
        res.address_score,
        r.request_email,
        res.matching_email,
        res.email_score,
        r.request_phone,
        res.matching_phone,
        res.phone_score,
        r.request_dob,
        res.matching_dob,
        res.dob_score,
        r.request_id_value,
        res.matching_id_value,
        res.id_score
    FROM requests r
    JOIN responses res ON r.request_id = res.request_id
    WHERE r.request_id = req_id; -- Use the parameter `req_id` here
END;
$$ LANGUAGE plpgsql;
