with matches as (
    select * from {{ ref('stg_matches') }}
),
teams as (
    select team_id, team_name from {{ ref('dim_teams') }}
)
select
    matches.match_date as date,
    matches.matchday,
    home.team_id as home_team_id,
    away.team_id as away_team_id,
    matches.home_score,
    matches.away_score,
    matches.winner
from matches
left join teams home on matches.home_team = home.team_name
left join teams away on matches.away_team = away.team_name