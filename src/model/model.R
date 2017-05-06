library(ggplot2)
library(alr4)
library(tidyverse)
library(stringr)

setwd("~/Documents/Columbia/msd-apam4990/msd-final-project/src")

track_uri_df = read.delim("track_uri.txt", sep="|")
colnames(track_uri_df) <- c("song", "uri")
track_uri_df[] <- lapply(track_uri_df, as.character)

track_uri_df <- track_uri_df %>%
  separate(uri, into=c("spotify", "track_rep", "uri"), sep=":") %>%
  select(song, uri)

song_ranks_weeks = read.delim("song_rank_weeks.txt",sep="|")
colnames(song_ranks_weeks) <- c("song", "week", "rank")

audio_features = read.delim("../audio_features.txt", sep="|")

names <- c("track_href", "analysis_url","energy", "liveness", "tempo",
           "speechiness", "uri", "acousticness", "instrumentalness",
           "time_signature", "danceability", "key", "duration_ms",
           "loudness", "valence", "type", "id", "mode")

colnames(audio_features) <- names


audio_features <- audio_features %>%
  separate(uri, into=c("spotify", "track_rep", "uri"), sep=":")

drops <- c("spotify", "track_rep", "type", "track_href", "analysis_url",
           "id", "mode")
audio_features$uri <- as.factor(audio_features$uri)
audio_features <- audio_features[, !(names(audio_features) %in% drops)]

uri_songs_weeks_df <- track_uri_df %>%
  inner_join(song_ranks_weeks, by="song")

final_df <- uri_songs_weeks_df %>%
  inner_join(audio_features, by='uri')


model <- lm(week ~ acousticness + energy + key + loudness + tempo, 
            data=final_df)

sqrt(mean(model$residuals^2))
sqrt(sum(model$residuals))

summary(model)
invResPlot(model)


all_model <- lm(week ~ . , data=final_df)


model <- lm(week ~ acousticness + energy + key + loudness + mode + tempo, 
            data=final_df)
step(model, scope = ~ 1, direction="backward")

all_var <- lm(week ~ . - spotify - track_rep, data=final_df)

rank_week <- lm(rank ~ week + tempo, data=final_df)
summary(rank_week)

rank <- lm(rank ~ week, data=final_df)

summary(rank)

plot(rank)

rank_log <- lm(log(rank) ~ week, data=final_df)
summary(rank_log)

plot(rank_log)

rank_energy <- lm(rank ~ week*energy, data=final_df)
summary(rank_energy)
plot(rank_energy)

anova(rank, rank_energy, rank_week)
