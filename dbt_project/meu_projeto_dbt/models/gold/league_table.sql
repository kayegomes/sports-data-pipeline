with home_stats as (
    select
        home_team as team,
        count(*) as matches_home,
        sum(case when winner = 'HOME_TEAM' then 1 else 0 end) as wins_home,
        sum(case when winner = 'AWAY_TEAM' then 1 else 0 end) as losses_home,
        sum(case when winner = 'DRAW' then 1 else 0 end) as draws_home
    from {{ ref('stg_matches') }}
    group by home_team
),
away_stats as (
    select
        away_team as team,
        count(*) as matches_away,
        sum(case when winner = 'AWAY_TEAM' then 1 else 0 end) as wins_away,
        sum(case when winner = 'HOME_TEAM' then 1 else 0 end) as losses_away,
        sum(case when winner = 'DRAW' then 1 else 0 end) as draws_away
    from {{ ref('stg_matches') }}
    group by away_team
),
team_stats as (
    select
        coalesce(h.team, a.team) as team,
        coalesce(h.matches_home, 0) + coalesce(a.matches_away, 0) as matches,
        coalesce(h.wins_home, 0) + coalesce(a.wins_away, 0) as wins,
        coalesce(h.draws_home, 0) + coalesce(a.draws_away, 0) as draws,
        coalesce(h.losses_home, 0) + coalesce(a.losses_away, 0) as losses
    from home_stats h
    full outer join away_stats a on h.team = a.team
)
select
    team,
    matches,
    wins,
    draws,
    losses,
    (wins * 3 + draws) as points
from team_stats
order by points desc