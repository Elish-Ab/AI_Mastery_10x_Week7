SELECT *
FROM {{ source('telegram_data', 'raw_data') }} 
