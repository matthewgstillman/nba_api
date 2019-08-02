from django.shortcuts import render, redirect

import nba_api, requests, unirest
# Create your views here.
def index(request):
    players = {}
    response = requests.get('https://www.balldontlie.io/api/v1/players')
    nba_players = response.json()
    print(nba_players)
    meta = nba_players['meta']
    print(meta)
    data = nba_players['data']
    print(data)
    for i in range(0, len(data)):
        print(data[i])
        first_name = data[i]['first_name']
        last_name = data[i]['last_name']
        height_inches = data[i]['height_inches']
        height_feet = data[i]['height_feet']
        weight_pounds = data[i]['weight_pounds']
        team = data[i]['team']
        conference = data[i]['team']['conference']
        city = data[i]['team']['city']
        name = data[i]['team']['name']
        division = data[i]['team']['division']
        abbreviation = data[i]['team']['abbreviation']
        full_name = data[i]['team']['full_name']
        team_id = data[i]['team']['id']
        position = data[i]['position']
        player_id = data[i]['id']
        print("My name is {} {} and I play for the {}. I'm {} foot {} inches tall and weigh {} pounds.".format(first_name, last_name, full_name, height_feet, height_inches, weight_pounds))
        players[i] = {
            "first_name": first_name,
            "last_name": last_name,
            "height_inches": height_inches,
            "height_feet": height_feet,
            "weight": weight_pounds,
            "team": team,
            "city": city,
            "name": name,
            "division": division,
            "abbreviation": abbreviation,
            "full name": full_name,
            "team id": team_id,
            "position": position,
            "player id": player_id
        }
        context = {
            "nba_players": nba_players,
            "players": players,
        }
        return render(request, 'nba_api/index.html', context)

def players(request):
    return render(request, 'nba_api/players.html')

def stats(request):
    response = requests.get('https://www.balldontlie.io/api/v1/stats')
    stats = response.json()
    print(stats)
    meta_stats = stats['meta']
    print(meta_stats)
    data = stats['data']
    for i in range(0, len(data)):
        # print(data[i])
        field_goal_pct = data[i]['fg_pct']
        player = data[i]['player']
        player_first_name = data[i]['player']['first_name']
        player_last_name = data[i]['player']['last_name']
        player_weight = data[i]['player']['weight_pounds']
        player_team_id = data[i]['player']['team_id']
        player_height_feedt = data[i]['player']['height_feet']
        player_position = data[i]['player']['position']
        if player_position == 'G':
            player_position = 'Guard'
        elif player_position == 'F':
            player_position = 'Forward'
        elif player_position == 'C':
            player_position = 'Center'
        elif player_position =='G-F':
            player_position = 'Guard/Forward'
        elif player_position == 'F-C':
            player_position = 'Forward/Center'
        elif player_position == 'C-F':
            player_position = 'Center/Forward'
        elif player_position == 'F-G':
            player_position = "Forward/Guard"
        player_id = data[i]['player']['id']
        player_points = data[i]['pts']
        game_id = data[i]['id']
        player_minutes = data[i]['min']
        free_throws_attempted = data[i]['fta']
        free_throws_made = data[i]['ftm']
        personal_fouls = data[i]['pf']
        blocks = data[i]['blk']
        rebounds = data[i]['reb']
        free_throws_made = data[i]['ftm']
        free_throw_percentage = data[i]['ft_pct']
        three_pointers_attempted = data[i]['fg3a']
        three_pointers_made = data[i]['fg3m']
        assists = data[i]['ast']
        field_goals_made = data[i]['fgm']
        game = data[i]['game']
        game_status = data[i]['game']['status']
        visitor_team_score = data[i]['game']['visitor_team_score']
        season = data[i]['game']['season']
        period = data[i]['game']['period']
        home_team_id = data[i]['game']['home_team_id']
        visitor_team_id = data[i]['game']['visitor_team_id']
        time = data[i]['game']['time']
        date = data[i]['game']['date']
        home_team_score = data[i]['game']['home_team_score']
        box_score_id = data[i]['game']['id']
        postseason = data[i]['game']['postseason']
        three_point_percentage = data[i]['fg3_pct']
        defensive_rebounds = data[i]['fg3_pct']
        field_goals_attempted = data[i]['fga']
        steals = data[i]['stl']
        offensive_rebounds = data[i]['oreb']
        team = data[i]['team']
        team_conference = data[i]['team']['conference']
        team_city = data[i]['team']['city']
        team_name = data[i]['team']['name']
        team_division = data[i]['team']['division']
        team_abbreviation = data[i]['team']['abbreviation']
        team_full_name = data[i]['team']['full_name']
        team_id = data[i]['team']['id']
        turnovers = data[i]['turnover']
        print("My name is {} {}, and I play {} for the {}".format(player_first_name, player_last_name, player_position, team_full_name))

        context = {
            'response': response,
            'stats': stats,
            'data': data
        }
    return render(request, 'nba_api/stats.html', context) 