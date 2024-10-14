{{config(materialized='table')}}

WITH source_data AS (
    SELECT *
    FROM {{ source('public', 'raw_data') }}
)
SELECT *
FROM source_data
