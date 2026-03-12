with teams as (
    select distinct home_team as team_name
    from {{ ref('stg_matches') }}
    union distinct
    select distinct away_team as team_name
    from {{ ref('stg_matches') }}
)
select
    row_number() over (order by team_name) as team_id,
    team_name
from teams
order by team_name