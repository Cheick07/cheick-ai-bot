create table matches (
  id serial primary key,
  home_team text,
  away_team text,
  date date,
  league text
);

create table predictions (
  id serial primary key,
  match_id integer references matches(id),
  home_win float,
  draw float,
  away_win float
);

create table leaks (
  id serial primary key,
  match_id integer references matches(id),
  source text,
  prediction text,
  timestamp timestamptz
);
