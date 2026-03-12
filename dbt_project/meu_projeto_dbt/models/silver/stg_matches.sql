with source as (
    select * from {{ source('raw', 'matches') }}
),
renamed as (
    select
        date as match_date,
        matchday,
        home_team,
        away_team,
        home_score,
        away_score,
        winner,
        status,
        _ingested_at
    from source
)
select * from renamed