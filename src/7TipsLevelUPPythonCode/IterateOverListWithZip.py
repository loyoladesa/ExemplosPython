teams = ['Barcelona','Bayern Munich','Chelsea']
leagues = ['La Liga','Bundesliga','Premiere League']
countries = ['Spain','Germany','UK']

for i,team in enumerate(teams):
    league = leagues[i]
    print(f'{team} plays in {league}')

for team,league,country in zip(teams,leagues,countries):
    print(f'{team} plays in {league}. Country: {country}')
    