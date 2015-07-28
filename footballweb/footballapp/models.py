from django.db import models

# Create your models here.
class League(models.Model):
	League_name = models.CharField(max_length=200)
	def __str__(self):return self.League_name


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    league = models.ForeignKey(League)
    def __str__(self):return self.team_name


class Player(models.Model):
    team = models.ForeignKey(Team)
    player_name = models.CharField(max_length=200)
    def __str__(self):return self.player_name

class Match(models.Model):
    team1 = models.ForeignKey(Team,related_name='team1')
    team2 = models.ForeignKey(Team,related_name='team2')
    date = models.DateTimeField('Match Date')
    team1score=models.IntField('score1')
    team2score=models.IntField('score2')
    result =models.CharField(max_length=200)
    
