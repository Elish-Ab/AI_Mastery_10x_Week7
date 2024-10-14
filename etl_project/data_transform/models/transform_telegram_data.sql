WITH raw_data AS (
    SELECT *
    FROM {{ ref('raw_data') }}  -- This should now correctly reference the raw_data model
)

SELECT 
    message_id,
    message,
    date
FROM raw_data
WHERE message IS NOT NULL
